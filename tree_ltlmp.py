import copy
import re
class tree:
    def __init__ (self, x):
        self.data = x
        self.child = [] # children class must be tree[this]
        self.attr = [] # for MP constraint and search label
        # MP condition
        self.ineq = '' # <= ...
        self.const = '' # 0 1 ...

    def set_attr(self, attr):
        self.attr.append(attr)
        
    def find_attr(self, key):
        for sa in self.attr:
            if sa == key:
                return True
        return False
    
    def find_node(self, key): # DFS
        if self.data == key:
            return True #node found
        elif self.child == []:
            return False
        else:
            for c in self.child:
                if c.find_node(key):
                    return True
        return False #if no node
    
    def get_tree(self, key): # DFS
        if self.data == key:
            return self #node found
        elif self.child == []:
            return False
        else:
            for c in self.child:
                a = c.get_tree(key)
                if a:
                    return a
            return False
        return False
    
    def get_tree_deepest(self,tree,key):
        # input: tree key
        # output: tree if found
        #            False  if Fail to search
        temp = tree.get_tree(key)
        if temp:
            while True:
                old = temp
                for cld in temp.child:
                    a = cld.get_tree(key)
                    if a:
                        temp = a
                        break
                if temp == old:
                    break
        return temp
    
    def remove_child(self):
        self.child= []

    def reverse_MP(self):
        # MP ineq in attr[0] = '<', attr[1] = 0(constant)
        # INEQ-op MUST be in attr[0]
        if (self.data == 'MP^') or (self.data == 'MP_'): #IDK If this syntacxis proper
            if self.ineq == '<=':
                self.ineq = '>'
            elif self.ineq == '<':
                self.ineq = '>='
            elif self.ineq == '>=':
                self.ineq = '<'
            elif self.ineq == '>':
                self.ineq= '<='
            else:
                pass
    

    # process all MP terms into U-indipendent term
    # MP( 3_(a AND b U c ) - 2_(true) + MP(a)<=0 + MP(a U b)<=0  ) <= 0
    #
    #  1. replace all-UntilTerm to Prop and  (Prop<->UntilTerm),
    #     MP(... t_(~  bUc ) ...) <= 0 
    #  to MP(... t_(~ p[bUc]) ...) <= 0  &  p <-> bUc
    #       ( aUbUcU... is replaced by p[aUbUcU...] )
    # 
    #  2. replace MP-nest --- PHI(MP)  to  (PHI(MP/True) & MP) | (PHI(MP/False) & !MP)
    #        PSY U MP(t_(MP(...) ...)<=0 ...) <=0 
    #   to (PSY U True & MP(...) <=0  |  PSY U False & MP(...)>0)
    #        MP(t_(MP(...) ...)<=0 ...) <=0
    #        MP(True ...)<=0 & MP(...)<=0  |  MP(False ...)<=0 & MP(...)>0
    #    so MP-replacement can be done by OuterTraversal? Process
    #
    #   InnerTraversal is also done and MORE EFFECTIVE
    #      because MP-nested Checking cost is  c*d     (innerTraversal)
    #                                                         c*2^d (outerTraversal)
    # 
    #  I DONT KNOW: whether 1. first is better or not
'---------- end class def -----'

def get_not_MPNF_MP_tree(tree):
    # input: tree (its root, in which u want to find notMPNF node)
    # output: tree (if the not'MPNF' MP-node)
    #            False (otherwise)
    'check whtr Input Node is not MPNF MP-node'
    if tree.data == 'MP^' or tree.data == 'MP_':
        if not tree.find_attr('MPNF'):
            return tree
    'check whtr Child is MPNF or not'        
    for cld in tree.child:
        a = get_not_MPNF_MP_tree(cld)
        if a:
            return a
    return False

def get_not_MPNF_MP_tree_deepest(root):
    # input: tree (its root, in which u want to find deepest notMPNF node)
    # output: tree (if deepest notMPNF node)
    #            False (if not found) 
    temp = get_not_MPNF_MP_tree(root)
    if temp:
        while True:
            old = temp
            for cld in temp.child:
                a = get_not_MPNF_MP_tree(cld)
                if a:
                    temp = a
                    break
            if temp == old:
                break
    return temp

