#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import subprocess
import copy
import time
import optparse

import networkx as nx

import antlr3
import antlr3.tree
from antlr_files.LTLMPLexer import LTLMPLexer
from antlr_files.LTLMPParser import LTLMPParser
from antlr_files.LTLMPTree import LTLMPTree

#from tree_ltlmp import Tree
import tree_ltlmp as tltl
import generate_graph as gg
import translate_tree as tmtc
import runsmt


def get_weighted_graph(graph, mp_prop_pair, opts):
    # MPList_i = mp_prop_pair['mp']
    # MPPropsList_i = mp_prop_pair['prop']

    # input: graph(automaton) mdg
    if opts.tgba:
        mdg = nx.MultiDiGraph(acccond=graph.graph['acccond'])
    else:
        mdg = nx.MultiDiGraph()

    for node in graph.nodes():
        mdg.add_node(node)

    for edge in graph.edges(data=True):

        DPsList = edge[2]['condList']
        if opts.pdebug:
            print DPsList
        # get Undecidable Prop List by removing DP from mpproplist
        UDPs = set([]) # UDPList According to 'Cond-or List'
        if DPsList == []:
            for mp_prop in mp_prop_pair:
                mpprops_ = set(mp_prop['prop'])
                UDPs = UDPs | mpprops_
        else:
            for DPs in DPsList:
                for mp_prop in mp_prop_pair:
                    mpprops_ = set(mp_prop['prop'])
                    mpprops_ = mpprops_ - set(DPs[0])
                    mpprops_ = mpprops_ - set(DPs[1])
                    UDPs = UDPs | mpprops_
        UDPs = list(UDPs)

        '    ---- decide weight for Dicidable Props ----'
        # Decide 0-1 for each MPtree
        mpsList_per_DPs = []
        # mplist * number of (DPs | DPs | DPs)
        # DPsList = (DPs | DPs | DPs)
        for DPs in DPsList:
            mps_ = []
            for mp_prop in mp_prop_pair:
                mp_ = copy.deepcopy(mp_prop['mp'])
                for dp in DPs[0]:
                    tltl.decide_cond_pos(mp_, dp)
                for dp in DPs[1]:
                    tltl.decide_cond_neg(mp_, dp)
                mps_.append(mp_)
            mpsList_per_DPs.append(mps_)
        # preudp [mp num][cond-or num]
        '    ---- decision Complete ----'

        mpsList_Preweight = []
        for mps in mpsList_per_DPs:
            if UDPs == []:
                m = [mps]
            else:
                m = tltl.get_weighted_uhlan(mps, UDPs)
            mpsList_Preweight.extend(m)

        # weights : weight per MP on 1 transition
        w8sList = []
        for mps in mpsList_Preweight:
            w8s = []
            for mp in mps:
                exec "w = " + (tmtc.mp_out(mp.child[0]))
                # MP(t)~c ---> MP(t-c)~0
                w = w - int(mp.const)
                w8s.append(w)
            w8sList.append(w8s)

        # remove weight overlap in each edge
        w8list = []
        for w8 in w8sList:
            if not w8 in w8list:
                w8list.append(w8)
        mdg.add_node(edge[0])
        mdg.add_node(edge[1])
        if opts.tgba:
            for w8 in w8list:
                mdg.add_edge(edge[0], edge[1], weight=w8, acc=edge[2]['acc'])
        else:
            for w8 in w8list:
                mdg.add_edge(edge[0], edge[1], weight=w8)
        if opts.pdebug:
            for w8 in w8list:
                print '    '+str(edge[0])+' --> '+str(edge[1])+'  w8: '+str(w8)
    return mdg


