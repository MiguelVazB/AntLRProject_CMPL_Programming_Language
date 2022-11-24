grammar CMPL;

prog: stmts* EOF;

stmts: stmt | if_scope | while_scope;

stmt: (variable_stmt | funct_call | expr | show_stmt) NEWLINE*;

if_scope: 'if' expr scope ('else' else_if_scope)?;

else_if_scope: scope | if_scope;

while_scope: WHILE expr scope;

scope: NEWLINE* '{' NEWLINE* stmts* NEWLINE* '}' NEWLINE*;

variable_stmt: var=VAR '=' exp=expr           #varStatement
             ;

funct_call: var=VAR '(' (expr (',' expr)*)? ')';

show_stmt: 'show(' expr plus_plus_minus_minus? ')'   #showStatement
         ;

expr: data_type                                 #typeExpr
    | VAR plus_plus_minus_minus?                #varExpr
    | funct_call                                #functionCall
    | '(' expr ')'                             #parensExpr
    | '!' expr                                  #negationExpr
    | left=expr op='^' right=expr               #infixExpr
    | left=expr op=('*'|'/') right=expr         #infixExpr
    | left=expr op=('+'|'-') right=expr         #infixExpr
    | left=expr op=comparison_op right=expr     #compareExpr
    | left=expr op=logic_op right=expr          #logicExpr
    ;

plus_plus_minus_minus: PLUS_PLUS | MINUS_MINUS ;

data_type: INT | FLOAT | BOOLEAN | STRING | NULL;

comparison_op: 'equals'
             | 'not equals'
             | 'greater'
             | 'smaller'
             | 'greater or equal'
             | 'smaller or equal'
             ;

logic_op: 'and' | 'or';

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_POW: '^';

FLOAT: [0-9]+ '.' [0-9]+;
BOOLEAN: 'true'|'false';
STRING: ('"' ~'"'* '"') | ('\'' ~'\''* '\'');
NULL: 'null';
WHILE: 'while';
PLUS_PLUS: '++';
MINUS_MINUS: '--';
VAR : [a-zA-Z]+ ;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);
