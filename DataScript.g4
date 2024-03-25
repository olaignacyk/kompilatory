grammar DataScript;

program: statement+ EOF;

statement: loadDataStatement
         | displayDataStatement
         | splitDataStatement
         | linearRegressionStatement
         | modelEvaluationStatement
         | meanStatement
         | pointPlotStatement
         ;

loadDataStatement: 'wczytaj_dane' '(' STRING ')' ';';
displayDataStatement: 'wyswietl' STRING (',' STRING)* ';';
splitDataStatement: 'podzial_danych' '(' STRING ',' NUMBER ')' ';';
linearRegressionStatement: 'regresja_liniowa' '(' STRING ',' STRING ')' ';';
modelEvaluationStatement: 'ocena_modelu' '(' STRING ',' STRING ')' ';';
meanStatement: 'srednia' '(' STRING ')' ';';
pointPlotStatement: 'wykres_punktowy' '(' STRING ',' STRING ',' STRING ')' ';';

STRING: '"' ~["]* '"';

NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