def get_SMTCode(mdg, mp_prop, opts):
    # input mdg
    # output SMTCode list, result per 
    results = {'SCCs': [], 'AccSCCs': []}
    if opts.tgba:
        all_acceptlist = mdg.graph['acccond']
    SCCs = nx.strongly_connected_component_subgraphs(mdg)
    for scc in SCCs:
        results['SCCs'].append({'edges':nx.number_of_edges(scc), 'nodes':nx.number_of_nodes(scc)})
        if scc.edges() == []:
            pass
        else:
            # nx.draw_circular(scc)
            accept = 0
            if opts.tgba:
                a = reduce(lambda x, y : x | y , [set(edge[2]['acc']) for edge in scc.edges(data=True)])
                print a
                acceptlist = list(a)
                print acceptlist
                """for edge in scc.edges(data=True):
                    for acc in edge[2]['acc']:
                        if not acc in acceptlist:
                            acceptlist.append(acc)
                    if opts.debug:
                        print acceptlist
                        """
                if all_acceptlist.sort() == acceptlist.sort():
                    if opts.pdebug:
                        print acceptlist,' ==? ',all_acceptlist
                    print '  TGBA-Accept'
                    accept = 1
            else:
                for node in scc.nodes():
                    if 'accept' in node:
                        accept = 1
                        break

            if accept == 1:
                if opts.debug:
                    print '\t found BA/TGBA-Accept SCC'
                code_time = runsmt.gen_smtcodelist_time(scc, mp_prop, opts)
                results['AccSCCs'].append({'SMTCode':code_time['code'],
                                           'edges':nx.number_of_edges(scc), 'nodes':nx.number_of_nodes(scc),
                                           'gen_time':code_time['time'], 'sat_time':0})
            else:
                if opts.pdebug:
                    print ' non accept SCC'
    return results

def execute_smt_solver(codes_ext, opts):
    result_list = {'time':'a'}
    cmd_smt = './yices yicesinput'
    unsat_scc = 0

    st = time.time()
    for codes in codes_ext:
        if opts.showprogress: print '     ---- solving Constraints ---- '
        with open('yicesinput', 'w') as yinput:
            for code in codes:
                if opts.pdebug:
                    print code
                yinput.write(str(code)+'\n')
        smt_solver = subprocess.Popen(cmd_smt, shell=True, close_fds=True, stdout=subprocess.PIPE)

        for line in smt_solver.stdout:
            if 'unsat' in line:
                if opts.showprogress:
                    print '        unsat in SCC'
                unsat_scc = 1
                break

    en = time.time()
    sattime = str(en-st) +  '  -- CSP solve Completion Time:  '
    result_list['time'] = sattime
    print sattime

    if unsat_scc == 0:
        result_list['sat'] = True
        return result_list
    result_list['sat'] = False
    return result_list

'''
def convert_ltl_to_graph(ltl, opts):
    ltl_string = tmtc.ltl_out(ltl)

    if opts.tgba:
        cmd = 'ltl2tgba --low -f ' + '\'' + ltl_string + '\''
    elif opts.ltltrans:
        cmd = './translator/ltltrans -f ' + '\'' + ltl_string + '\''
    else:
        cmd = './translator/ltl3ba -f ' + '\'' + ltl_string + '\''
    st = time.time()
    constime = time.time()
    ltl2tgba = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE)
    out = ltl2tgba.stdout
    graph = gg.tgba2graph(out, constime, opts)
    en = time.time()
    extime = en-st
    return graph, extime
'''

def graph_tgba(pair, opts):
    # input: TGBA
    # output: results{'graph', 'time'}
    #     
    results = {'mp-prop-pair': []}

    ltl = pair[0]
    mp_list = pair[1]

    cmd_ltl2tgba = 'ltl2tgba --low -f ' + '\'' +tmtc.ltl_out(ltl)+ '\''
    st = time.time()
    constime = time.time()
    ltl2tgba = subprocess.Popen(cmd_ltl2tgba, shell=True, close_fds=True, stdout=subprocess.PIPE)
    out = ltl2tgba.stdout
    graph = gg.tgba2graph(out, constime, opts)
    if graph:
        props = []
        for mp in mp_list:
            results['mp-prop-pair'].append({'mp':tltl._simplify_all_term_in_mp(mp), 'prop':tltl.get_proplist(mp)})
        results['graph'] = graph
        if opts.pdebug: print "\t\tprops:", props
        en = time.time()
        tctime = str(en-st)
        print tctime + '  -- ltl2tgba -> Graph  Conversion Time '
        results['time'] = tctime
        return results
    else:
        return False

