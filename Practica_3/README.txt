1) ¿Qué tokens se generan para la estructura for (i = 0; i < 10; i = i + 1) { x = x + i; }?
a) La opción correcta, ANTLR reconoce todos los tokens del for.

2) ¿Cómo se organiza la estructura for en el árbol de análisis sintáctico?
a) for es el nodo raíz, con inicialización, condición, actualización y cuerpo como nodos hijos.
 
3) ¿Qué ocurre si en la gramática se omiten los ; en la estructura for?
a) Da error de sintaxis porque los ; son necesarios en la gramática.

comandos:
antlr4 MiGramatica.g4
javac MiGramatica*.java

tokens:
echo "for (i = 0; i < 10; i = i + 1) { x = x + i; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tokens
[@0,0:2='for',<'for'>,1:0]
[@1,4:4='(',<'('>,1:4]
[@2,5:5='i',<ID>,1:5]
[@3,7:7='=',<'='>,1:7]
[@4,9:9='0',<INT>,1:9]
[@5,10:10=';',<';'>,1:10]
[@6,12:12='i',<ID>,1:12]
[@7,14:14='<',<'<'>,1:14]
[@8,16:17='10',<INT>,1:16]
[@9,18:18=';',<';'>,1:18]
[@10,20:20='i',<ID>,1:20]
[@11,22:22='=',<'='>,1:22]
[@12,24:24='i',<ID>,1:24]
[@13,26:26='+',<'+'>,1:26]
[@14,28:28='1',<INT>,1:28]
[@15,29:29=')',<')'>,1:29]
[@16,31:31='{',<'{'>,1:31]
[@17,33:33='x',<ID>,1:33]
[@18,35:35='=',<'='>,1:35]
[@19,37:37='x',<ID>,1:37]
[@20,39:39='+',<'+'>,1:39]
[@21,41:41='i',<ID>,1:41]
[@22,42:42=';',<';'>,1:42]
[@23,44:44='}',<'}'>,1:44]
[@24,46:45='<EOF>',<EOF>,2:0]

Arbol:
echo "for (i = 0; i < 10; i = i + 1) { x = x + i; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tree
(programa (sentencia (forStmt for ( (inicializacion i = (expresion 0)) ; (condicion i < (expresion 10)) ; (actualizacion i = (expresion (expresion i) + (expresion 1))) ) { (sentencia (asignacion x = (expresion (expresion x) + (expresion i)) ;)) })) <EOF>)