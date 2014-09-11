import sys
import networkx as nx
import re
import time
## interpret SPIN neverclaim input
def tgba2graph(tgba_input, starttime, opts):
    # input: <spot's tgba>
    # output: <Graph> / False
    # assumption: cond-format is DNF
    acclist_all = []
    graph = nx.MultiDiGraph(acccond=acclist_all)
    ss = re.compile('\W+')
    for line in tgba_input:
        # print line,
        condList = []
        accList = []
        # print 'line: ',line,
        if 'digraph G {' in line:
            print str(time.time()-starttime)+'  ---- Automata construction Time '
            st = time.time()
        elif ' -> ' in line:
            tr = ss.split(line,3)
            state = tr[1]
            dest = tr[2]
            labels = tr[3].rstrip(']\n').lstrip('label=').strip('"').split('\\n')
            if len(labels) ==1:
                pass
            else:
                condList = []
                
                for conds in labels[0].split(' | '):
                    neglist=[]
                    poslist=[]
                    b = set(conds.split(' '))
                    if '&' in b: b.remove('&')
                    if '1' in b: b.remove('1')
                    b = list(b)
                    for p in b:
                        if '!' in p:
                            neglist.append(p)
                        else:
                            poslist.append(p)
                    condList.append([poslist, neglist])
                    
                if labels[1] == '':
                    accept_Fs = []
                else:
                    accept_Fs = labels[1].strip('{}"').split(', ')
                    acclist_all.append(list(set(accept_Fs)))
                    # print 'aaccFs: ',list(set(accept_Fs))
                    
                graph.add_node(state)
                graph.add_node(dest)
                graph.add_edge(state,dest,condList=condList,acc=accept_Fs)
    if graph.edges() == []:
        if opts.debug:
            print 'No Graph Generated'
        return False
    # print 'edges:       '
    # print str(edges)
    # print 'graph.edges: '
    # print str(graph.edges(data=True))
    graph.graph['acccond'] = acclist_all
    if opts.pdebug:
        print '    accept condlist: ', str(graph.graph['acccond'])
    en = time.time()
    print '  -- DiGraph Construction Time:  ' + str(en-st)
    return graph

def nvc2graph(nvc_input, starttime, opts):
    # input: neverclaim
    # output: Graph
    #            False
    # assumption: cond-format is DNF
    graph = nx.DiGraph()
    # DiGraph is enough because it is guaranteed that there is only one transition for each state-pair in neverclaim
    edges = []
    trans = 0
    retrans = re.compile(' -> ')
    reor = re.compile('\|\|')
    for line in nvc_input:
        # print line,
        trans = 0
        condList = []
        tr= ''
        if 'never {' in line:
            print str(time.time()-starttime)+'  ---- Automata construction Time '
            st = time.time()
        elif ':\n' in line:
            state = line.strip(':\n')
        elif 'false' in line:
            return False
        elif ' -> ' in line:
            trans = 1
            tr = retrans.split(line)
            condinput = tr[0].strip(':\n\t ;')
            ors = reor.split(condinput)
            for o in ors:
                neglist=[]
                poslist=[]
                a = o.strip('() ')
                b = set(a.split(' '))
                if '&' in b: b.remove('&')
                if '1' in b: b.remove('1')
                b = list(b)
                for p in b:
                    if '!' in p:
                        neglist.append(p)
                    else:
                        poslist.append(p)
                condList.append([poslist, neglist])
            dest = tr[1].strip(':\n\t ').split(' ')[1]
            graph.add_node(state)
            graph.add_node(dest)
            graph.add_edge(state, dest, condList=condList)
        elif 'skip' in line:
            trans = 1
            condList = []
            dest = state
            graph.add_node(state)
            graph.add_node(dest)
            graph.add_edge(state, dest, condList=condList)
    if graph.edges() == []:
        if opts.debug:
            print 'No Graph Generated'
        return False
    en = time.time()
    if opts.debug:
        print '  -- DiGraph Construction Time:  '+ str(en-st)
    return graph

def ltltrans2graph(nvc_input, starttime, opts):
    # input: neverclaim(ltltrans)
    # output: Graph
    #            False
    # assumption: cond-format is DNF
    graph = nx.DiGraph()
    # DiGraph is enough because it is guaranteed that there is only one transition for each state-pair in neverclaim
    edges = []
    trans = 0
    retrans = re.compile(' -> ')
    reor = re.compile('\|\|')
    for line in nvc_input:
        # print line,
        trans = 0
        condList = []
        tr= ''
        if 'never {' in line:
            print str(time.time()-starttime)+'  ---- Automata construction Time '
            st = time.time()
        elif ':\n' in line:
            state = line.strip(':\n\t')
        elif 'false' in line:
            return False
        elif ' -> ' in line:
            trans = 1
            tr = retrans.split(line)
            condinput = tr[0].strip(':\n\t ;')
            ors = reor.split(condinput)
            for o in ors:
                neglist=[]
                poslist=[]
                a = o.strip('() ')
                b = set(a.split(' '))
                while '&&' in b: b.remove('&&')
                while '1' in b: b.remove('1')
                b = list(b)
                for p in b:
                    if '!' in p:
                        neglist.append(p.strip('\t ()'))
                    else:
                        poslist.append(p)
                condList.append([poslist, neglist])
            dest = tr[1].strip(':\n\t ').split(' ')[1]
            graph.add_node(state)
            graph.add_node(dest)
            graph.add_edge(state, dest, condList=condList)
        elif 'skip' in line:
            trans = 1
            condList = []
            dest = state
            graph.add_node(state)
            graph.add_node(dest)
            graph.add_edge(state, dest, condList=condList)
    if graph.edges() == []:
        if opts.debug:
            print 'No Graph Generated'
        return False
    en = time.time()
    if opts.debug:
        print '  -- DiGraph Construction Time:  ' + str(en-st)
    return graph

"""
edges = []
f = open('input.txt')
for line in f:
    flag = 0
    if '->' in line:
        flag = 1
        temp = line.strip(':\n \t')
        templist = temp.split(' ')
        cond = templist[0].strip('()')
        dest = templist[3]
    if ':\n' in line:
        state = line.strip(':\n')
        print state
    if flag == 1:
        edges.append((state,dest,cond))
        print ('From: '+state,'To: '+dest, 'Cond: '+cond)
f.close()

print edges

if __name__ == '__main__':
    graph = nx.Graph()
    for (a,b,c) in edges:
        graph.add_node(a)
        graph.add_node(b)
        graph.add_edge(a,b,trainsitionLabel=c)
    SCC = nx.strongly_connected_component_subgraphs(graph)
    #nx.draw(graph)
    nx.draw(SCC[0])
    plt.show()

## draw by Graphviz
##dot = Dot.Dot(graph) 
##dot.display()
"""
