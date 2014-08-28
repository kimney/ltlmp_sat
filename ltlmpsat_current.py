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

from tree_ltlmp import tree
import tree_ltlmp as tltl
import generategraph as gg
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
                exec "w = "+ (tmtc.mp_out(mp.child[0]))
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
                mdg.add_edge(edge[0],edge[1],weight=w8,acc=edge[2]['acc'])
        else:
            for w8 in w8list:
                mdg.add_edge(edge[0],edge[1],weight=w8)
        if opts.pdebug:
            for w8 in w8list:
                print '    '+str(edge[0])+' --> '+str(edge[1])+'  w8: '+str(w8)
    return mdg


def get_SMTCode(mdg, mp_prop, opts):
    # input mdg
    # output SMTCode list, result per 
    results = {'SCCs':[], 'AccSCCs':[]}
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

def do_sat(codes_ext, opts):
    result_list = {'time':'a'}
    cmd_smt = './yices yicesinput'
    unsat_scc = 0
    
    st = time.time()
    for codes in codes_ext:
        if opts.showprogress:
            print '     ---- solving Constraints ---- '
        yinput = open('yicesinput', 'w')
        for code in codes:
            if opts.pdebug:
                print code
            yinput.write(str(code)+'\n')
        yinput.close()
        smt_solver = subprocess.Popen(cmd_smt,shell=True,close_fds=True,stdout=subprocess.PIPE)
        
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



def graph_tgba(pair, opts):
    # input: TGBA
    # output: results{'graph', ''}
    #     
    results = {'mp-prop-pair':[]}
    # temp
    ltl = pair[0]
    mplist = pair[1]
    cmd_ltl2tgba = 'ltl2tgba -f ' + '\'' +tmtc.ltl_out(ltl)+ '\''
    st = time.time()
    constime = time.time()
    ltl2tgba = subprocess.Popen(cmd_ltl2tgba,shell=True,close_fds=True,stdout=subprocess.PIPE)
    out = ltl2tgba.stdout
    graph = gg.tgba2graph(out, constime,opts)
    if graph:
        props = []
        for mp in mplist:
            results['mp-prop-pair'].append({'mp':tltl.all_term_in_mp_to_simple(mp), 'prop':tltl.get_proplist(mp)})
        results['graph'] = graph
        # results['mplist'] = copy.deepcopy(mplist)
        # results['mpprops'] = props
        if opts.pdebug:
            print "    props:",props
        en = time.time()
        tctime = str(en-st)+'  -- ltl2tgba -> Graph  Conversion Time '
        print tctime
        results['time'] = tctime
        return results
    else:
        return False

def graph_ltltrans(pair, opts):
    # input: TGBA
    # output: results{'graph', ''}
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
            results['mp-prop-pair'].append({'mp':tltl.all_term_in_mp_to_simple(mp), 'prop':tltl.get_proplist(mp)})
        results['graph'] = graph
        # results['mplist'] = copy.deepcopy(mplist)
        # results['mpprops'] = props
        if opts.pdebug:
            print "    props:",props
        en = time.time()
        tctime = str(en-st)+'  -- ltl2tgba -> Graph  Conversion Time '
        print tctime
        results['time'] = tctime
        return results
    else:
        return False
        
def graph_ba(pair, opts):
    # input: TGBA
    # output: results{'graph', ''}
    #     
    results = {'mp-prop-pair':[]}
    # temp
    ltl = pair[0]
    mplist = pair[1]
    cmd_ltl3ba = './translator/ltl3ba -f ' + '\'' +tmtc.ltl_out(ltl)+ '\''
    st = time.time()
    ltl3ba = subprocess.Popen(cmd_ltl3ba,shell=True,close_fds=True,stdout=subprocess.PIPE)
    out = ltl3ba.stdout
    graph = gg.nvc2graph(out, st, opts)
    if graph:
        props = []
        for mp in mplist:
            results['mp-prop-pair'].append({'mp':tltl.all_term_in_mp_to_simple(mp), 'prop':tltl.get_proplist(mp)})
        results['graph'] = graph
        # results['mplist'] = copy.deepcopy(mplist)
        # results['mpprops'] = props
        if opts.pdebug:
            print "    props:",props
        en = time.time()
        tctime = str(en-st)+'  -- ltl3ba -> Graph  Total Construction Time '
        print tctime
        results['time'] = tctime
        return results
    else:
        return False


