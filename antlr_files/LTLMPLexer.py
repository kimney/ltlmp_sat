# $ANTLR 3.5 /Users/taka/works/github/sotsuron/LTLMP.g 2013-07-14 16:38:49

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



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


class LTLMPLexer(Lexer):

    grammarFileName = "/Users/taka/works/github/sotsuron/LTLMP.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(LTLMPLexer, self).__init__(input, state)

        self.delegates = []






    # $ANTLR start "T__20"
    def mT__20(self, ):
        try:
            _type = T__20
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:7:7: ( '(' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:7:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__20"



    # $ANTLR start "T__21"
    def mT__21(self, ):
        try:
            _type = T__21
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:8:7: ( ')' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:8:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__21"



    # $ANTLR start "T__22"
    def mT__22(self, ):
        try:
            _type = T__22
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:9:7: ( '*' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:9:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__22"



    # $ANTLR start "T__23"
    def mT__23(self, ):
        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:10:7: ( '+' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:10:9: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__23"



    # $ANTLR start "T__24"
    def mT__24(self, ):
        try:
            _type = T__24
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:11:7: ( '-' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:11:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__24"



    # $ANTLR start "MP"
    def mMP(self, ):
        try:
            _type = MP
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:41:4: ( 'MP^' | 'MP_' )
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 77) :
                LA1_1 = self.input.LA(2)

                if (LA1_1 == 80) :
                    LA1_2 = self.input.LA(3)

                    if (LA1_2 == 94) :
                        alt1 = 1
                    elif (LA1_2 == 95) :
                        alt1 = 2
                    else:
                        nvae = NoViableAltException("", 1, 2, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 1, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae


            if alt1 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:41:5: 'MP^'
                pass 
                self.match("MP^")



            elif alt1 == 2:
                # /Users/taka/works/github/sotsuron/LTLMP.g:41:11: 'MP_'
                pass 
                self.match("MP_")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MP"



    # $ANTLR start "TERM"
    def mTERM(self, ):
        try:
            _type = TERM
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:42:6: ( 'T' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:42:7: 'T'
            pass 
            self.match(84)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TERM"



    # $ANTLR start "DIGITS"
    def mDIGITS(self, ):
        try:
            _type = DIGITS
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:43:8: ( '1' .. '9' ( '0' .. '9' )* | '0' )
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if ((49 <= LA3_0 <= 57)) :
                alt3 = 1
            elif (LA3_0 == 48) :
                alt3 = 2
            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae


            if alt3 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:43:9: '1' .. '9' ( '0' .. '9' )*
                pass 
                self.matchRange(49, 57)

                # /Users/taka/works/github/sotsuron/LTLMP.g:43:18: ( '0' .. '9' )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((48 <= LA2_0 <= 57)) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/taka/works/github/sotsuron/LTLMP.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop2



            elif alt3 == 2:
                # /Users/taka/works/github/sotsuron/LTLMP.g:43:29: '0'
                pass 
                self.match(48)


            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIGITS"



    # $ANTLR start "INEQ"
    def mINEQ(self, ):
        try:
            _type = INEQ
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:44:6: ( '>' | '>=' | '<' | '<=' )
            alt4 = 4
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 62) :
                LA4_1 = self.input.LA(2)

                if (LA4_1 == 61) :
                    alt4 = 2
                else:
                    alt4 = 1

            elif (LA4_0 == 60) :
                LA4_2 = self.input.LA(2)

                if (LA4_2 == 61) :
                    alt4 = 4
                else:
                    alt4 = 3

            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:44:7: '>'
                pass 
                self.match(62)


            elif alt4 == 2:
                # /Users/taka/works/github/sotsuron/LTLMP.g:44:11: '>='
                pass 
                self.match(">=")



            elif alt4 == 3:
                # /Users/taka/works/github/sotsuron/LTLMP.g:44:16: '<'
                pass 
                self.match(60)


            elif alt4 == 4:
                # /Users/taka/works/github/sotsuron/LTLMP.g:44:20: '<='
                pass 
                self.match("<=")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INEQ"



    # $ANTLR start "IMP"
    def mIMP(self, ):
        try:
            _type = IMP
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:46:5: ( '->' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:46:6: '->'
            pass 
            self.match("->")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IMP"



    # $ANTLR start "PROP"
    def mPROP(self, ):
        try:
            _type = PROP
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:47:6: ( 'a' .. 'z' ( '0' .. '9' | 'a' .. 'z' | '_' )* )
            # /Users/taka/works/github/sotsuron/LTLMP.g:47:7: 'a' .. 'z' ( '0' .. '9' | 'a' .. 'z' | '_' )*
            pass 
            self.matchRange(97, 122)

            # /Users/taka/works/github/sotsuron/LTLMP.g:47:16: ( '0' .. '9' | 'a' .. 'z' | '_' )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or LA5_0 == 95 or (97 <= LA5_0 <= 122)) :
                    alt5 = 1


                if alt5 == 1:
                    # /Users/taka/works/github/sotsuron/LTLMP.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop5




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROP"



    # $ANTLR start "AND"
    def mAND(self, ):
        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:48:5: ( 'AND' | '&&' | '&' )
            alt6 = 3
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 65) :
                alt6 = 1
            elif (LA6_0 == 38) :
                LA6_2 = self.input.LA(2)

                if (LA6_2 == 38) :
                    alt6 = 2
                else:
                    alt6 = 3

            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae


            if alt6 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:48:6: 'AND'
                pass 
                self.match("AND")



            elif alt6 == 2:
                # /Users/taka/works/github/sotsuron/LTLMP.g:48:12: '&&'
                pass 
                self.match("&&")



            elif alt6 == 3:
                # /Users/taka/works/github/sotsuron/LTLMP.g:48:17: '&'
                pass 
                self.match(38)


            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:49:4: ( 'OR' | '||' | '|' )
            alt7 = 3
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 79) :
                alt7 = 1
            elif (LA7_0 == 124) :
                LA7_2 = self.input.LA(2)

                if (LA7_2 == 124) :
                    alt7 = 2
                else:
                    alt7 = 3

            else:
                nvae = NoViableAltException("", 7, 0, self.input)

                raise nvae


            if alt7 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:49:5: 'OR'
                pass 
                self.match("OR")



            elif alt7 == 2:
                # /Users/taka/works/github/sotsuron/LTLMP.g:49:10: '||'
                pass 
                self.match("||")



            elif alt7 == 3:
                # /Users/taka/works/github/sotsuron/LTLMP.g:49:15: '|'
                pass 
                self.match(124)


            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "UNTIL"
    def mUNTIL(self, ):
        try:
            _type = UNTIL
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:50:7: ( 'U' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:50:8: 'U'
            pass 
            self.match(85)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNTIL"



    # $ANTLR start "WUNTIL"
    def mWUNTIL(self, ):
        try:
            _type = WUNTIL
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:51:8: ( 'V' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:51:9: 'V'
            pass 
            self.match(86)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WUNTIL"



    # $ANTLR start "NOT"
    def mNOT(self, ):
        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:52:6: ( '!' | 'NOT' )
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 33) :
                alt8 = 1
            elif (LA8_0 == 78) :
                alt8 = 2
            else:
                nvae = NoViableAltException("", 8, 0, self.input)

                raise nvae


            if alt8 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:52:7: '!'
                pass 
                self.match(33)


            elif alt8 == 2:
                # /Users/taka/works/github/sotsuron/LTLMP.g:52:11: 'NOT'
                pass 
                self.match("NOT")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT"



    # $ANTLR start "NEXT"
    def mNEXT(self, ):
        try:
            _type = NEXT
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:53:7: ( 'X' | 'O' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:
            pass 
            if self.input.LA(1) == 79 or self.input.LA(1) == 88:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEXT"



    # $ANTLR start "GLOBAL"
    def mGLOBAL(self, ):
        try:
            _type = GLOBAL
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:54:9: ( 'G' | '[]' )
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if (LA9_0 == 71) :
                alt9 = 1
            elif (LA9_0 == 91) :
                alt9 = 2
            else:
                nvae = NoViableAltException("", 9, 0, self.input)

                raise nvae


            if alt9 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:54:10: 'G'
                pass 
                self.match(71)


            elif alt9 == 2:
                # /Users/taka/works/github/sotsuron/LTLMP.g:54:14: '[]'
                pass 
                self.match("[]")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GLOBAL"



    # $ANTLR start "FINAL"
    def mFINAL(self, ):
        try:
            _type = FINAL
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:55:8: ( 'F' | '<>' )
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 70) :
                alt10 = 1
            elif (LA10_0 == 60) :
                alt10 = 2
            else:
                nvae = NoViableAltException("", 10, 0, self.input)

                raise nvae


            if alt10 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:55:9: 'F'
                pass 
                self.match(70)


            elif alt10 == 2:
                # /Users/taka/works/github/sotsuron/LTLMP.g:55:13: '<>'
                pass 
                self.match("<>")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FINAL"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:57:9: ( ( '\\r' )? '\\n' )
            # /Users/taka/works/github/sotsuron/LTLMP.g:57:10: ( '\\r' )? '\\n'
            pass 
            # /Users/taka/works/github/sotsuron/LTLMP.g:57:10: ( '\\r' )?
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 13) :
                alt11 = 1
            if alt11 == 1:
                # /Users/taka/works/github/sotsuron/LTLMP.g:57:10: '\\r'
                pass 
                self.match(13)




            self.match(10)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /Users/taka/works/github/sotsuron/LTLMP.g:58:4: ( ( ' ' | '\\t' | '\\n' | '\\r' ) )
            # /Users/taka/works/github/sotsuron/LTLMP.g:58:5: ( ' ' | '\\t' | '\\n' | '\\r' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            self.skip()
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # /Users/taka/works/github/sotsuron/LTLMP.g:1:8: ( T__20 | T__21 | T__22 | T__23 | T__24 | MP | TERM | DIGITS | INEQ | IMP | PROP | AND | OR | UNTIL | WUNTIL | NOT | NEXT | GLOBAL | FINAL | NEWLINE | WS )
        alt12 = 21
        LA12 = self.input.LA(1)
        if LA12 == 40:
            alt12 = 1
        elif LA12 == 41:
            alt12 = 2
        elif LA12 == 42:
            alt12 = 3
        elif LA12 == 43:
            alt12 = 4
        elif LA12 == 45:
            LA12_5 = self.input.LA(2)

            if (LA12_5 == 62) :
                alt12 = 10
            else:
                alt12 = 5

        elif LA12 == 77:
            alt12 = 6
        elif LA12 == 84:
            alt12 = 7
        elif LA12 == 48 or LA12 == 49 or LA12 == 50 or LA12 == 51 or LA12 == 52 or LA12 == 53 or LA12 == 54 or LA12 == 55 or LA12 == 56 or LA12 == 57:
            alt12 = 8
        elif LA12 == 62:
            alt12 = 9
        elif LA12 == 60:
            LA12_10 = self.input.LA(2)

            if (LA12_10 == 62) :
                alt12 = 19
            else:
                alt12 = 9

        elif LA12 == 97 or LA12 == 98 or LA12 == 99 or LA12 == 100 or LA12 == 101 or LA12 == 102 or LA12 == 103 or LA12 == 104 or LA12 == 105 or LA12 == 106 or LA12 == 107 or LA12 == 108 or LA12 == 109 or LA12 == 110 or LA12 == 111 or LA12 == 112 or LA12 == 113 or LA12 == 114 or LA12 == 115 or LA12 == 116 or LA12 == 117 or LA12 == 118 or LA12 == 119 or LA12 == 120 or LA12 == 121 or LA12 == 122:
            alt12 = 11
        elif LA12 == 38 or LA12 == 65:
            alt12 = 12
        elif LA12 == 79:
            LA12_13 = self.input.LA(2)

            if (LA12_13 == 82) :
                alt12 = 13
            else:
                alt12 = 17

        elif LA12 == 124:
            alt12 = 13
        elif LA12 == 85:
            alt12 = 14
        elif LA12 == 86:
            alt12 = 15
        elif LA12 == 33 or LA12 == 78:
            alt12 = 16
        elif LA12 == 88:
            alt12 = 17
        elif LA12 == 71 or LA12 == 91:
            alt12 = 18
        elif LA12 == 70:
            alt12 = 19
        elif LA12 == 13:
            LA12_21 = self.input.LA(2)

            if (LA12_21 == 10) :
                alt12 = 20
            else:
                alt12 = 21

        elif LA12 == 10:
            alt12 = 20
        elif LA12 == 9 or LA12 == 32:
            alt12 = 21
        else:
            nvae = NoViableAltException("", 12, 0, self.input)

            raise nvae


        if alt12 == 1:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:10: T__20
            pass 
            self.mT__20()



        elif alt12 == 2:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:16: T__21
            pass 
            self.mT__21()



        elif alt12 == 3:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:22: T__22
            pass 
            self.mT__22()



        elif alt12 == 4:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:28: T__23
            pass 
            self.mT__23()



        elif alt12 == 5:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:34: T__24
            pass 
            self.mT__24()



        elif alt12 == 6:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:40: MP
            pass 
            self.mMP()



        elif alt12 == 7:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:43: TERM
            pass 
            self.mTERM()



        elif alt12 == 8:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:48: DIGITS
            pass 
            self.mDIGITS()



        elif alt12 == 9:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:55: INEQ
            pass 
            self.mINEQ()



        elif alt12 == 10:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:60: IMP
            pass 
            self.mIMP()



        elif alt12 == 11:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:64: PROP
            pass 
            self.mPROP()



        elif alt12 == 12:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:69: AND
            pass 
            self.mAND()



        elif alt12 == 13:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:73: OR
            pass 
            self.mOR()



        elif alt12 == 14:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:76: UNTIL
            pass 
            self.mUNTIL()



        elif alt12 == 15:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:82: WUNTIL
            pass 
            self.mWUNTIL()



        elif alt12 == 16:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:89: NOT
            pass 
            self.mNOT()



        elif alt12 == 17:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:93: NEXT
            pass 
            self.mNEXT()



        elif alt12 == 18:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:98: GLOBAL
            pass 
            self.mGLOBAL()



        elif alt12 == 19:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:105: FINAL
            pass 
            self.mFINAL()



        elif alt12 == 20:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:111: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt12 == 21:
            # /Users/taka/works/github/sotsuron/LTLMP.g:1:119: WS
            pass 
            self.mWS()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(LTLMPLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
