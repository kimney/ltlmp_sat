# $ANTLR 3.5 /Users/taka/works/github/sotsuron/LTLMP.g 2013-07-14 16:38:49

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




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




class LTLMPParser(Parser):
    grammarFileName = "/Users/taka/works/github/sotsuron/LTLMP.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(LTLMPParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.start_return, self).__init__()

            self.tree = None





    # $ANTLR start "start"
    # /Users/taka/works/github/sotsuron/LTLMP.g:18:1: start : stmt ( NEWLINE !)* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE2 = None
        stmt1 = None

        NEWLINE2_tree = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:18:7: ( stmt ( NEWLINE !)* )
                # /Users/taka/works/github/sotsuron/LTLMP.g:18:8: stmt ( NEWLINE !)*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_stmt_in_start52)
                stmt1 = self.stmt()

                self._state.following.pop()
                self._adaptor.addChild(root_0, stmt1.tree)


                # /Users/taka/works/github/sotsuron/LTLMP.g:18:13: ( NEWLINE !)*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NEWLINE) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/taka/works/github/sotsuron/LTLMP.g:18:14: NEWLINE !
                        pass 
                        NEWLINE2 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_start55)


                    else:
                        break #loop1




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "start"


    class stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.stmt_return, self).__init__()

            self.tree = None





    # $ANTLR start "stmt"
    # /Users/taka/works/github/sotsuron/LTLMP.g:19:1: stmt : andstmt ( OR ^ andstmt )* ;
    def stmt(self, ):
        retval = self.stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OR4 = None
        andstmt3 = None
        andstmt5 = None

        OR4_tree = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:19:6: ( andstmt ( OR ^ andstmt )* )
                # /Users/taka/works/github/sotsuron/LTLMP.g:19:7: andstmt ( OR ^ andstmt )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_andstmt_in_stmt66)
                andstmt3 = self.andstmt()

                self._state.following.pop()
                self._adaptor.addChild(root_0, andstmt3.tree)


                # /Users/taka/works/github/sotsuron/LTLMP.g:19:15: ( OR ^ andstmt )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == OR) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/taka/works/github/sotsuron/LTLMP.g:19:16: OR ^ andstmt
                        pass 
                        OR4 = self.match(self.input, OR, self.FOLLOW_OR_in_stmt69)
                        OR4_tree = self._adaptor.createWithPayload(OR4)
                        root_0 = self._adaptor.becomeRoot(OR4_tree, root_0)



                        self._state.following.append(self.FOLLOW_andstmt_in_stmt72)
                        andstmt5 = self.andstmt()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, andstmt5.tree)



                    else:
                        break #loop2




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "stmt"


    class andstmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.andstmt_return, self).__init__()

            self.tree = None





    # $ANTLR start "andstmt"
    # /Users/taka/works/github/sotsuron/LTLMP.g:20:1: andstmt : binarystmt ( AND ^ binarystmt )* ;
    def andstmt(self, ):
        retval = self.andstmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        AND7 = None
        binarystmt6 = None
        binarystmt8 = None

        AND7_tree = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:20:9: ( binarystmt ( AND ^ binarystmt )* )
                # /Users/taka/works/github/sotsuron/LTLMP.g:20:10: binarystmt ( AND ^ binarystmt )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_binarystmt_in_andstmt80)
                binarystmt6 = self.binarystmt()

                self._state.following.pop()
                self._adaptor.addChild(root_0, binarystmt6.tree)


                # /Users/taka/works/github/sotsuron/LTLMP.g:20:21: ( AND ^ binarystmt )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == AND) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/taka/works/github/sotsuron/LTLMP.g:20:22: AND ^ binarystmt
                        pass 
                        AND7 = self.match(self.input, AND, self.FOLLOW_AND_in_andstmt83)
                        AND7_tree = self._adaptor.createWithPayload(AND7)
                        root_0 = self._adaptor.becomeRoot(AND7_tree, root_0)



                        self._state.following.append(self.FOLLOW_binarystmt_in_andstmt86)
                        binarystmt8 = self.binarystmt()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, binarystmt8.tree)



                    else:
                        break #loop3




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "andstmt"


    class binarystmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.binarystmt_return, self).__init__()

            self.tree = None





    # $ANTLR start "binarystmt"
    # /Users/taka/works/github/sotsuron/LTLMP.g:21:1: binarystmt : unarystmt ( ( UNTIL | WUNTIL | IMP ) ^ unarystmt )* ;
    def binarystmt(self, ):
        retval = self.binarystmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set10 = None
        unarystmt9 = None
        unarystmt11 = None

        set10_tree = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:21:11: ( unarystmt ( ( UNTIL | WUNTIL | IMP ) ^ unarystmt )* )
                # /Users/taka/works/github/sotsuron/LTLMP.g:21:12: unarystmt ( ( UNTIL | WUNTIL | IMP ) ^ unarystmt )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_unarystmt_in_binarystmt93)
                unarystmt9 = self.unarystmt()

                self._state.following.pop()
                self._adaptor.addChild(root_0, unarystmt9.tree)


                # /Users/taka/works/github/sotsuron/LTLMP.g:21:22: ( ( UNTIL | WUNTIL | IMP ) ^ unarystmt )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == IMP or LA4_0 == UNTIL or LA4_0 == WUNTIL) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/taka/works/github/sotsuron/LTLMP.g:21:23: ( UNTIL | WUNTIL | IMP ) ^ unarystmt
                        pass 
                        set10 = self.input.LT(1)

                        set10 = self.input.LT(1)

                        if self.input.LA(1) == IMP or self.input.LA(1) == UNTIL or self.input.LA(1) == WUNTIL:
                            self.input.consume()
                            root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set10), root_0)

                            self._state.errorRecovery = False


                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse



                        self._state.following.append(self.FOLLOW_unarystmt_in_binarystmt105)
                        unarystmt11 = self.unarystmt()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, unarystmt11.tree)



                    else:
                        break #loop4




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "binarystmt"


    class unarystmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.unarystmt_return, self).__init__()

            self.tree = None





    # $ANTLR start "unarystmt"
    # /Users/taka/works/github/sotsuron/LTLMP.g:23:1: unarystmt : ( FINAL unarystmt -> ^( FINAL unarystmt ) | GLOBAL unarystmt -> ^( GLOBAL unarystmt ) | NOT unarystmt -> ^( NOT unarystmt ) | NEXT unarystmt -> ^( NEXT unarystmt ) | prop );
    def unarystmt(self, ):
        retval = self.unarystmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FINAL12 = None
        GLOBAL14 = None
        NOT16 = None
        NEXT18 = None
        unarystmt13 = None
        unarystmt15 = None
        unarystmt17 = None
        unarystmt19 = None
        prop20 = None

        FINAL12_tree = None
        GLOBAL14_tree = None
        NOT16_tree = None
        NEXT18_tree = None
        stream_FINAL = RewriteRuleTokenStream(self._adaptor, "token FINAL")
        stream_NEXT = RewriteRuleTokenStream(self._adaptor, "token NEXT")
        stream_NOT = RewriteRuleTokenStream(self._adaptor, "token NOT")
        stream_GLOBAL = RewriteRuleTokenStream(self._adaptor, "token GLOBAL")
        stream_unarystmt = RewriteRuleSubtreeStream(self._adaptor, "rule unarystmt")
        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:23:10: ( FINAL unarystmt -> ^( FINAL unarystmt ) | GLOBAL unarystmt -> ^( GLOBAL unarystmt ) | NOT unarystmt -> ^( NOT unarystmt ) | NEXT unarystmt -> ^( NEXT unarystmt ) | prop )
                alt5 = 5
                LA5 = self.input.LA(1)
                if LA5 == FINAL:
                    alt5 = 1
                elif LA5 == GLOBAL:
                    alt5 = 2
                elif LA5 == NOT:
                    alt5 = 3
                elif LA5 == NEXT:
                    alt5 = 4
                elif LA5 == MP or LA5 == PROP or LA5 == 20:
                    alt5 = 5
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:24:2: FINAL unarystmt
                    pass 
                    FINAL12 = self.match(self.input, FINAL, self.FOLLOW_FINAL_in_unarystmt115) 
                    stream_FINAL.add(FINAL12)


                    self._state.following.append(self.FOLLOW_unarystmt_in_unarystmt117)
                    unarystmt13 = self.unarystmt()

                    self._state.following.pop()
                    stream_unarystmt.add(unarystmt13.tree)


                    # AST Rewrite
                    # elements: unarystmt, FINAL
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 24:18: -> ^( FINAL unarystmt )
                    # /Users/taka/works/github/sotsuron/LTLMP.g:24:21: ^( FINAL unarystmt )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_FINAL.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_unarystmt.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt5 == 2:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:25:3: GLOBAL unarystmt
                    pass 
                    GLOBAL14 = self.match(self.input, GLOBAL, self.FOLLOW_GLOBAL_in_unarystmt129) 
                    stream_GLOBAL.add(GLOBAL14)


                    self._state.following.append(self.FOLLOW_unarystmt_in_unarystmt131)
                    unarystmt15 = self.unarystmt()

                    self._state.following.pop()
                    stream_unarystmt.add(unarystmt15.tree)


                    # AST Rewrite
                    # elements: GLOBAL, unarystmt
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 25:20: -> ^( GLOBAL unarystmt )
                    # /Users/taka/works/github/sotsuron/LTLMP.g:25:23: ^( GLOBAL unarystmt )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_GLOBAL.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_unarystmt.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt5 == 3:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:26:3: NOT unarystmt
                    pass 
                    NOT16 = self.match(self.input, NOT, self.FOLLOW_NOT_in_unarystmt143) 
                    stream_NOT.add(NOT16)


                    self._state.following.append(self.FOLLOW_unarystmt_in_unarystmt145)
                    unarystmt17 = self.unarystmt()

                    self._state.following.pop()
                    stream_unarystmt.add(unarystmt17.tree)


                    # AST Rewrite
                    # elements: unarystmt, NOT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 26:17: -> ^( NOT unarystmt )
                    # /Users/taka/works/github/sotsuron/LTLMP.g:26:20: ^( NOT unarystmt )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_NOT.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_unarystmt.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt5 == 4:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:27:3: NEXT unarystmt
                    pass 
                    NEXT18 = self.match(self.input, NEXT, self.FOLLOW_NEXT_in_unarystmt158) 
                    stream_NEXT.add(NEXT18)


                    self._state.following.append(self.FOLLOW_unarystmt_in_unarystmt160)
                    unarystmt19 = self.unarystmt()

                    self._state.following.pop()
                    stream_unarystmt.add(unarystmt19.tree)


                    # AST Rewrite
                    # elements: unarystmt, NEXT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 27:18: -> ^( NEXT unarystmt )
                    # /Users/taka/works/github/sotsuron/LTLMP.g:27:21: ^( NEXT unarystmt )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_NEXT.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_unarystmt.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt5 == 5:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:28:3: prop
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_prop_in_unarystmt172)
                    prop20 = self.prop()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, prop20.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "unarystmt"


    class prop_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.prop_return, self).__init__()

            self.tree = None





    # $ANTLR start "prop"
    # /Users/taka/works/github/sotsuron/LTLMP.g:29:1: prop : ( PROP ^| MP '(' mpexpr ')' INEQ DIGITS -> ^( MP ^( INEQ ^( DIGITS mpexpr ) ) ) | '(' ! stmt ')' !);
    def prop(self, ):
        retval = self.prop_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROP21 = None
        MP22 = None
        char_literal23 = None
        char_literal25 = None
        INEQ26 = None
        DIGITS27 = None
        char_literal28 = None
        char_literal30 = None
        mpexpr24 = None
        stmt29 = None

        PROP21_tree = None
        MP22_tree = None
        char_literal23_tree = None
        char_literal25_tree = None
        INEQ26_tree = None
        DIGITS27_tree = None
        char_literal28_tree = None
        char_literal30_tree = None
        stream_21 = RewriteRuleTokenStream(self._adaptor, "token 21")
        stream_INEQ = RewriteRuleTokenStream(self._adaptor, "token INEQ")
        stream_20 = RewriteRuleTokenStream(self._adaptor, "token 20")
        stream_MP = RewriteRuleTokenStream(self._adaptor, "token MP")
        stream_DIGITS = RewriteRuleTokenStream(self._adaptor, "token DIGITS")
        stream_mpexpr = RewriteRuleSubtreeStream(self._adaptor, "rule mpexpr")
        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:29:6: ( PROP ^| MP '(' mpexpr ')' INEQ DIGITS -> ^( MP ^( INEQ ^( DIGITS mpexpr ) ) ) | '(' ! stmt ')' !)
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 == PROP:
                    alt6 = 1
                elif LA6 == MP:
                    alt6 = 2
                elif LA6 == 20:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:29:7: PROP ^
                    pass 
                    root_0 = self._adaptor.nil()


                    PROP21 = self.match(self.input, PROP, self.FOLLOW_PROP_in_prop178)
                    PROP21_tree = self._adaptor.createWithPayload(PROP21)
                    root_0 = self._adaptor.becomeRoot(PROP21_tree, root_0)




                elif alt6 == 2:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:30:3: MP '(' mpexpr ')' INEQ DIGITS
                    pass 
                    MP22 = self.match(self.input, MP, self.FOLLOW_MP_in_prop183) 
                    stream_MP.add(MP22)


                    char_literal23 = self.match(self.input, 20, self.FOLLOW_20_in_prop184) 
                    stream_20.add(char_literal23)


                    self._state.following.append(self.FOLLOW_mpexpr_in_prop185)
                    mpexpr24 = self.mpexpr()

                    self._state.following.pop()
                    stream_mpexpr.add(mpexpr24.tree)


                    char_literal25 = self.match(self.input, 21, self.FOLLOW_21_in_prop186) 
                    stream_21.add(char_literal25)


                    INEQ26 = self.match(self.input, INEQ, self.FOLLOW_INEQ_in_prop188) 
                    stream_INEQ.add(INEQ26)


                    DIGITS27 = self.match(self.input, DIGITS, self.FOLLOW_DIGITS_in_prop190) 
                    stream_DIGITS.add(DIGITS27)


                    # AST Rewrite
                    # elements: MP, DIGITS, mpexpr, INEQ
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 30:30: -> ^( MP ^( INEQ ^( DIGITS mpexpr ) ) )
                    # /Users/taka/works/github/sotsuron/LTLMP.g:30:33: ^( MP ^( INEQ ^( DIGITS mpexpr ) ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_MP.nextNode()
                    , root_1)

                    # /Users/taka/works/github/sotsuron/LTLMP.g:30:38: ^( INEQ ^( DIGITS mpexpr ) )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    stream_INEQ.nextNode()
                    , root_2)

                    # /Users/taka/works/github/sotsuron/LTLMP.g:30:45: ^( DIGITS mpexpr )
                    root_3 = self._adaptor.nil()
                    root_3 = self._adaptor.becomeRoot(
                    stream_DIGITS.nextNode()
                    , root_3)

                    self._adaptor.addChild(root_3, stream_mpexpr.nextTree())

                    self._adaptor.addChild(root_2, root_3)

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt6 == 3:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:31:3: '(' ! stmt ')' !
                    pass 
                    root_0 = self._adaptor.nil()


                    char_literal28 = self.match(self.input, 20, self.FOLLOW_20_in_prop210)

                    self._state.following.append(self.FOLLOW_stmt_in_prop212)
                    stmt29 = self.stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, stmt29.tree)


                    char_literal30 = self.match(self.input, 21, self.FOLLOW_21_in_prop213)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "prop"


    class mpexpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.mpexpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "mpexpr"
    # /Users/taka/works/github/sotsuron/LTLMP.g:34:1: mpexpr : mpprod ( '-' ^ mpprod | '+' ^ mpprod )* ;
    def mpexpr(self, ):
        retval = self.mpexpr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal32 = None
        char_literal34 = None
        mpprod31 = None
        mpprod33 = None
        mpprod35 = None

        char_literal32_tree = None
        char_literal34_tree = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:34:8: ( mpprod ( '-' ^ mpprod | '+' ^ mpprod )* )
                # /Users/taka/works/github/sotsuron/LTLMP.g:34:9: mpprod ( '-' ^ mpprod | '+' ^ mpprod )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_mpprod_in_mpexpr224)
                mpprod31 = self.mpprod()

                self._state.following.pop()
                self._adaptor.addChild(root_0, mpprod31.tree)


                # /Users/taka/works/github/sotsuron/LTLMP.g:34:16: ( '-' ^ mpprod | '+' ^ mpprod )*
                while True: #loop7
                    alt7 = 3
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 24) :
                        alt7 = 1
                    elif (LA7_0 == 23) :
                        alt7 = 2


                    if alt7 == 1:
                        # /Users/taka/works/github/sotsuron/LTLMP.g:34:17: '-' ^ mpprod
                        pass 
                        char_literal32 = self.match(self.input, 24, self.FOLLOW_24_in_mpexpr227)
                        char_literal32_tree = self._adaptor.createWithPayload(char_literal32)
                        root_0 = self._adaptor.becomeRoot(char_literal32_tree, root_0)



                        self._state.following.append(self.FOLLOW_mpprod_in_mpexpr230)
                        mpprod33 = self.mpprod()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, mpprod33.tree)



                    elif alt7 == 2:
                        # /Users/taka/works/github/sotsuron/LTLMP.g:34:31: '+' ^ mpprod
                        pass 
                        char_literal34 = self.match(self.input, 23, self.FOLLOW_23_in_mpexpr234)
                        char_literal34_tree = self._adaptor.createWithPayload(char_literal34)
                        root_0 = self._adaptor.becomeRoot(char_literal34_tree, root_0)



                        self._state.following.append(self.FOLLOW_mpprod_in_mpexpr237)
                        mpprod35 = self.mpprod()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, mpprod35.tree)



                    else:
                        break #loop7




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mpexpr"


    class mpprod_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.mpprod_return, self).__init__()

            self.tree = None





    # $ANTLR start "mpprod"
    # /Users/taka/works/github/sotsuron/LTLMP.g:35:1: mpprod : mpterm ( '*' ^ mpterm )* ;
    def mpprod(self, ):
        retval = self.mpprod_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal37 = None
        mpterm36 = None
        mpterm38 = None

        char_literal37_tree = None

        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:35:8: ( mpterm ( '*' ^ mpterm )* )
                # /Users/taka/works/github/sotsuron/LTLMP.g:35:9: mpterm ( '*' ^ mpterm )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_mpterm_in_mpprod246)
                mpterm36 = self.mpterm()

                self._state.following.pop()
                self._adaptor.addChild(root_0, mpterm36.tree)


                # /Users/taka/works/github/sotsuron/LTLMP.g:35:16: ( '*' ^ mpterm )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 22) :
                        alt8 = 1


                    if alt8 == 1:
                        # /Users/taka/works/github/sotsuron/LTLMP.g:35:17: '*' ^ mpterm
                        pass 
                        char_literal37 = self.match(self.input, 22, self.FOLLOW_22_in_mpprod249)
                        char_literal37_tree = self._adaptor.createWithPayload(char_literal37)
                        root_0 = self._adaptor.becomeRoot(char_literal37_tree, root_0)



                        self._state.following.append(self.FOLLOW_mpterm_in_mpprod252)
                        mpterm38 = self.mpterm()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, mpterm38.tree)



                    else:
                        break #loop8




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mpprod"


    class mpterm_return(ParserRuleReturnScope):
        def __init__(self):
            super(LTLMPParser.mpterm_return, self).__init__()

            self.tree = None





    # $ANTLR start "mpterm"
    # /Users/taka/works/github/sotsuron/LTLMP.g:36:1: mpterm : ( TERM '(' stmt ')' -> ^( TERM stmt ) | '(' ! mpexpr ')' !| DIGITS );
    def mpterm(self, ):
        retval = self.mpterm_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TERM39 = None
        char_literal40 = None
        char_literal42 = None
        char_literal43 = None
        char_literal45 = None
        DIGITS46 = None
        stmt41 = None
        mpexpr44 = None

        TERM39_tree = None
        char_literal40_tree = None
        char_literal42_tree = None
        char_literal43_tree = None
        char_literal45_tree = None
        DIGITS46_tree = None
        stream_21 = RewriteRuleTokenStream(self._adaptor, "token 21")
        stream_TERM = RewriteRuleTokenStream(self._adaptor, "token TERM")
        stream_20 = RewriteRuleTokenStream(self._adaptor, "token 20")
        stream_stmt = RewriteRuleSubtreeStream(self._adaptor, "rule stmt")
        try:
            try:
                # /Users/taka/works/github/sotsuron/LTLMP.g:36:9: ( TERM '(' stmt ')' -> ^( TERM stmt ) | '(' ! mpexpr ')' !| DIGITS )
                alt9 = 3
                LA9 = self.input.LA(1)
                if LA9 == TERM:
                    alt9 = 1
                elif LA9 == 20:
                    alt9 = 2
                elif LA9 == DIGITS:
                    alt9 = 3
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:36:10: TERM '(' stmt ')'
                    pass 
                    TERM39 = self.match(self.input, TERM, self.FOLLOW_TERM_in_mpterm261) 
                    stream_TERM.add(TERM39)


                    char_literal40 = self.match(self.input, 20, self.FOLLOW_20_in_mpterm263) 
                    stream_20.add(char_literal40)


                    self._state.following.append(self.FOLLOW_stmt_in_mpterm264)
                    stmt41 = self.stmt()

                    self._state.following.pop()
                    stream_stmt.add(stmt41.tree)


                    char_literal42 = self.match(self.input, 21, self.FOLLOW_21_in_mpterm265) 
                    stream_21.add(char_literal42)


                    # AST Rewrite
                    # elements: stmt, TERM
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 36:26: -> ^( TERM stmt )
                    # /Users/taka/works/github/sotsuron/LTLMP.g:36:29: ^( TERM stmt )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_TERM.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_stmt.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt9 == 2:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:37:3: '(' ! mpexpr ')' !
                    pass 
                    root_0 = self._adaptor.nil()


                    char_literal43 = self.match(self.input, 20, self.FOLLOW_20_in_mpterm277)

                    self._state.following.append(self.FOLLOW_mpexpr_in_mpterm279)
                    mpexpr44 = self.mpexpr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, mpexpr44.tree)


                    char_literal45 = self.match(self.input, 21, self.FOLLOW_21_in_mpterm280)


                elif alt9 == 3:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:38:3: DIGITS
                    pass 
                    root_0 = self._adaptor.nil()


                    DIGITS46 = self.match(self.input, DIGITS, self.FOLLOW_DIGITS_in_mpterm285)
                    DIGITS46_tree = self._adaptor.createWithPayload(DIGITS46)
                    self._adaptor.addChild(root_0, DIGITS46_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "mpterm"



 

    FOLLOW_stmt_in_start52 = frozenset([1, 11])
    FOLLOW_NEWLINE_in_start55 = frozenset([1, 11])
    FOLLOW_andstmt_in_stmt66 = frozenset([1, 14])
    FOLLOW_OR_in_stmt69 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_andstmt_in_stmt72 = frozenset([1, 14])
    FOLLOW_binarystmt_in_andstmt80 = frozenset([1, 4])
    FOLLOW_AND_in_andstmt83 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_binarystmt_in_andstmt86 = frozenset([1, 4])
    FOLLOW_unarystmt_in_binarystmt93 = frozenset([1, 8, 17, 19])
    FOLLOW_set_in_binarystmt96 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_unarystmt_in_binarystmt105 = frozenset([1, 8, 17, 19])
    FOLLOW_FINAL_in_unarystmt115 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_unarystmt_in_unarystmt117 = frozenset([1])
    FOLLOW_GLOBAL_in_unarystmt129 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_unarystmt_in_unarystmt131 = frozenset([1])
    FOLLOW_NOT_in_unarystmt143 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_unarystmt_in_unarystmt145 = frozenset([1])
    FOLLOW_NEXT_in_unarystmt158 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_unarystmt_in_unarystmt160 = frozenset([1])
    FOLLOW_prop_in_unarystmt172 = frozenset([1])
    FOLLOW_PROP_in_prop178 = frozenset([1])
    FOLLOW_MP_in_prop183 = frozenset([20])
    FOLLOW_20_in_prop184 = frozenset([5, 16, 20])
    FOLLOW_mpexpr_in_prop185 = frozenset([21])
    FOLLOW_21_in_prop186 = frozenset([9])
    FOLLOW_INEQ_in_prop188 = frozenset([5])
    FOLLOW_DIGITS_in_prop190 = frozenset([1])
    FOLLOW_20_in_prop210 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_stmt_in_prop212 = frozenset([21])
    FOLLOW_21_in_prop213 = frozenset([1])
    FOLLOW_mpprod_in_mpexpr224 = frozenset([1, 23, 24])
    FOLLOW_24_in_mpexpr227 = frozenset([5, 16, 20])
    FOLLOW_mpprod_in_mpexpr230 = frozenset([1, 23, 24])
    FOLLOW_23_in_mpexpr234 = frozenset([5, 16, 20])
    FOLLOW_mpprod_in_mpexpr237 = frozenset([1, 23, 24])
    FOLLOW_mpterm_in_mpprod246 = frozenset([1, 22])
    FOLLOW_22_in_mpprod249 = frozenset([5, 16, 20])
    FOLLOW_mpterm_in_mpprod252 = frozenset([1, 22])
    FOLLOW_TERM_in_mpterm261 = frozenset([20])
    FOLLOW_20_in_mpterm263 = frozenset([6, 7, 10, 12, 13, 15, 20])
    FOLLOW_stmt_in_mpterm264 = frozenset([21])
    FOLLOW_21_in_mpterm265 = frozenset([1])
    FOLLOW_20_in_mpterm277 = frozenset([5, 16, 20])
    FOLLOW_mpexpr_in_mpterm279 = frozenset([21])
    FOLLOW_21_in_mpterm280 = frozenset([1])
    FOLLOW_DIGITS_in_mpterm285 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("LTLMPLexer", LTLMPParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
