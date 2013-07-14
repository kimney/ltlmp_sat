grammar LTLMP;

options{
	output = AST;
	ASTLabelType = CommonTree;
	language=Python;
	}
tokens{
	// tokens which appears only in AST
	// NOTE: u can use LexerRuleName as Token in AST
	}
	
//ast constructuin debugging need coldreboot for correctly labeled AST

//TODO: skip WhiteSpase


start	:stmt (NEWLINE!)* /*{print $stmt.tree.toStringtree();}*/;
stmt	:andstmt (OR^ andstmt)*;
andstmt	:binarystmt (AND^ binarystmt)*;
binarystmt:unarystmt ((UNTIL|WUNTIL|IMP)^ unarystmt)*;
// note: GFN and X meaning analysis  not for this section?
unarystmt:
	FINAL unarystmt -> ^(FINAL unarystmt)
	|GLOBAL unarystmt -> ^(GLOBAL unarystmt)
	|NOT unarystmt -> ^(NOT unarystmt) 
	|NEXT unarystmt -> ^(NEXT unarystmt)
	|prop;
prop	:PROP^
	|MP'('mpexpr')' INEQ DIGITS -> ^(MP ^(INEQ ^(DIGITS mpexpr)))
	|'('!stmt')'!
	;
	
mpexpr	:mpprod ('-'^ mpprod | '+'^ mpprod)*;	
mpprod	:mpterm ('*'^ mpterm)*;
mpterm 	:TERM '('stmt')' -> ^(TERM stmt)
	|'('!mpexpr')'!
	|DIGITS
	;

MP	:'MP^'|'MP_';
TERM	:'T';
DIGITS	:'1'..'9' '0'..'9'*| '0';
INEQ	:'>'|'>='|'<'|'<=';

IMP	:'->';
PROP	:'a'..'z' ('0'..'9'|'a'..'z'|'_')*;
AND	:'AND'|'&&'|'&';
OR	:'OR'|'||'|'|';
UNTIL	:'U';
WUNTIL	:'V';
NOT 	:'!'|'NOT';
NEXT 	:'X'|'O';
GLOBAL 	:'G'|'[]';
FINAL 	:'F'|'<>';

NEWLINE	:'\r'? '\n';
WS	:(' '|'\t'|'\n'|'\r'){self.skip()} ;//{self.skip()};