def graph_ltltrans(pair, opts):
    # input: TGBA
    # output: results{'graph', 'time'}
    #     
    results = {'mp-prop-pair':[]}
    # temp
    ltl = pair[0]
    mplist = pair[1]
    cmd_ltltrans = './translator/ltltrans -f ' + '\'' +tmtc.ltl_out_trans(ltl)+ '\''
    st = time.time()
    ltltrans = subprocess.Popen(cmd_ltltrans,shell=True,close_fds=True,stdout=subprocess.PIPE)
    out = ltltrans.stdout
    graph = gg.ltltrans2graph(out, st, opts)
    if graph:
        props = []
        for mp in mplist:
            results['mp-prop-pair'].append({'mp':tltl._simplify_all_term_in_mp(mp), 'prop':tltl.get_proplist(mp)})
        results['graph'] = graph
        # results['mplist'] = copy.deepcopy(mplist)
        # results['mpprops'] = props
        if opts.pdebug:
            print "    props:",props
        en = time.time()
        tctime = str(en-st)
        print tctime + '  -- ltltrans -> Graph  Conversion Time '
        results['time'] = tctime
        return results
    else:
        return False

def graph_ba(pair, opts):
    # input: TGBA
    # output: results{'graph', 'time'}
    #     
    results = {'mp-prop-pair':[]}
    # temp
    ltl = pair[0]
    mplist = pair[1]
    cmd_ltl3ba = './translator/ltl3ba -f ' + '\'' +tmtc.ltl_out(ltl)+ '\''
    st = time.time()
    ltl3ba = subprocess.Popen(cmd_ltl3ba, shell=True,close_fds=True,stdout=subprocess.PIPE)
    out = ltl3ba.stdout
    graph = gg.nvc2graph(out, st, opts)
    if graph:
        props = []
        for mp in mplist:
            results['mp-prop-pair'].append({'mp':tltl._simplify_all_term_in_mp(mp), 'prop':tltl.get_proplist(mp)})
        results['graph'] = graph
        # results['mplist'] = copy.deepcopy(mplist)
        # results['mpprops'] = props
        if opts.pdebug:
            print "    props:",props
        en = time.time()
        tctime = str(en-st)
        print tctime + '  -- ltl3ba -> Graph  Total Construction Time '
        results['time'] = tctime
        return results
    else:
        return False

def parse_input(formula):

    print "----- Parsing ", repr(formula), '-----'
    char_stream = antlr3.ANTLRStringStream(formula)
    lexer = LTLMPLexer(char_stream)
    tokens = antlr3.CommonTokenStream(lexer)
    parser = LTLMPParser(tokens)
    r = parser.start()
    ast_root = r.tree # root of the AST(Type: CommonTree(antlr))

    if opts.showprogress:
        print "----- Parsing Done -----"

    if opts.debug:
        print "----- Tree Parsing -----"

    nodes = antlr3.tree.CommonTreeNodeStream(ast_root)
    nodes.setTokenStream(tokens)
    evaltree = LTLMPTree(nodes)
    ltlmp_root = evaltree.expr()
    if opts.debug:
        print "----- Tree Parsing Done -----"

    return ltlmp_root

def make_graph(pairList, MPNF_List, opts):
    if opts.tgba:
        for pair in pairList:
            g = graph_tgba(pair, opts)
            if g:
                MPNF_List.append(g)
    elif opts.ltltrans:
        for pair in pairList:
            g = graph_ltltrans(pair, opts)
            if g:
                MPNF_List.append(g)
    else:
        for pair in pairList:
            g = graph_ba(pair, opts)
            if g:
                MPNF_List.append(g)

