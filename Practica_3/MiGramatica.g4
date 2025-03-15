grammar MiGramatica;

programa: sentencia (';' sentencia)* EOF; 
sentencia: forStmt | asignacion;

forStmt: 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' (sentencia (';')?)* '}';

inicializacion: ID '=' expresion;
condicion: ID ('>' | '<' | '==' | '!=') expresion; // Se usa expresion para más flexibilidad
actualizacion: ID '=' expresion;

asignacion: ID '=' expresion ';';

// Expresiones con jerarquía de operaciones
expresion
    : expresion ('*' | '/') expresion   # MulDiv
    | expresion ('+' | '-') expresion   # AddSub
    | '(' expresion ')'                 # Parens
    | ID                                # Variable
    | INT                               # Numero
    ;

// Tokens
ID: [a-zA-Z]+;
INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;

