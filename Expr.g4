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


INT : [0-9]+ ;

WS: [ \t\n\r\f]+ -> skip ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;

program: statment* EOF;

statment: ifstat
    | funcstat
    | expr ';'
    | 'return' expr ';' 
    ;
    
    
ifstat: IF '(' expr ')' LCURLY statment* RCURLY ;

funcstat : 
    DEF ID '(' ID (',' ID)* ')' LCURLY statment* RCURLY
;

expr: ID
    | func
    | expr '==' expr 
    | expr 'or' expr
    | ID '=' expr
    | expr '+' expr 
    | expr '-' expr 
    | 'not' expr
    | expr 'and' expr
    | INT
    ;

func : ID '(' expr (',' expr)* ')';