def make_graph2(pair_list, opts):
    mpnf_list = []
    if opts.tgba:
        for pair in pair_list:
            g = graph_tgba(pair, opts)
            if g:
                mpnf_list.append(g)
    elif opts.ltltrans:
        for pair in pair_list:
            g = graph_ltltrans(pair, opts)
            if g:
                mpnf_list.append(g)
    else:
        for pair in pair_list:
            g = graph_ba(pair, opts)
            if g:
                mpnf_list.append(g)
    return mpnf_list

def show_progress1(ltlmp_root):
    print '----- AST Parse Result -----'
    print tmtc.ltl_out(ltlmp_root)
    print '----- End AST Parse Reslt-----'
    print '----- LTLMP to Nomal Form List -----'

def debug1(pairList):
    print '----- Printing MP-NF Result -----'
    for pair in pairList:
        print '  --', tmtc.ltl_out(pair[0]), '--'
        for mp in pair[1]:
            print '   ', tmtc.mp_out(mp)

def convert_mpnf(mpnf):
    graph = mpnf['graph']
    pair = mpnf['mp-prop-pair']

    st = time.time()
    mpnf['mdg'] = get_weighted_graph(graph, pair, opts)
    mdg = mpnf['mdg']
    en = time.time()

    res_graph = {'nodes': nx.number_of_nodes(graph),
                 'edges': nx.number_of_edges(graph),
                 'scclist': {'nodes': [], 'edges': []},
                 'mdg_nodes': nx.number_of_nodes(mdg),
                 'mdg_edges': nx.number_of_edges(mdg),
                 'time': str(en - st)}
    mpnf['graph_result'] = res_graph

    ##############
def convert_mpnf2(mp_and_prop_pair, graph):
    mdg = get_weighted_graph(graph, mp_and_prop_pair, opts)
    return mdg


def show_progress2(MPNF_List):
    print '  -------- temporal result ---------'
    for mpnf in MPNF_List:
        print str(mpnf['graph_result']['nodes']) + '  --   Nodes'
        print str(mpnf['graph_result']['edges']) + '  --   Edges'
        print str(mpnf['graph_result']['time']) + ' -- Weighted Graph Generating Time: '

    if opts.showprogress:
        print '----- end weighted Graph ----'

    '  -- Total Weighted Graph Generating Time:  '
    #print str(wg_en - wg_st) + '  -- Total Weighted Graph Generating Time:  '
    print '  -------- temporal result ---------'
    for mpnf in MPNF_List:
        print str(mpnf['graph_result']['mdg_nodes'])+'  --   Nodes'
        print str(mpnf['graph_result']['mdg_edges'])+'  --   Edges'

def show_progress3(MPNF_List):
    print '  -------- temporal result ---------'
    for mpnf in MPNF_List:
        # mpnf- 'Code/SCC' - 'AccSCCs' - 'sat-time'
        for accscc in mpnf['Code/SCC']['AccSCCs']:
            print str(accscc['nodes'])+'  --  AccSCC Nodes'
            print str(accscc['edges'])+'  --  AccSCC Edges'
        print str(mpnf['graph_result']['nodes'])+'  --   Nodes'
        print str(mpnf['graph_result']['edges'])+'  --   Edges'


