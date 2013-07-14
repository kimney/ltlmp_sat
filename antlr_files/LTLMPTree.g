tree grammar LTLMPTree;

options{
	tokenVocab = LTLMP;
	ASTLabelType = CommonTree;
	language=Python;
	}
//@members{ void print(String s){ print s}}
@header {
from tree_ltlmp import tree as maketree
}
@init {self.memory = {}}

prog	:
	{print " ---- Tree parsing prog ----"}
	stat+ //{$tree = $stat.tree}
	{print " ---- End Treeparsing ----"}
	;
	
stat	:
	expr
	{print 'EXPR!'}	
	;
	
expr returns [value]
	:^(OR ax=expr bx=expr)
{$value = maketree('OR')
$value.child.append(ax)
$value.child.append(bx)}

	|^(AND cx=expr dx=expr)
{$value = maketree('AND')
$value.child.append(cx)
$value.child.append(dx)}

	|^(IMP cx=expr dx=expr)
{$value = maketree('IMP')
$value.child.append(cx)
$value.child.append(dx)}

	|^(NEXT x=expr)
{$value = maketree('X')
$value.child.append(x)}

	|^(UNTIL ax=expr bx=expr)
{$value = maketree('U')
$value.child.append(ax)
$value.child.append(bx)}

	|^(WUNTIL ax=expr bx=expr)
{$value = maketree('V')
$value.child.append(ax)
$value.child.append(bx)}

	|^(FINAL x=expr)
{$value = maketree('F')
$value.child.append(x)}

	|^(GLOBAL x=expr)
{$value = maketree('G')
$value.child.append(x)}

	|^(NOT x=expr)
{$value = maketree('NOT')
$value.child.append(x)}

	|^(MP mpineq)
{$value = maketree($MP.toString())
$value.ineq = $mpineq.ineq
$value.const = $mpineq.const
$value.child.append($mpineq.value)}

	|^(TERM x=expr)
{$value = maketree('TERM')
$value.child.append(x)}

	|^('*' ax=expr bx=expr)
{$value = maketree('*')
$value.child.append(ax)
$value.child.append(bx)}
	|^('+' ax=expr bx=expr)
{$value = maketree('+')
$value.child.append(ax)
$value.child.append(bx)}
	|^('-' ax=expr bx=expr)
{$value = maketree('-')
$value.child.append(ax)
$value.child.append(bx)}

	|DIGITS
{$value = maketree($DIGITS.toString())
#print ' digits(leaf): '+ $DIGITS.toString()
}
	|PROP
{$value = maketree($PROP.toString())
#print ' prop: '+$PROP.toString()
}
;

//not so good but it works	
mpineq returns [ineq, const, value]
	:^(str=INEQ mpconst)
{$ineq = str.toString()
$const = $mpconst.const
$value = $mpconst.value};

mpconst	returns [const, value]
	:^(DIGITS x=expr)
{$const = $DIGITS.getText()
$value = x};

//digits	:'1'..'9' '0'..'9'*| '0';
//prop	:'>'|'>='|'<'|'<=';
/*
MP	:'MP';
TERM	:'T';
DIGITS	:'1'..'9' '0'..'9'*| '0';
INEQ	:'>'|'>='|'<'|'<=';

PROP	:'a'..'z' ('0'..'9'|'a'..'z'|'_')*;
AND	:'AND'|'&&'|'&';
OR	:'OR'|'||'|'|';
UNTIL	:'U';
NOT 	:'!'|'NOT';
NEXT 	:'X'|'O';
GLOBAL 	:'G'|'[]';
FINAL 	:'F'|'<>';

NEWLINE	:'\r'? '\n';
WS	:(' '|'\t'|'\n'|'\r')+ {self.skip()} ;
*/