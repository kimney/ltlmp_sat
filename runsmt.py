import networkx as nx
import copy
import time
def gen_smtcodelist_time(graph, mp_prop, opts):
    ExistentialMPList = []
    UniversalMPList = []
    gentime = time.time()
    for mpp in mp_prop:
        mp = mpp['mp']
        if (mp.ineq=='>=' or mp.ineq=='>')and(mp.data=='MP^'):
            if opts.debug:
                print '  existential mp'
            ExistentialMPList.append(mp)
        elif (mp.ineq=='<=' or mp.ineq=='<')and(mp.data=='MP_'):
            if opts.debug:
                print '  existential mp'
            ExistentialMPList.append(mp)
        else:
            if opts.debug:
                print '  universal mp'
            UniversalMPList.append(mp)
    retcodelist = []
    if ExistentialMPList ==[]:
        if opts.debug:
            print ' all Universal'
        retcodelist.append(generate_code(graph, UniversalMPList))
    elif UniversalMPList == []:
        if opts.debug:
            print ' all Existential'
        for e in ExistentialMPList:
            retcodelist.append(generate_code(graph, [e]))
    else:
        for existmp in ExistentialMPList:
            mplist = copy.deepcopy(UniversalMPList)
            mplist.append(existmp)
            retcodelist.append(generate_code(graph, mplist))
            ' SMT ---- generating Code time'
    return {'code':retcodelist, 'time':time.time()-gentime}

def generate_code(graph, MPList):
    newgraph = nx.MultiDiGraph()
    idx_tr = 1
    result_list = {'time':[]}
    st = time.time()
    for edge in graph.edges(data=True):
        newgraph.add_edge(edge[0],edge[1],name='x_'+str(idx_tr)+'_',weight= edge[2]['weight'])
        newgraph.add_node(edge[0],inList=[],outList=[])
        newgraph.add_node(edge[1],inList=[],outList=[])
        idx_tr += 1
    en = time.time()
    result_list['time'].append(str(en-st)+' SMT ---- making new graph -- add new node to newgraph, edge naming')
    st = time.time()
    for edge in newgraph.edges(data=True):
        newgraph.node[edge[1]]['inList'].append(edge[2]['name'])
        newgraph.node[edge[0]]['outList'].append(edge[2]['name'])
        # tooslow method-----> nx.get_node_attributes(newgraph, 'outList')[edge[0]].append(edge[2]['name'])
    # print '   transitions in SCC: ', str(idx_tr-1)
    en = time.time()
    result_list['time'].append(str(en-st)+' SMT ---- making new graph -- add edge to inList, outList')
    st = time.time()
    for node in newgraph.nodes(data=True):
        node[1]['outList'] = list(set(node[1]['outList']))
        node[1]['inList'] = list(set(node[1]['inList']))
    en = time.time()
    result_list['time'].append(str(en-st)+' SMT ---- making new graph -- list-set reducing')
    
    # (define x_1_1::nat)
    # (define x_1_2::nat)
    # (define x_1_3::nat)
    # (define x_2_1::nat)
    # (define x_2_2::nat)
    # (define x_2_3::nat)
    # ;; same count for each transition indices 
    # ;; (assert (and (= x_i_1 x_i_2) ... (= x_i_1 x_i_d)))
    # (assert (and (= x_1_1 x_1_2) (= x_1_1 x_1_3)))
    # (assert (and (= x_2_1 x_2_2) (= x_2_1 x_2_3)))
    returnlist = []
    returnlist.append('(reset)')
    st = time.time()
    for edge in newgraph.edges(data=True):
        idx_mp = 1
        eqmp = '(assert (and'
        for w8 in edge[2]['weight']:
            defnat = '(define '+edge[2]['name']+str(idx_mp)+'::nat)'
            returnlist.append(defnat)
            eqmp += ' (= '+edge[2]['name']+'1 '+edge[2]['name']+str(idx_mp)+')'
            idx_mp += 1
        eqmp += '))'
        returnlist.append(eqmp)
    en = time.time()
    result_list['time'].append(str(en-st)+' SMT ---- generating code -- mp')
    # ;; Exist of Transition
    # (assert (>= (+ x_1_1 ... x_n_1) 1))
    extr = '(assert (>= (+'
    for edge in newgraph.edges(data=True):
        extr += ' '+edge[2]['name']+str(1)
    extr += ') 1))'
    returnlist.append(extr)
    
    # ;; ?Exist of Init Transition
    # ;; (assert (or (>= x_(init_1)_1 1) ... (>= x_(init_i)_1 1))
    # (assert (>= x_1_1 1))
    
    # ;; Cyclic Transiton
    # ;; (same in-out count for each State)
    # ;; (assert (= (+ x_(in_1) ... x_(in_i)) (+ x_(out_1) ... x_(out_j)))
    # (assert (= (+ x_1_1 0) (+ x_2_1 0)))
    st = time.time()
    for node in newgraph.nodes(data=True):
        eccy = '(assert (= (+ '
        for name in node[1]['inList']:
            eccy +=  name+'1 '
        eccy += ') (+ '
        for name in node[1]['outList']:
            eccy += name+'1 '
        eccy += ')))'
        returnlist.append(eccy)
    en = time.time()
    result_list['time'].append(str(en-st)+' SMT ---- generating code -- in-out same count')

    # ;; MP weight constraints
    # ;; weight calucurated
    # ;; SUM_(i)[x_i_d * weight_i_d] >= 0
    # (assert (>= (+ (* x_1_1 1) (* x_2_1 -1)) 0))
    # (assert (>= (+ (* x_1_2 1) (* x_2_2 0)) 0))
    # (assert (>= (+ (* x_1_3 -1) (* x_2_3 1)) 0))
    # (- (mp.ineq (- (- edge[0].name edge[k].w8) (- edge[n].name edge[k].w8) 0)))
    mpcount = 0
    for mp in MPList:
        exmp = '(assert ('+mp.ineq+' (+ '
        for edge in newgraph.edges(data=True):
            exmp += '(* '+edge[2]['name']+str(mpcount+1)+' '+str(edge[2]['weight'][mpcount])+') '
        exmp += ') '+str(0)+'))'
        mpcount += 1
        returnlist.append(exmp)
    # ;; check check
    returnlist.append('(check)')
    # returnlist.append('(dump-context)')
    return returnlist