class SatContent:
    class MpnfUnit:
        class SccUnit:
            def __init__(self, smt_code, smt_gen_time, opts):
                self.smt_code = smt_code
                self.opts = opts
                self.time = [('smt_gencode_time', smt_gen_time)]

            def execute_smt_solver(self):
                cmd_smt = './yices yicesinput'
                filename = 'yicesinput'
                unsat = 0

                for codes in self.smt_code:
                    '     ---- solving Constraints ---- '
                    with open(filename, 'w') as yinput:
                        for code in codes:
                            yinput.write(str(code)+'\n')

                    smt_solver = subprocess.Popen(cmd_smt, shell=True, close_fds=True, stdout=subprocess.PIPE)

                    for line in smt_solver.stdout:
                        if 'unsat' in line:
                            unsat = 1
                            break

                if unsat == 0:
                    return True
                return False

            def sat(self):
                st = time.time()
                torf = self.execute_smt_solver()
                en = time.time()
                self.time.append(('smt_solver_execute_time', en - st))
                return torf

            def print_result(self):
                for tm in self.time:
                    print "\t\t", tm[0], "\t", tm[1]

        def __init__(self, pair, opts):
            self.graph = None
            self.mpnf = None
            self.pair = pair
            self.time = []
            self.info = []
            self.mdg = None
            self.sccs = []
            self.sat_or_list = []
            self.opts = opts
            self.pair_mp_prop = []

        def make_graph(self):
            st = time.time()
            self.pair_mp_prop = [{'mp': tltl._simplify_all_term_in_mp(mp),
                                  'prop': tltl.get_proplist(mp)}
                                 for mp in self.pair[1]]
            self.graph = self._make_graph_by_opts()
            en = time.time()
            self.time.append(('make_graph(scc_u):', en - st))

            if not self.graph:
                #print "non-graph"
                raise ValueError
            else:
                #self._show_graph_info(self.graph)
                pass

        def _make_graph_by_opts(self):
            ltl = self.pair[0]

            if opts.tgba:
                print "-- TGBA!"
                cmd_ltl2tgba = 'ltl2tgba --low -f ' + '\'' + tmtc.ltl_out(ltl) + '\''
                ltl2tgba = subprocess.Popen(cmd_ltl2tgba, shell=True, close_fds=True, stdout=subprocess.PIPE)
                out = ltl2tgba.stdout
                graph = gg.tgba2graph(out, time.time(), self.opts)
            elif opts.ltltrans:
                cmd_ltltrans = './translator/ltltrans -f ' + '\'' + tmtc.ltl_out_trans(ltl) + '\''
                ltltrans = subprocess.Popen(cmd_ltltrans, shell=True, close_fds=True, stdout=subprocess.PIPE)
                out = ltltrans.stdout
                graph = gg.ltltrans2graph(out, time.time(), self.opts)
            else:
                print "-- BA!"
                cmd_ltl3ba = './translator/ltl3ba -f ' + "'" + tmtc.ltl_out(ltl) + "'"
                ltl3ba = subprocess.Popen(cmd_ltl3ba, shell=True, close_fds=True, stdout=subprocess.PIPE)
                out = ltl3ba.stdout
                graph = gg.nvc2graph(out, time.time(), self.opts)

            return graph

        @staticmethod
        def _show_graph_info(graph):
            print 'nodes:', nx.number_of_nodes(graph), '\t edges:', nx.number_of_edges(graph)

        def generate_smtcode(self):
            st = time.time()

            sccs = self._gen_sccs(self.graph)

            for scc in sccs:
                self.mdg = get_weighted_graph(scc, self.pair_mp_prop, self.opts)

            self.info.extend([('g_nodes', nx.number_of_nodes(self.graph)),
                              ('g_edges', nx.number_of_edges(self.graph)),
                                    ('mdg_nodes', nx.number_of_nodes(self.mdg)),
                                    ('mdg_edges', nx.number_of_edges(self.mdg))])

            self._gen_smt_from_graph(sccs)
            en = time.time()

            self.time.append(('total gen_smt: graph->scc->mdg(scc)', en - st))


        def generate_smtcode_old(self): #convert_mpnf
            st = time.time()
            self.mdg = get_weighted_graph(self.graph, self.pair_mp_prop, self.opts)

            self.info.extend([('g_nodes', nx.number_of_nodes(self.graph)),
                                    ('g_edges', nx.number_of_edges(self.graph)),
                                    ('mdg_nodes', nx.number_of_nodes(self.mdg)),
                                    ('mdg_edges', nx.number_of_edges(self.mdg))])

            sccs = self._gen_sccs(self.mdg)

            self._gen_smt_from_graph(sccs)

            en = time.time()
            self.time.append(('total gen_smt: graph->mdg->mdg(scc)', en - st))

        def _gen_sccs(self, digraph):
            st = time.time()
            g = nx.strongly_connected_component_subgraphs(digraph)
            en = time.time()
            print '\t\t\t scc time:', en - st
            return g

        def _gen_smt_from_graph(self, sccs):
            def gen_smt(sat_or_list, scc, mp_prop, opts):
                if scc.edges() == []:
                    pass
                else:
                    accept = 0
                    if opts.tgba:
                        #all_acceptlist = mdg.graph['acccond']
                        all_acceptlist = scc.graph['acccond']
                        a = reduce(lambda x, y: x | y,
                                   [set(edge[2]['acc']) for edge in scc.edges(data=True)])
                        accept_list = list(a)
                        if all_acceptlist.sort() == accept_list.sort():
                            accept = 1
                    else:
                        for node in scc.nodes():
                            if 'accept' in node:
                                accept = 1
                                break

                    if accept == 1:
                        code_and_time = runsmt.gen_smtcodelist_time(scc, mp_prop, opts)
                        code = code_and_time['code']
                        time = code_and_time['time']
                        sat_or_list.append(self.SccUnit(code, time, opts))

            for scc_mdg in sccs:
                gen_smt(self.sat_or_list, scc_mdg, self.pair_mp_prop, self.opts)

        def do_sat(self):
            st = time.time()
            for or_unit in self.sat_or_list:
                if or_unit.sat():
                    en = time.time()
                    self.time.append(('do_sat(total_ex_smt):', en - st))
                    return True
            en = time.time()
            self.time.append(('do_sat(total_ex_smt / mpnf):', en - st))
            return False

        def print_result(self):
            for tm in self.time:
                print "\t", tm[0], "\t", tm[1]
            for inf in self.info:
                print "\t\t", inf[0], "\t", inf[1]
            for oru in self.sat_or_list:
                oru.print_result()


    def __init__(self, ltl_mp_pair_list, options):
        self.mpnf_list = []
        self.sat_units = []
        self.opts = options
        self.time = []
        self.sat = None
        self.results = []
        for pair in ltl_mp_pair_list:
            self.sat_units.append(self.MpnfUnit(pair, self.opts))

    def strat_all_through(self):
        print 'sat_units:', len(self.sat_units), self.sat_units
        cnt = 0
        for unit in self.sat_units:
            print "unit", cnt
            cnt += 1
            try:
                unit.make_graph()
                unit.generate_smtcode()
                a = unit.do_sat()
                self.results.append(a)
                if a == True:
                    return 0
            except ValueError:
                print "unit abort: nothing do more"

    def strat_all_through_old(self):
        st = time.time()
        print 'sat_units:', len(self.sat_units), self.sat_units
        cnt = 0
        for unit in self.sat_units:
            print "unit", cnt
            cnt += 1
            try:
                unit.make_graph()
                unit.generate_smtcode_old()
                a = unit.do_sat()
                self.results.append(a)
            except ValueError:
                print "unit abort: nothing do more"
        en = time.time()
        self.time.append(('total sat time:', en - st))

    def strat_broad(self):
        for unit in self.sat_units: # per SCC
            st = time.time()
            if unit.do_sat():
                self.sat = True
                return True
            en = time.time()
            self.time.append(('execute_time', en - st))
        'totally unsat'
        self.sat = False
        return False

    def _make_graph(self):
        for unit in self.sat_units:
            self.mpnf_list.append(unit.make_graph())

    def _convert_graph_to_mdg(self):
        st = time.time()
        for unit in self.sat_units:
            unit.convert_graph_to_mdg()
        en = time.time()
        self.time.append(('total_gen_mdg', en - st))

    def _generate_smtcode(self):
        for unit in self.sat_units:
            unit.generate_smtcode()

    def print_result(self):
        print '---Result---'
        print "SAT?   : ", self.sat
        print "results: ", self.results
        for tm in self.time:
            print tm[0], "\t", tm[1]
        for unit in self.sat_units:
            unit.print_result()
        print '------------'