def satmain(ltlmp_formula, opts):
    total_result = {'sat':False, 'time':[], 'graphs':[], 'total_wg_time':0.0 }
    print "----- Parsing ", repr(ltlmp_formula), '-----'
    char_stream = antlr3.ANTLRStringStream(ltlmp_formula)
    lexer = LTLMPLexer(char_stream)
    tokens = antlr3.CommonTokenStream(lexer)
    parser = LTLMPParser(tokens)
    r = parser.start()
    ast_root = r.tree # root of the AST(Type: CommonTree(antlr))
    if opts.showprogress:
        print "----- Parsing Done -----"

    nodes = antlr3.tree.CommonTreeNodeStream(ast_root)
    nodes.setTokenStream(tokens)
    evaltree = LTLMPTree(nodes)
    if opts.debug:
        print "----- Tree Parsing -----"
    ltlmp_root = evaltree.expr()
    if opts.showprogress:
        print "----- Tree Parsing Done -----"
        print '----- AST Parse Result -----'
        print tmtc.ltl_out(ltlmp_root)
        print '----- End AST Parse Reslt-----'
        print '----- LTLMP to Nomal Form List -----'
    # from tree_ltl
    # the pairs of (ltlmp-NF, )
    pairList = tltl.get_MPNF_list(ltlmp_root)
    
    if opts.debug:
        print '----- Printing MP-NF Result -----'
        for pair in pairList:
            print '  --',tmtc.ltl_out(pair[0]),'--'
            for mp in pair[1]:
                print '   ',tmtc.mp_out(mp)
            
    # improve LTL tree
    # TODO: this is future work

    # LTL2BA: LTL to never-claim(nvc)
    # LTL2TGBA: LTL to Transition-based Generalized BA
    # LTLTrans: 
    MPNF_List = []   # MP Normal Form  Sentence? list
    GraphList = []   # 
    MPList = []      # MP-Constraints List according to Graph
    MPPropsList = [] # Props(var) used in MP-Constraints according to Graph
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
    if opts.showprogress:
        print '---- Weighted Graph generating ----'

    wg_st = time.time()

     
    print '  -------- temporal result ---------'
    for mpnf in MPNF_List:
        res_graph = {'nodes':0, 'edges':0, 'scclist':{'nodes':[], 'edges':[]} }
        res_graph['edges'] = nx.number_of_edges(mpnf['graph'])
        res_graph['nodes'] = nx.number_of_nodes(mpnf['graph'])
        print str(res_graph['nodes'])+'  --   Nodes'
        print str(res_graph['edges'])+'  --   Edges'
        st_gtime = time.time()
        mpnf['mdg'] = get_weighted_graph(mpnf['graph'], mpnf['mp-prop-pair'], opts)
        # print mpnf['mdg']
        en_gtime = time.time()
        res_graph['mnodes'] = nx.number_of_nodes(mpnf['mdg'])
        res_graph['medges'] = nx.number_of_edges(mpnf['mdg'])
        res_graph['time'] = str(en_gtime-st_gtime)+ ' -- Weighted Graph Generating Time: '
        mpnf['graph_result'] = res_graph
        print str(en_gtime-st_gtime)+ ' -- Weighted Graph Generating Time: '
        
    if opts.showprogress:
        print '----- end weighted Graph ----'
        
    wg_en = time.time()
    total_result['total_wg_time'] = wg_en - wg_st
    '  -- Total Weighted Graph Generating Time:  '
    print str(wg_en - wg_st) + '  -- Total Weighted Graph Generating Time:  '
    print '  -------- temporal result ---------'
    for mpnf in MPNF_List:
        print str(mpnf['graph_result']['mnodes'])+'  --   Nodes'
        print str(mpnf['graph_result']['medges'])+'  --   Edges'

    """
    if opts.pdebug:
        print ' pdebug: ---- Generated MultiDiGraph ----'
        if opts.tgba:
            print ' TGBA Acc Cond: ',MDGraphList[i].graph['acccond']
        for i in range(len(MDGraphList)):
            edges = MDGraphList[i].edges(data=True)
            for edge in edges:
                print '    [',
                print edge[0]+'  --->  '+edge[1] + '\tWeight: ', edge[2]['weight'],
                if opts.tgba:
                    print '\t',edge[2]['acc'],
                print ' ]'
                """
                
    if opts.showprogress:
        print '---- SMT input generating ----'

    # for SCC which includes 'accept' state'
    #     do SAT 
    # convert Weighted Graph to SMT-Solver Sentence
    SMTCodesExtList = []
    for mpnf in MPNF_List:
        mpnf['Code/SCC'] = get_SMTCode(mpnf['mdg'], mpnf['mp-prop-pair'], opts)
        
    if opts.showprogress:
        print '---- solving SAT ----'

    # temp
    print '  -------- temporal result ---------'
    for mpnf in MPNF_List:
        # mpnf- 'Code/SCC' - 'AccSCCs' - 'sat-time'
        for accscc in mpnf['Code/SCC']['AccSCCs']:
            print str(accscc['nodes'])+'  --  AccSCC Nodes'
            print str(accscc['edges'])+'  --  AccSCC Edges'
        print str(mpnf['graph_result']['nodes'])+'  --   Nodes'
        print str(mpnf['graph_result']['edges'])+'  --   Edges'
        
    unsat = 0
    for mpnf in MPNF_List:
        # SAT for Each MPNF
        for accscc in mpnf['Code/SCC']['AccSCCs']:
            # SAT for each SCC
            st = time.time()
            smt_result = do_sat(accscc['SMTCode'], opts)
            en = time.time()
            accscc['sat_time'] = en - st
            if smt_result['sat']:
                print "   SCC-SAT found"
                total_result['sat']=True
                return process_result(MPNF_List, total_result)
            else:
                print '      SCC-partial UNSAT'
                unsat = 1
        print '    SCC-total-UNSAT'
    if unsat ==1:
        print '  Totally UNSAT'
        total_result['sat'] = False
        return process_result(MPNF_List, total_result)
        # do SAT-checking for Each SCC
    else:
        print '  all through UNSAT, no BA/TGBA-acceptable SCC, noSMTcode'
        total_result['sat'] = False
        return process_result(MPNF_List, total_result)

def process_result(MPNF_List, total_result):
    return_result = {'time':[], 'sat':False, 'aaa':[]}
    for mpnf in MPNF_List:
        # time
        # mpnf- 'graph-result' - 'time'
        return_result['time'].append(str(mpnf['graph_result']['time'])+'  --  Automata-Graph-Construction Time')
        return_result['time'].append(str(mpnf['graph_result']['nodes'])+'  --   Nodes')
        return_result['time'].append(str(mpnf['graph_result']['edges'])+'  --   Eedges')
        return_result['time'].append(str(mpnf['graph_result']['mnodes'])+'  --   M-Nodes')
        return_result['time'].append(str(mpnf['graph_result']['medges'])+'  --   M-Eedges')
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
            
def print_result_vs(reslist1,reslist2):
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
    optparser.add_option("-f", "--formula", dest='formula', default='GFa&MP_(T(a))<=0')
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
            reslist = satmain(opts.formula, opts)
            print_result(reslist)
    sys.exit()
