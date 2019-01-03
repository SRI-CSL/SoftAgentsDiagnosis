grammar Deviation;

/*

    Events, Constraints and Timelines


*/



unit : fact+ ;

fact: constraint
      | event
      | timeline
      | invariant
      ;

constraint: term ID term
            | LPAREN term ID term RPAREN
            ;

event:  LPAREN expression '@' timestamp RPAREN
        |  expression '@' timestamp
        ;

timeline: TIMELINE LPAREN term ',' varlist RPAREN ;


invariant:  event IMPLIES constraint ;


expression: ID LPAREN termlist RPAREN;

term:   INTEGER
        | NOLOC
        | variable
        | ID LPAREN termlist RPAREN
        | term INFIX term
        | LPAREN term INFIX term RPAREN
        ;

termlist: term ( ',' term )* ;


timestamp:  INTEGER
            | variable;

variable: ID ':' vartype ;

varlist: variable ( ',' variable )* ;

vartype: ID ;


/*

    Configuration Settings


*/


configuration: setting+ ;

setting: ID LPAREN INTEGER RPAREN ;


LPAREN : '(' ;

RPAREN : ')' ;

INFIX : '-' | '+' | '*' ;

NOLOC       :  'noLoc' ;

TIMELINE    : 'timeline' ;

IMPLIES     : '=>' ;

ID  :   LETTER (LETTER | DIGIT)* ;

INTEGER     :   DIGIT+ ;

fragment
DIGIT       :   [0-9] ;

STRING      :   '"' (ESCAPE|.)*? '"' ;
fragment
ESCAPE      :   '\\"' | '\\\\'  ;

fragment
LETTER      :   [a-zA-Z\u0080-\u00FF_!=<>/] ;

LINE_COMMENT : '%' .*? '\r'? '\n'  -> skip ;

WHITE_SPACE: [ \t\r\n]+ -> skip ;