def satmain2(formula, opts):
    ltlmp_root = parse_input(formula)

    # or-list of and-pair of (ltl, [mp, ..])
    # [(ltl, [mp]), (ltl, [mp]), ...]
    ltl_mp_pair_list = tltl.get_mpnf_list(ltlmp_root)

    # FUTURE: improve LTL tree
    sat_content = SatContent(ltl_mp_pair_list, opts)
    sat_content.strat_all_through_old()
    sat_content.print_result()


def satmain(formula, opts):
    total_result = {'sat': False, 'time': [], 'graphs': [], 'total_wg_time': 0.0 }

    ltlmp_root = parse_input(formula)
    if opts.showprogress: show_progress1(ltlmp_root)

    # or-list of and-pair (ltl, mp)
    ltl_mp_pair_list = tltl.get_mpnf_list(ltlmp_root)
    if opts.debug: debug1(ltl_mp_pair_list)

    # FUTURE: improve LTL tree

    mpnf_list = []
    make_graph(ltl_mp_pair_list, mpnf_list, opts)


    if opts.showprogress: print '---- Weighted Graph generating ----'

    wg_st = time.time()
    for mpnf in mpnf_list:
        convert_mpnf(mpnf)
    wg_en = time.time()
    total_result['total_wg_time'] = wg_en - wg_st

    show_progress2(mpnf_list)
    if opts.showprogress: print '---- SMT input generating ----'

    # for SCC which includes 'accept' state'
    #     do SAT
    # convert Weighted Graph to SMT-Solver Sentence
    for mpnf in mpnf_list:
        mpnf['Code/SCC'] = get_SMTCode(mpnf['mdg'], mpnf['mp-prop-pair'], opts)

    if opts.showprogress: print '---- solving SAT ----'
    show_progress3(mpnf_list)

    sat = 1
    for mpnf in mpnf_list:
        # SAT for Each MPNF
        for scc_acc in mpnf['Code/SCC']['AccSCCs']:
            # SAT for each SCC
            st = time.time()
            smt_result = execute_smt_solver(scc_acc['SMTCode'], opts)
            en = time.time()
            scc_acc['sat_time'] = en - st
            if smt_result['sat']:
                print "   SCC-SAT found"
                total_result['sat'] = True
                return process_result(mpnf_list, total_result)
            else:
                print '      SCC-partial UNSAT'
                sat = 0
        print '    SCC-total-UNSAT'
    if sat == 0:
        print '  Totally UNSAT'
        total_result['sat'] = False
        return process_result(mpnf_list, total_result)
        # do SAT-checking for Each SCC
    else:
        print 'ERROR?:  passed all SCC, maybe no BA/TGBA acceptable SCCs, or no SMT code'
        total_result['sat'] = False
        return process_result(mpnf_list, total_result)

