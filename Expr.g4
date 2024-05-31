grammar Expr;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
IF : 'if' ;
DEF : 'def' ;
EQ : '=' ;
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;

int_type: 'int';
float_type: 'float';

type
    : int_type
    | float_type
;


INT : [0-9]+ ;
FLOAT : [0-9]+[.][0-9]+;

WS: [ \t\n\r\f]+ -> skip ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;

program: statment* EOF;

statment: ifstat
    | funcstat
    | expr ';'
    | asingment ';'
    | declaration ';'
    | 'return' expr ';' 
    ;
    
    
ifstat: IF '(' expr ')' LCURLY statment* RCURLY ;

id : ID;
int: INT;
float: FLOAT;


funcstat : 
    DEF id '(' id (',' id)* ')' LCURLY statment* RCURLY
;

expr: id
    | func
    | expr '==' expr 
    | expr 'or' expr
    | expr '*' expr 
    | expr '/' expr 
    | expr '+' expr 
    | expr '-' expr 
    | 'not' expr
    | expr 'and' expr
    | int
    | float
    ;

declaration: id ':' type '=' expr ;
asingment: id '=' expr ;

func : id '(' expr (',' expr)* ')';