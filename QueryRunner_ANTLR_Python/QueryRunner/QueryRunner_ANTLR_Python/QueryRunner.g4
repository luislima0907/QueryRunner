grammar QueryRunner;

options { caseInsensitive = true; }

consulta
    : declaracionLectura EOF
    ;

declaracionLectura
    : LEER origen EXTRAER columnas
      (DONDE expresion)?
      (ORDENAR POR listaIds orden?)?
      (HASTA valor)?
      (COMBINAR origen EN listaIds)?
    ;

origen
    : identificador
    | STRING
    ;

columnas
    : ASTERISCO
    | listaIds
    ;

listaIds
    : identificador (COMA identificador)*
    ;

expresion
    : comparacion ((Y | O) comparacion)*
    ;

comparacion
    : valor operadorComparacion valor
    ;

operadorComparacion
    : IGUAL
    | DIFERENTE
    | MAYOR_IGUAL
    | MENOR_IGUAL
    | MAYOR
    | MENOR
    ;

valor
    : identificador
    | STRING
    | NUMERO
    ;

orden
    : ASCENDENTE
    | DESCENDENTE
    ;

identificador
    : IDENTIFICADOR
    ;


LEER : 'LEER';
EXTRAER : 'EXTRAER';
DONDE : 'DONDE';
ORDENAR : 'ORDENAR';
POR : 'POR';
HASTA : 'HASTA';
COMBINAR : 'COMBINAR';
EN : 'EN';
Y : 'Y';
O : 'O';
ASCENDENTE : 'ASCENDENTE';
DESCENDENTE : 'DESCENDENTE';

MAYOR_IGUAL : '>=';
MENOR_IGUAL : '<=';
DIFERENTE : '!=' | '<>';
IGUAL : '=';
MAYOR : '>';
MENOR : '<';
ASTERISCO : '*';
COMA : ',';

STRING
    : '"' (~["\r\n\\] | '\\' .)* '"'
    | '\'' (~['\r\n\\] | '\\' .)* '\''
    ;

NUMERO
    : DIGITO+ ('.' DIGITO+)?
    ;

IDENTIFICADOR
    : (LETRA | '_') (LETRA | DIGITO | '_' | '.')*
    ;

fragment LETRA
    : [a-zA-Z]
    ;

fragment DIGITO
    : [0-9]
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

COMENTARIO_LINEA
    : '--' ~[\r\n]* -> skip
    ;

COMENTARIO_BLOQUE
    : '/*' .*? '*/' -> skip
    ;