def process_result(MPNF_List, total_result):
    return_result = {'time': [], 'sat': False}
    for mpnf in MPNF_List:
        # time
        # mpnf- 'graph-result' - 'time'
        return_result['time'].append(str(mpnf['graph_result']['time'])+'  --  Automata-Graph-Construction Time')
        return_result['time'].append(str(mpnf['graph_result']['nodes'])+'  --   Nodes')
        return_result['time'].append(str(mpnf['graph_result']['edges'])+'  --   Eedges')
        return_result['time'].append(str(mpnf['graph_result']['mdg_nodes'])+'  --   M-Nodes')
        return_result['time'].append(str(mpnf['graph_result']['mdg_edges'])+'  --   M-Eedges')
    return_result['time'].append(str(total_result['total_wg_time'])+'  --  Total Weighted-Graph-Construction Time')
    for mpnf in MPNF_List:
        # mpnf- 'Code/SCC' - 'AccSCCs' - 'sat-time'
        for accscc in mpnf['Code/SCC']['AccSCCs']:
            return_result['time'].append(str(accscc['gen_time'])+'  --  SMTCode-Generating Time/SCC')
            return_result['time'].append(str(accscc['sat_time'])+'  --  SAT Time')
            return_result['time'].append(str(accscc['nodes'])+'  --  AccSCC Nodes')
            return_result['time'].append(str(accscc['edges'])+'  --  AccSCC Edges')
    if total_result['sat']:
        return_result['sat'] = True
    return return_result

