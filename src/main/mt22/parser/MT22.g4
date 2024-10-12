/* ID: 2212878 */
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}


//!----------------LEXER_STRUCTURE-------------------//

/* KEYWORDS */
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

/* OPERATORS */
ADDITION: '+';
SUBTRACTION: '-';
MULTIPLICATION: '*';
DIVISION: '/';
MODULO: '%';
BOOLEANNOT: '!';
BOOLEANAND: '&&';
BOOLEANOR: '||';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHAN: '<';
LESSTHANOREQUAL: '<=';
GREATERTHAN: '>';
GREATERTHANOREQUAL: '>=';
STRINGCONCATENATION: '::';
ASSIGN: '=';

/* SEPERATORS */
LB: '(';
RB: ')';
LS: '[';
RS: ']';
POI: '.';
COMMA: ',';
SEMI_COLON: ';';
COLON: ':';
LP: '{';
RP: '}';

/* LITERAL */
literal: INTEGER_LIT
			| FLOAT_LIT
			| BOOLEAN_LIT
			| STRING_LIT 
			| arraylit;

/* INT_LITERAL */
INTEGER_LIT: INT_LIT {self.text = self.text.replace("_","")};
fragment INT_LIT: ('0' | [1-9] DIGIT* ('_' DIGIT+)*);

/* FLOAT LITERAL */
FLOAT_LIT: INTPART DECPART EXPONENTPART {self.text = self.text.replace("_","")}
					| INTPART DECPART {self.text = self.text.replace("_","")}
					| INTPART EXPONENTPART {self.text = self.text.replace("_","")}
					| DECPART EXPONENTPART {self.text = self.text.replace("_","")};

fragment INTPART: ('0' | [1-9] DIGIT* ('_' DIGIT+)*);
fragment DECPART: '.' [0-9]*;
fragment EXPONENTPART: [eE][+-]? DIGIT+;
fragment DIGIT: [0-9];

/* BOOLEAN_LIT */
BOOLEAN_LIT: 'true'
				| 'false';


