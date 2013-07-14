#DEFINE ltl3ba input style from AST

def ltl_out(tin):
    # INPUT: tree
    # returning
    #--templete--
    # elif tin.data == :
    #    return '('+ltl_out(tin.child[0])+')'
    # cf. LTLMPTree.g
    
    #print 'LTL_out: '+tin.data
    if tin.data == 'AND':
        return '('+ltl_out(tin.child[0])+' && '+ltl_out(tin.child[1])+')'
    elif tin.data == 'OR':
        return '('+ltl_out(tin.child[0])+' || '+ltl_out(tin.child[1])+')'
    elif tin.data == 'U':
        return '( '+ltl_out(tin.child[0])+' U '+ltl_out(tin.child[1])+' )'
    elif tin.data == 'V':
        return '( '+ltl_out(tin.child[0])+' V '+ltl_out(tin.child[1])+' )'
    elif tin.data == 'IMP':
        return '( '+ltl_out(tin.child[0])+' -> '+ltl_out(tin.child[1])+' )'
    elif tin.data == 'X':
        return ' X '+ltl_out(tin.child[0])
    elif tin.data == 'NOT':
        return ' ! '+ltl_out(tin.child[0])
    elif tin.data == 'F':
        return ' F '+ltl_out(tin.child[0])
    elif tin.data == 'EQ':
        return '('+ltl_out(tin.child[0])+'<->'+ltl_out(tin.child[1])+')'
    elif tin.data == 'G':
        return ' G '+ltl_out(tin.child[0])
    elif tin.data == 'True':
        return ' true '
    elif tin.data == 'False':
        return ' false '
    elif tin.data == 'MP^':
        return mp_out(tin)
    elif tin.data == 'MP_':
        return mp_out(tin)
    else:
        #print tin.data
        return tin.data

def mp_out(tin):
    #print 'mp_out: '+tin.data
    if tin.data == '*':
        return '('+mp_out(tin.child[0])+'*'+mp_out(tin.child[1])+')'
    elif tin.data == '-':
        return '('+mp_out(tin.child[0])+'-'+mp_out(tin.child[1])+')'
    elif tin.data == '+':
        return '('+mp_out(tin.child[0])+'+'+mp_out(tin.child[1])+')'
    elif tin.data == 'TERM':
        #print 'term'
        return 'T('+ltl_out(tin.child[0])+')'
    elif tin.data == ('AND' or 'OR' or 'U' or 'G' or 'F' or 'NOT' or 'X' or 'EQ'): #or 'OR' or 'U':  or something else ...
        return ltl_out(tin.child[0])+'-- MP Error --'#ltl_out(tin)
    elif tin.data == 'MP^':
        #print 'this is MP^'
        return tin.data +'('+mp_out(tin.child[0])+')'+tin.ineq+ tin.const
    elif tin.data == 'MP_':
        #print 'this is MP_'
        return tin.data +'('+mp_out(tin.child[0])+')'+tin.ineq+ tin.const
    else:
        #print '--mp error--' + tin.data
        return tin.data

    
def ltl_out_trans(tin):
    # INPUT: tree
    # returning
    #--templete--
    # elif tin.data == :
    #    return '('+ltl_out(tin.child[0])+')'
    # cf. LTLMPTree.g
    
    #print 'LTL_out: '+tin.data
    if tin.data == 'AND':
        return '('+ltl_out_trans(tin.child[0])+' && '+ltl_out_trans(tin.child[1])+')'
    elif tin.data == 'OR':
        return '('+ltl_out_trans(tin.child[0])+' || '+ltl_out_trans(tin.child[1])+')'
    elif tin.data == 'U':
        return '( '+ltl_out_trans(tin.child[0])+' U '+ltl_out_trans(tin.child[1])+' )'
    elif tin.data == 'V':
        return '( '+ltl_out_trans(tin.child[0])+' V '+ltl_out_trans(tin.child[1])+' )'
    elif tin.data == 'IMP':
        return '( '+ltl_out_trans(tin.child[0])+' -> '+ltl_out_trans(tin.child[1])+' )'
    elif tin.data == 'X':
        return ' X '+ltl_out_trans(tin.child[0])
    elif tin.data == 'NOT':
        return ' ! '+ltl_out_trans(tin.child[0])
    elif tin.data == 'F':
        return '(<> '+ltl_out_trans(tin.child[0])+' )'
    elif tin.data == 'EQ':
        return '( '+ltl_out_trans(tin.child[0])+' && '+ltl_out_trans(tin.child[1])+' ) || ( ! '+ltl_out_trans(tin.child[0])+' && ! '+ltl_out_trans(tin.child[1]) +' )'
    elif tin.data == 'G':
        return '([] '+ltl_out_trans(tin.child[0])+' )'
    elif tin.data == 'True':
        return ' true '
    elif tin.data == 'False':
        return ' false '
    else:
        #print tin.data
        return tin.data
