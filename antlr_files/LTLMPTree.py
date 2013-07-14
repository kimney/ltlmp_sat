# $ANTLR 3.5 /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g 2013-07-14 17:29:35

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset

        
from tree_ltlmp import tree as maketree



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__20=20
T__21=21
T__22=22
T__23=23
T__24=24
AND=4
DIGITS=5
FINAL=6
GLOBAL=7
IMP=8
INEQ=9
MP=10
NEWLINE=11
NEXT=12
NOT=13
OR=14
PROP=15
TERM=16
UNTIL=17
WS=18
WUNTIL=19

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "AND", "DIGITS", "FINAL", "GLOBAL", "IMP", "INEQ", "MP", "NEWLINE", 
    "NEXT", "NOT", "OR", "PROP", "TERM", "UNTIL", "WS", "WUNTIL", "'('", 
    "')'", "'*'", "'+'", "'-'"
]




class LTLMPTree(TreeParser):
    grammarFileName = "/Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(LTLMPTree, self).__init__(input, state, *args, **kwargs)



        self.memory = {}

        self.delegates = []






    # $ANTLR start "prog"
    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:14:1: prog : ( stat )+ ;
    def prog(self, ):
        try:
            try:
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:14:6: ( ( stat )+ )
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:15:2: ( stat )+
                pass 
                #action start
                print " ---- Tree parsing prog ----"
                #action end


                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:16:2: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((AND <= LA1_0 <= IMP) or LA1_0 == MP or (NEXT <= LA1_0 <= UNTIL) or LA1_0 == WUNTIL or (22 <= LA1_0 <= 24)) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:16:2: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_prog55)
                        self.stat()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                #action start
                print " ---- End Treeparsing ----"
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "prog"



    # $ANTLR start "stat"
    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:20:1: stat : expr ;
    def stat(self, ):
        try:
            try:
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:20:6: ( expr )
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:21:2: expr
                pass 
                self._state.following.append(self.FOLLOW_expr_in_stat72)
                self.expr()

                self._state.following.pop()

                #action start
                print 'EXPR!'
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "stat"



    # $ANTLR start "expr"
    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:25:1: expr returns [value] : ( ^( OR ax= expr bx= expr ) | ^( AND cx= expr dx= expr ) | ^( IMP cx= expr dx= expr ) | ^( NEXT x= expr ) | ^( UNTIL ax= expr bx= expr ) | ^( WUNTIL ax= expr bx= expr ) | ^( FINAL x= expr ) | ^( GLOBAL x= expr ) | ^( NOT x= expr ) | ^( MP mpineq ) | ^( TERM x= expr ) | ^( '*' ax= expr bx= expr ) | ^( '+' ax= expr bx= expr ) | ^( '-' ax= expr bx= expr ) | DIGITS | PROP );
    def expr(self, ):
        value = None


        MP1 = None
        DIGITS3 = None
        PROP4 = None
        ax = None
        bx = None
        cx = None
        dx = None
        x = None
        mpineq2 = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:26:2: ( ^( OR ax= expr bx= expr ) | ^( AND cx= expr dx= expr ) | ^( IMP cx= expr dx= expr ) | ^( NEXT x= expr ) | ^( UNTIL ax= expr bx= expr ) | ^( WUNTIL ax= expr bx= expr ) | ^( FINAL x= expr ) | ^( GLOBAL x= expr ) | ^( NOT x= expr ) | ^( MP mpineq ) | ^( TERM x= expr ) | ^( '*' ax= expr bx= expr ) | ^( '+' ax= expr bx= expr ) | ^( '-' ax= expr bx= expr ) | DIGITS | PROP )
                alt2 = 16
                LA2 = self.input.LA(1)
                if LA2 == OR:
                    alt2 = 1
                elif LA2 == AND:
                    alt2 = 2
                elif LA2 == IMP:
                    alt2 = 3
                elif LA2 == NEXT:
                    alt2 = 4
                elif LA2 == UNTIL:
                    alt2 = 5
                elif LA2 == WUNTIL:
                    alt2 = 6
                elif LA2 == FINAL:
                    alt2 = 7
                elif LA2 == GLOBAL:
                    alt2 = 8
                elif LA2 == NOT:
                    alt2 = 9
                elif LA2 == MP:
                    alt2 = 10
                elif LA2 == TERM:
                    alt2 = 11
                elif LA2 == 22:
                    alt2 = 12
                elif LA2 == 23:
                    alt2 = 13
                elif LA2 == 24:
                    alt2 = 14
                elif LA2 == DIGITS:
                    alt2 = 15
                elif LA2 == PROP:
                    alt2 = 16
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:26:3: ^( OR ax= expr bx= expr )
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_expr92)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr96)
                    ax = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr100)
                    bx = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('OR')
                    value.child.append(ax)
                    value.child.append(bx)
                    #action end



                elif alt2 == 2:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:31:3: ^( AND cx= expr dx= expr )
                    pass 
                    self.match(self.input, AND, self.FOLLOW_AND_in_expr109)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr113)
                    cx = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr117)
                    dx = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('AND')
                    value.child.append(cx)
                    value.child.append(dx)
                    #action end



                elif alt2 == 3:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:36:3: ^( IMP cx= expr dx= expr )
                    pass 
                    self.match(self.input, IMP, self.FOLLOW_IMP_in_expr126)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr130)
                    cx = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr134)
                    dx = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('IMP')
                    value.child.append(cx)
                    value.child.append(dx)
                    #action end



                elif alt2 == 4:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:41:3: ^( NEXT x= expr )
                    pass 
                    self.match(self.input, NEXT, self.FOLLOW_NEXT_in_expr143)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr147)
                    x = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('X')
                    value.child.append(x)
                    #action end



                elif alt2 == 5:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:45:3: ^( UNTIL ax= expr bx= expr )
                    pass 
                    self.match(self.input, UNTIL, self.FOLLOW_UNTIL_in_expr156)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr160)
                    ax = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr164)
                    bx = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('U')
                    value.child.append(ax)
                    value.child.append(bx)
                    #action end



                elif alt2 == 6:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:50:3: ^( WUNTIL ax= expr bx= expr )
                    pass 
                    self.match(self.input, WUNTIL, self.FOLLOW_WUNTIL_in_expr173)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr177)
                    ax = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr181)
                    bx = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('V')
                    value.child.append(ax)
                    value.child.append(bx)
                    #action end



                elif alt2 == 7:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:55:3: ^( FINAL x= expr )
                    pass 
                    self.match(self.input, FINAL, self.FOLLOW_FINAL_in_expr190)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr194)
                    x = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('F')
                    value.child.append(x)
                    #action end



                elif alt2 == 8:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:59:3: ^( GLOBAL x= expr )
                    pass 
                    self.match(self.input, GLOBAL, self.FOLLOW_GLOBAL_in_expr203)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr207)
                    x = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('G')
                    value.child.append(x)
                    #action end



                elif alt2 == 9:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:63:3: ^( NOT x= expr )
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_expr216)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr220)
                    x = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('NOT')
                    value.child.append(x)
                    #action end



                elif alt2 == 10:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:67:3: ^( MP mpineq )
                    pass 
                    MP1 = self.match(self.input, MP, self.FOLLOW_MP_in_expr229)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_mpineq_in_expr231)
                    mpineq2 = self.mpineq()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree(MP1.toString())
                    value.ineq = ((mpineq2 is not None) and [mpineq2.ineq] or [None])[0]
                    value.const = ((mpineq2 is not None) and [mpineq2.const] or [None])[0]
                    value.child.append(((mpineq2 is not None) and [mpineq2.value] or [None])[0])
                    #action end



                elif alt2 == 11:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:73:3: ^( TERM x= expr )
                    pass 
                    self.match(self.input, TERM, self.FOLLOW_TERM_in_expr240)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr244)
                    x = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('TERM')
                    value.child.append(x)
                    #action end



                elif alt2 == 12:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:77:3: ^( '*' ax= expr bx= expr )
                    pass 
                    self.match(self.input, 22, self.FOLLOW_22_in_expr253)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr257)
                    ax = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr261)
                    bx = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('*')
                    value.child.append(ax)
                    value.child.append(bx)
                    #action end



                elif alt2 == 13:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:81:3: ^( '+' ax= expr bx= expr )
                    pass 
                    self.match(self.input, 23, self.FOLLOW_23_in_expr269)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr273)
                    ax = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr277)
                    bx = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('+')
                    value.child.append(ax)
                    value.child.append(bx)
                    #action end



                elif alt2 == 14:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:85:3: ^( '-' ax= expr bx= expr )
                    pass 
                    self.match(self.input, 24, self.FOLLOW_24_in_expr285)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr289)
                    ax = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr293)
                    bx = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = maketree('-')
                    value.child.append(ax)
                    value.child.append(bx)
                    #action end



                elif alt2 == 15:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:90:3: DIGITS
                    pass 
                    DIGITS3 = self.match(self.input, DIGITS, self.FOLLOW_DIGITS_in_expr301)

                    #action start
                    value = maketree(DIGITS3.toString())
                    #print ' digits(leaf): '+ DIGITS3.toString()

                    #action end



                elif alt2 == 16:
                    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:94:3: PROP
                    pass 
                    PROP4 = self.match(self.input, PROP, self.FOLLOW_PROP_in_expr307)

                    #action start
                    value = maketree(PROP4.toString())
                    #print ' prop: '+PROP4.toString()

                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "expr"


    class mpineq_return(TreeRuleReturnScope):
        def __init__(self):
            super(LTLMPTree.mpineq_return, self).__init__()

            self.ineq = None
            self.const = None
            self.value = None





    # $ANTLR start "mpineq"
    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:101:1: mpineq returns [ineq, const, value] : ^(str= INEQ mpconst ) ;
    def mpineq(self, ):
        retval = self.mpineq_return()
        retval.start = self.input.LT(1)


        str = None
        mpconst5 = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:102:2: ( ^(str= INEQ mpconst ) )
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:102:3: ^(str= INEQ mpconst )
                pass 
                str = self.match(self.input, INEQ, self.FOLLOW_INEQ_in_mpineq326)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_mpconst_in_mpineq328)
                mpconst5 = self.mpconst()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.ineq = str.toString()
                retval.const = ((mpconst5 is not None) and [mpconst5.const] or [None])[0]
                retval.value = ((mpconst5 is not None) and [mpconst5.value] or [None])[0]
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "mpineq"


    class mpconst_return(TreeRuleReturnScope):
        def __init__(self):
            super(LTLMPTree.mpconst_return, self).__init__()

            self.const = None
            self.value = None





    # $ANTLR start "mpconst"
    # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:107:1: mpconst returns [const, value] : ^( DIGITS x= expr ) ;
    def mpconst(self, ):
        retval = self.mpconst_return()
        retval.start = self.input.LT(1)


        DIGITS6 = None
        x = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:108:2: ( ^( DIGITS x= expr ) )
                # /Users/taka/works/github/sotsuron/antlr_files/LTLMPTree.g:108:3: ^( DIGITS x= expr )
                pass 
                DIGITS6 = self.match(self.input, DIGITS, self.FOLLOW_DIGITS_in_mpconst344)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_expr_in_mpconst348)
                x = self.expr()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.const = DIGITS6.getText()
                retval.value = x
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "mpconst"



 

    FOLLOW_stat_in_prog55 = frozenset([1, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_stat72 = frozenset([1])
    FOLLOW_OR_in_expr92 = frozenset([2])
    FOLLOW_expr_in_expr96 = frozenset([4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_expr100 = frozenset([3])
    FOLLOW_AND_in_expr109 = frozenset([2])
    FOLLOW_expr_in_expr113 = frozenset([4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_expr117 = frozenset([3])
    FOLLOW_IMP_in_expr126 = frozenset([2])
    FOLLOW_expr_in_expr130 = frozenset([4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_expr134 = frozenset([3])
    FOLLOW_NEXT_in_expr143 = frozenset([2])
    FOLLOW_expr_in_expr147 = frozenset([3])
    FOLLOW_UNTIL_in_expr156 = frozenset([2])
    FOLLOW_expr_in_expr160 = frozenset([4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_expr164 = frozenset([3])
    FOLLOW_WUNTIL_in_expr173 = frozenset([2])
    FOLLOW_expr_in_expr177 = frozenset([4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_expr181 = frozenset([3])
    FOLLOW_FINAL_in_expr190 = frozenset([2])
    FOLLOW_expr_in_expr194 = frozenset([3])
    FOLLOW_GLOBAL_in_expr203 = frozenset([2])
    FOLLOW_expr_in_expr207 = frozenset([3])
    FOLLOW_NOT_in_expr216 = frozenset([2])
    FOLLOW_expr_in_expr220 = frozenset([3])
    FOLLOW_MP_in_expr229 = frozenset([2])
    FOLLOW_mpineq_in_expr231 = frozenset([3])
    FOLLOW_TERM_in_expr240 = frozenset([2])
    FOLLOW_expr_in_expr244 = frozenset([3])
    FOLLOW_22_in_expr253 = frozenset([2])
    FOLLOW_expr_in_expr257 = frozenset([4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_expr261 = frozenset([3])
    FOLLOW_23_in_expr269 = frozenset([2])
    FOLLOW_expr_in_expr273 = frozenset([4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_expr277 = frozenset([3])
    FOLLOW_24_in_expr285 = frozenset([2])
    FOLLOW_expr_in_expr289 = frozenset([4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 22, 23, 24])
    FOLLOW_expr_in_expr293 = frozenset([3])
    FOLLOW_DIGITS_in_expr301 = frozenset([1])
    FOLLOW_PROP_in_expr307 = frozenset([1])
    FOLLOW_INEQ_in_mpineq326 = frozenset([2])
    FOLLOW_mpconst_in_mpineq328 = frozenset([3])
    FOLLOW_DIGITS_in_mpconst344 = frozenset([2])
    FOLLOW_expr_in_mpconst348 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(LTLMPTree)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