def print_result(reslist):
    print ' '
    print '  --------- result --------- ',
    if reslist['sat']:
        print 'SAT'
    else:
        print 'UNSAT'
    for t in reslist['time']:
        print t

def print_result_vs(reslist1, reslist2):
    print '  ---- result ---- ',
    if reslist['sat']:
        print 'SAT'
    else:
        print 'UNSAT'
    for i in range(max([len(reslist_ba['time']),len(reslist_tgba['time'])])):
        if reslist_ba['time'][i]:
            print '  ba:\t'+str(reslist_ba['time'][i])
        if reslist_tgba['time'][i]:
            print 'tgba:\t'+str(reslist_tgba['time'][i])
        print ''
    for t in reslist['time']:
        print t
    for resattr in reslist['graphs']:
        print ' Graph Nodes: '+str(resattr['nodes'])
        print ' Graph Edges: '+str(resattr['edges'])
        print ' WeightedGraph Nodes: '+str(resattr['mnodes'])
        print ' WeightedGraph Edges: '+str(resattr['medges'])
        for i in range(len(resattr['scclist']['nodes'])):
            print '  SCC Nodes: '+str(resattr['scclist']['nodes'][i])
            print '  SCC Edges: '+str(resattr['scclist']['edges'][i])



if __name__ == '__main__':
    optparser = optparse.OptionParser()
    optparser.add_option("-f", "--formula", dest='formula', default='GFa&MP^(T(a))<=0')
    optparser.add_option("-t", "--tgba", action="store_true", dest='tgba', default=False)
    optparser.add_option("-l", "--ltltrans", action="store_true", dest='ltltrans', default=False)
    optparser.add_option("-d", "--debug", action="store_true", dest='debug', default=False)
    optparser.add_option("-p", "--pdebug", action="store_true", dest='pdebug', default=False)
    optparser.add_option("-a", "--allsat", action="store_true", dest='allsat', default=False)
    optparser.add_option("-v", "--versus", action="store_true", dest='versus', default=False)
    optparser.add_option("-s", "--showprogress", action="store_true", dest='showprogress', default=False)
    optparser.add_option("-r", "--reverse", action="store_true", dest='reverse', default=False)
    optparser.add_option("-c", "--testcase", dest='testcase', default=None)
    opts, args = optparser.parse_args(sys.argv[1:])
    if opts.testcase:
        testinput = open(opts.testcase, 'r')
        line = testinput.readline()
        rcount = 1
        for line in testinput:
            # TODO line
            if '#' in line:
                pass
            elif 'EOF' in line:
                print 'EOF...'
                pass
            else:
                if not opts.versus:
                    print '   ---------- test case '+str(rcount)+' ----------'
                    formula = line.strip('\n')
                    reslist = satmain(formula, opts)
                    print_result(reslist)
                    print ''
                    rcount +=1
                else:
                    print '   ---------- BA vs TGBA Round '+str(rcount)+'----------'
                    formula = line.strip('\n')
                    opts.tgba = False
                    reslist_ba = satmain(formula, opts)
                    opts.tgba = True
                    reslist_tgba = satmain(formula, opts)
                    print_result_vs(reslist_ba,reslist_tgba)
                    rcount += 1
                    print ''
        testinput.close()
    else:
        if opts.versus:
            print '   ---------- BA vs TGBA  ----------'
            opts.tgba = False
            reslist_ba = satmain(opts.formula, opts)
            opts.tgba = True
            reslist_tgba = satmain(opts.formula, opts)
            print_result_vs(reslist_ba,reslist_tgba)
        else:
            '''
            reslist = satmain2(opts.formula, opts)
            print_result(reslist)
            '''
            sat = satmain2(opts.formula, opts)
            print sat
    sys.exit()