def replaced_MP_tree_list(root, r_mp):
    # input: tree (its root)
    #          MP-node(will be replaced by T/F)
    # output: list (OR (AND LTL-MP) (AND LTL-MP)) 
    mp1 = copy.deepcopy(r_mp)
    mp1.set_attr('MPNF')
    mp2 = copy.deepcopy(r_mp)
    mp2.reverse_MP()
    mp2.set_attr('MPNF')
    # Make True/False Subtree
    r_mp.remove_child()
    r_mp.data = 'true'
    ltl1 = copy.deepcopy(root)
    r_mp.data = 'false'
    ltl2 = copy.deepcopy(root)
    return [[ltl1,[mp1]], [ltl2,[mp2]]]
    
def get_MPNF_list(root):
    # input: tree(its root)
    # output: OR-List( AND-Pair(LTL, Simple-MP) )
    #            False if fail to create
    
    newroot = root
    pairList = []
    # : pairList = {(LTL, MP-List)}
    # semantics: LTL and MP in MP-List are connected by AND (i.e. MPNF)
    r_mp = False

    # Firstly, convert root to MPNF
    if root.find_node('MP^'):
        r_mp = root.get_tree_deepest(root, 'MP^')
    elif root.find_node('MP_'):
        r_mp = root.get_tree_deepest(root, 'MP_')
    if r_mp:
        a = replaced_MP_tree_list(root, r_mp)
        pairList = a
    else:
        print 'Error (MP_nest_proto): MP not found'
        return False #Escape

    # Secondery, find and convert to MPNF for Children
    while True:
        old = copy.copy(pairList) # infinit Loop if deepcopy
        for pair in pairList:
            ltl_chk = pair[0] # pair[0] is LTL(may contain MP)
            replace = get_not_MPNF_MP_tree_deepest(ltl_chk)
            if replace:
                # refresh pairList if no-MPNF found
                a = replaced_MP_tree_list(ltl_chk, replace)
                pairList.remove(pair)
                # extending List
                mp = pair[1] # pair[1] is MP-List (Type: list(tree)  #not tree)
                a[0][1].extend(copy.deepcopy(mp))
                a[1][1].extend(copy.deepcopy(mp))
                pairList.extend(a)
                break
        if pairList == old:
            break
    for mpnf_pair in pairList:
        replace_timed_MP(mpnf_pair)
    return pairList

def allprint(tree):
    print tree.data
    for c in tree.child:
        allprint(c)

# TODO: test this method
def replace_timed_MP(mpnf_pair):
    # input: a mpnf_list (possively MP term has Timed LTL.)
    # output: a mpnf_list (MP has only not Timed LTL)
    # this method rewriting input by append-remove list
    for mp in mpnf_pair[1]:
        #print ' --- while loop -----'
        while True:
            # get Timed LTL tree in simplified MP tree
            timed = mpnf_pair[1][0].get_tree_deepest(mp,'U')
            if not timed:
                timed = mp.get_tree('G')
                if not timed:
                    timed = mp.get_tree('F')
                    if not timed:
                        timed = mp.get_tree('X')
            if timed:
                p = get_new_prop()
                # create (timed-sentence <-> new-prop)
                eq = tree('EQ')
                eql = tree(p)
                eqr = copy.deepcopy(timed)
                eq.child.append(eql)
                eq.child.append(eqr)
                # replace timed-node in MP to prop-node
                newmp = mp
                mpnf_pair[1].remove(mp)
                timed.remove_child()
                timed.data = p
                mpnf_pair[1].append(newmp)
                # idk y this implement fails
                #  timed = tree(p)
                # create and update LTL
                oldLTL = copy.deepcopy(mpnf_pair[0])
                newLTL = tree('AND')
                newLTL.child.append(oldLTL)
                newLTL.child.append(eq)
                mpnf_pair.pop(0)
                mpnf_pair.insert(0, newLTL)
            else:
                break
    reset_count()

count = 0
def reset_count():
    global count
    count = 0
def get_new_prop():
    # output: prop neverused in current LTL
    global count
    count = count+1
    return 'np'+repr(count)

