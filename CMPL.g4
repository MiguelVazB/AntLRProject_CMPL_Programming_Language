grammar CMPL;

prog: stmts* EOF;

stmts: stmt | if_scope | while_scope | show_stmt;

stmt: (variable_stmt | funct_call);

if_scope: 'if' expr scope ('else' else_if_scope)?;

else_if_scope: scope | if_scope;

while_scope: WHILE expr scope;

scope: '{' stmts* '}';

variable_stmt: var=VAR '=' exp=expr             #varStatement
             ;

funct_call: var=VAR '(' (expr (',' expr)*)? ')';

show_stmt: 'show(' expr? (PLUS_PLUS)? ')'          #showStatement
         ;

expr: data_type                                 #typeExpr
    | VAR                                       #varExpr
    | funct_call                                #functionCall
    | '(' expr* ')'                             #parensExpr
    | '!' expr                                  #negationExpr
    | left=expr op='^' right=expr               #infixExpr
    | left=expr op=('*'|'/') right=expr         #infixExpr
    | left=expr op=('+'|'-') right=expr         #infixExpr
    | left=expr op=comparison_op right=expr     #compareExpr
    | left=expr op=logic_op right=expr          #logicExpr
    ;

data_type: INT | FLOAT | STRING | BOOLEAN | NULL;

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
STRING: ('"' ~'"'* '"') | ('\'' ~'\''* '\'');
NULL: 'null';
BOOLEAN: 'true'|'false';
WHILE: 'until';
PLUS_PLUS: '++';
VAR : [a-zA-Z]+ ;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);