/* STRING_LITERAL */
STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};
fragment STR_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\"' | '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\';
fragment ESCAPE_ILLEGAL: '\\' ~[bfrnt'\\] | '\'' ~'"';

/* ARRAY_LIT */
arraylit: LP exprlist RP;
exprlist: expr_prime | ;
expr_prime: expr COMMA expr_prime | expr;

/* IDENTIFIERS */
IDEN: [a-zA-Z_][a-zA-Z0-9_]*;

/* SKIP COMMENT AND WS*/
COMMENTS: (('//' ~[\n]*) | ('/*' .*? '*/')) -> skip; // Comments
WS : [ \t\r\f\b\n]+ -> skip ; // skip spaces, tabs


/* CHECK */
ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* (EOF | '\n' | '\r\n'){
	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESCAPE_ILLEGAL {
	raise IllegalEscape(self.text[1:])
};

//!----------------SYNTAX_ANALYZER_STRUCTURE-------------------//
program: classDefinition EOF;
classDefinition:  declaration classDefinition | declaration;
declaration: globalVariableDec | functionDec;


/* VARIABLE_DECLARATIONS */
globalVariableDec: (shortform | fullform) SEMI_COLON;

shortform: identifier_list COLON primitive_type;
identifier_list: IDEN COMMA identifier_list | IDEN;

fullform: IDEN full_list expr;
full_list: COMMA IDEN full_list expr COMMA | COLON primitive_type ASSIGN;

parameter: INHERIT? OUT? IDEN COLON primitive_type;

/* FUNCTION_DECLARATIONS */
functionDec: function_prototype function_body;
function_prototype: IDEN COLON FUNCTION return_type LB parameter_list RB inheritancePart;
parameter_list: parameters | ;
parameters: parameter COMMA parameters | parameter;
inheritancePart: (INHERIT IDEN)? ;
function_body: block_statement;

/* INDEX_OPERATORS */
index_oper: IDEN LS expr_prime RS;

/* TYPE */
primitive_type: BOOLEAN
					| INTEGER
					| FLOAT
					| STRING
					| array_type
					| AUTO;

array_type: ARRAY LS dimensions RS OF element_type;
dimensions: INTEGER_LIT COMMA dimensions | INTEGER_LIT;
element_type: INTEGER | FLOAT | BOOLEAN | STRING; 

return_type: BOOLEAN
					| INTEGER
					| FLOAT
					| STRING
					| array_type
					| AUTO
					| VOID;


/* EXPRESSIONS */
expr: expr1 STRINGCONCATENATION expr1 | expr1;
expr1: expr2 (EQUAL | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSTHANOREQUAL | GREATERTHANOREQUAL) expr2 | expr2;
expr2: expr2 (BOOLEANAND | BOOLEANOR) expr3 | expr3;
expr3: expr3 (ADDITION | SUBTRACTION) expr4 | expr4;
expr4: expr4 (MULTIPLICATION | DIVISION | MODULO) expr5 | expr5;
expr5: BOOLEANNOT expr5 | expr6;
expr6: SUBTRACTION expr6 | expr7;
expr7: index_oper | expr8;
expr8: IDEN | literal | LB expr RB | IDEN LB exprlist RB;

/* STATEMENT */
statement: (assignment_statement 
			| if_statement
			| for_statement
			| while_statement
			| do_while_statement
			| break_statement
			| continue_statement 
			| return_statement
			| call_statement 
			| block_statement);

assignment_statement: lhs ASSIGN expr SEMI_COLON;
lhs: IDEN | index_oper;

if_statement: IF LB expr RB statement else_statement;
else_statement: ELSE statement | ;

for_statement: FOR LB lhs ASSIGN init_expr COMMA expr COMMA expr RB statement;
init_expr: init_expr (ADDITION | SUBTRACTION) init_expr1 | init_expr1;
init_expr1: init_expr1 (MULTIPLICATION | DIVISION | MODULO) init_expr2 | init_expr2;
init_expr2: SUBTRACTION init_expr2 | init_expr3;
init_expr3:  LB expr RB | INTEGER_LIT;

while_statement: WHILE LB expr RB statement;

do_while_statement: DO block_statement WHILE LB expr RB SEMI_COLON;

break_statement: BREAK SEMI_COLON;

continue_statement: CONTINUE SEMI_COLON;

return_statement: RETURN re_turn SEMI_COLON;
re_turn: expr | ;

call_statement: (special_func | function_call) SEMI_COLON;

block_statement: LP block_list RP;
block_list: statement block_list | tmp;
tmp: globalVariableDec block_list | ;

/* FUNCTION_CALL */
function_call: IDEN LB arguments_list RB;
arguments_list: argument | ;
argument: expr COMMA argument | expr;

/* SPECIAL FUNCTION */
special_func: readIn
				| printIn
				| readFloa
				| writeFloa
				| readBoo
				| printBoo
				| readStr
				| printStr
				| sup
				| preDefault;

readIn: READINT LB RB;
printIn: PRINTINT LB expr RB;
readFloa: READFLO LB RB;
writeFloa: WRITEFLO LB expr RB;
readBoo: READBOOL LB RB;
printBoo: PRINTBOOL LB expr RB;
readStr: READSTR LB RB;
printStr: PRINTSTR LB expr RB;
sup: SUPER LB exprlist RB;
preDefault: PREVENTDEFAULT LB RB;


READINT: 'readInteger';
PRINTINT: 'printInteger'; 
READFLO: 'readFloat';
WRITEFLO: 'writeFloat';
READBOOL: 'readBoolean';
PRINTBOOL: 'printBoolean';
READSTR: 'readString';
PRINTSTR: 'printString';
SUPER: 'super';
PREVENTDEFAULT: 'preventDefault';