'----- expression ----- '
def all_term_in_mp_to_simple(inputmp):
    # input: expr(tree)
    # output: expr(tree) with only Props and 0-1s
    mp = copy.deepcopy(inputmp)
    while True:
        a = mp.get_tree('TERM')
        if a:
            acld = a.child[0]
            a.data = acld.data
            for cld in acld.child:
                a.child.append(cld)
            a.child.remove(acld)
            while True:
                tt = a.get_tree('true')
                if tt:
                    tt.data = '1'
                else:
                    break
            while True:
                tt = a.get_tree('false')
                if tt:
                    tt.data = '0'
                else:
                    break
            while True:
                nt = a.get_tree('NOT')
                if nt:
                    nt.data = '-'
                    nt0 = nt.child[0]
                    nt.remove_child()
                    nt.child.append(tree('1'))
                    nt.child.append(nt0)
                else:
                    break
            while True:
                at = a.get_tree('AND')
                if at:
                    at.data = '*'
                else:
                    break
            while True:
                ot = a.get_tree('OR')
                if ot:
                    # OR -> a + b - a*b
                    ot.data = '+'
                    ot0 = ot.child[0]
                    ot1 = ot.child[1]
                    ot.remove_child()
                    ot.child.append(ot0)
                    t2 = tree('-')
                    t2.child.append(ot1)
                    t3 = tree('*')
                    t3.child.append(copy.deepcopy(ot0))
                    t3.child.append(copy.deepcopy(ot1))
                    t2.child.append(t3)
                    ot.child.append(t2)
                else:
                    break
        else:
            break
    return mp

def decide_cond_pos(mp, a):
    # slow implement
    # DESTRUCTIVE for mp
    while True:
        node = mp.get_tree(a)
        if node:
            node.data = '1'
        else:
            break

def decide_cond_neg(mp, a):
    while True:
        node = mp.get_tree(a)
        if node:
            node.data = '0'
        else:
            break


def get_proplist(mptree):
    proplist = []
    get_all_leaf(mptree, proplist)
    proplist = list(set(proplist))
    proplist = [x for x in proplist if not re.match('\d+|true|false', x)]
    return proplist
                
def get_all_leaf(in_tree, leaf_list):
    for cld in in_tree.child:
        get_all_leaf(cld, leaf_list)
    if in_tree.child == []:
        leaf_list.append(in_tree.data)
                

def get_weighted(preweightmp_list, proplist):
    pl = copy.deepcopy(proplist)
    if proplist == []:
        print '---- NonProp error ---- return False'
        return False
    pwl = [preweightmp_list]
    while not pl == []:
        newlist = []
        prop = pl.pop()
        for mp in pwl:
            mp0 = copy.deepcopy(mp)
            mp1 = copy.deepcopy(mp)
            while True:
                a = mp0.get_tree(prop)
                if a:
                    a.data = '0'
                else:
                    break
            while True:
                a = mp1.get_tree(prop)
                if a:
                    a.data = '1'
                else:
                    break
            newlist.append(mp0)
            newlist.append(mp1)
        pwl = newlist
    return pwl


def get_weighted2(preweightmp, propset):
    pl = list(propset)
    if pl == []:
        print '---- NonProp error ---- return False'
        return False
    rooplist = [preweightmp]
    while not pl == []:
        newlist = []
        prop = pl.pop()
        for pwmp in rooplist:
            mp0 = copy.deepcopy(pwmp)
            mp1 = copy.deepcopy(pwmp)
            while True:
                br = 0
                for mp in mp0:
                    a = mp.get_tree(prop)
                    if a:
                        br = 1
                        a.data = '0'
                if br ==0:
                    break
            while True:
                br = 0
                for mp in mp1:
                    a = mp.get_tree(prop)
                    if a:
                        br = 1
                        a.data = '1'
                if br ==0:
                    break
            newlist.append(mp0)
            newlist.append(mp1)
        rooplist = newlist
    return rooplist

def get_weighted_uhlan(input_mps, props):
    udps = list(props)
    mps_loop = [input_mps]    
    while not udps == []:
        newlist = []
        prop = udps.pop()
        for mps in mps_loop:
            newlist.extend(mp__(mps, prop))
        mps_loop = newlist
    return mps_loop

def mp__(mps, prop):
    mps0 = copy.deepcopy(mps)
    mps1 = copy.deepcopy(mps)
    for mp in mps0:
        while True:
            a = mp.get_tree(str(prop))
            if a:
                a.data = '0'
            else:
                break
    for mp in mps1:
        while True:
            a = mp.get_tree(prop)
            if a:
                a.data = '1'
            else:
                break
    return [mps0, mps1]
