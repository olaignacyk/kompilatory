### ChinesePyPlus

## Zalozenie projektu:
- Ogólne cele: Stworzenie języka programowania w języku chińskim, który jednocześnie swoją składnią poprawia trudności które sprawia programistom składnia Pythona. 
- Rodzaj translatora: Kompilator
- Planowany wynik działania programu: Kompilator ChinesePyPlus do języka Python (wynik w postaci pliku .py)
- Planowany język implementacji: Python
- Sposób implementacji skanera/parsera: Użycie generatora ANTLR


## Przykładowy kod:
#deklaracja listy

	列舉 測試 <- [1,2,4,5]
	
	數位  指數 <= 0

	儘管 指數 < 10{
	
	如果  指數 = 4{
		列印(„我是 4”)

	}
	否則 指數=9{
		列印(„我是 9”)
		}

	的{
		列印(指數)
		}
	指數<-指數+1
	} :)

W pythonie ten kod:
	
	list=[1,2,4,5]
	idx=0
	while idx<10:
		if idx==4:
 			print("numer 4")
   		elif idx==9:
    			print("numer 9")
      		else:
       			print(idx)
	 	idx+=1




## Tokeny 
- TKN_END_LINE            :(';');
- TKN_NUMBER              :('數位');
- TKN_STRING              :('串');
- TKN_BOOL                :('對或錯');
- TKN_LIST                :('列舉');
- TKN_IF                  :('如果');
- TKN_ELSE                :('的');
- TKN_ELIF                :('否則');
- TKN_FOR                 :('給');
- TKN_FROM                :('打');
- TKN_TO                  :('遏');
- TKN_WHILE               :('儘管');
- TKN_NOT                 :('不是');
- TKN_AND                 :('和');
- TKN_OR                  :('或者');
- TKN_FUNCTION            :('功能');
- TKN_RETURN              :('返回');
- TKN_PRINT               :('列印');
- TKN_TRUE                :('真的');
- TKN_FALSE               :('錯誤的');
- TKN_END                 :('結尾');
- TKN_BREAK               :('休息');
- TKN_CONTINUE            :('繼續');
- TKN_PLUS                :'+';
- TKN_MINUS               :'-';
- TKN_MUL                 :'*';
- TKN_DIV                 :'/';
- TKN_POW                 :'^';
- TKN_CONCAT              :'++';
- TKN_ASSIGN              :'<-';
- TKN_G                   :'>';
- TKN_L                   :'<';
- TKN_EQ                  :'=';
- TKN_GEQ                 :'>=';
- TKN_LEQ                 :'<=';
- TKN_NEQ                 :'/=';
- TKN_DOTS                :':';
- TKN_LBRACKET            :'(';
- TKN_RBRACKET            :')';
- TKN_LSQUARE             :'[';
- TKN_RSQUARE             :']';
- TKN_COMMA               :',';
- TKN_LFUNBRACKET         :'{';
- TKN_RFUNBRACKET         :'}';
- TKN_COMMENT             :([#][a-zA-Z_0-9 \t;]*[\n] | '#{'[a-zA-Z_0-9 \t\n;]*'}#');
- TKN_NUMBER_VAL          :[-]?[0-9]+([.][0-9]+)?;
- TKN_STRING_VAL          :'"'[a-zA-Z_0-9!? \t\n;]*'"';
- TKN_VAR_ID              :[a-zA-Z_][a-zA-Z0-9_]*;
- TKN_WHITESPACE          :(' ' | '\t' | '\n') -> skip;



## Gramatyka:
program:
    code EOF;

code:
    expression TKN_END_LINE |
    expression TKN_END_LINE code |
    TKN_COMMENT code;

var_type:
    TKN_NUMBER | TKN_STRING | TKN_BOOL | TKN_LIST;

varDeclaration:
    var_type TKN_VAR_ID TKN_ASSIGN value;

varAssignment:
    TKN_VAR_ID TKN_ASSIGN value;

functionDeclaration:
    TKN_FUNCTION TKN_VAR_ID TKN_LBRACKET fullArgList TKN_RBRACKET TKN_LFUNBRACKET code TKN_RETURN value TKN_RFUNBRACKET;

functionCall:
    TKN_VAR_ID TKN_LBRACKET fullValueList TKN_RBRACKET;

expression:
    varDeclaration | varAssignment | printExpression | forLoopExpression | whileLoopExpression | conditionalExpression TKN_END | functionCall | functionDeclaration | TKN_RETURN value;
value:
    stringExpression | booleanExpression | arithmeticExpression | listExpression |TKN_VAR_ID | functionCall;

stringExpression:
    stringExpression TKN_CONCAT stringExpression | TKN_STRING_VAL | TKN_VAR_ID | TKN_LBRACKET stringExpression TKN_RBRACKET | functionCall;

booleanExpression:
    booleanExpression (TKN_AND | TKN_OR) booleanExpression | stringExpression (TKN_EQ | TKN_NEQ) stringExpression |
    arithmeticExpression (TKN_G | TKN_L | TKN_LEQ | TKN_GEQ | TKN_EQ | TKN_NEQ) arithmeticExpression | TKN_FALSE | TKN_TRUE |
    TKN_VAR_ID | TKN_NOT booleanExpression | TKN_LBRACKET booleanExpression TKN_RBRACKET | functionCall;

arithmeticExpression:
    TKN_LBRACKET arithmeticExpression TKN_RBRACKET |
    arithmeticExpression (TKN_MUL | TKN_DIV | TKN_MOD) arithmeticExpression |
    arithmeticExpression (TKN_MINUS | TKN_PLUS) arithmeticExpression |
    TKN_NUMBER_VAL | TKN_VAR_ID | functionCall;

printExpression:
    TKN_PRINT value | TKN_PRINT TKN_LBRACKET value TKN_RBRACKET;

forLoopExpression:
    TKN_FOR TKN_VAR_ID TKN_FROM arithmeticExpression TKN_TO arithmeticExpression TKN_LFUNBRACKET loopCode TKN_RFUNBRACKET;

whileLoopExpression:
    TKN_WHILE booleanExpression TKN_DOTS loopCode TKN_END;

conditionalExpression:
    TKN_IF booleanExpression TKN_LFUNBRACKET (code|loopCode) TKN_RFUNBRACKET|  TKN_IF booleanExpression TKN_LFUNBRACKET (code|loopCode)TKN_RFUNBRACKET elifExpression elseExpression |
    TKN_IF booleanExpression TKN_LFUNBRACKET (code|loopCode) TKN_RFUNBRACKET elifExpression | TKN_IF booleanExpression TKN_LFUNBRACKET (code|loopCode) TKN_RFUNBRACKET elseExpression;

elifExpression:
    TKN_ELIF booleanExpression TKN_LFUNBRACKET (code|loopCode) TKN_RFUNBRACKET | elifExpression TKN_ELIF booleanExpression TKN_LFUNBRACKET (code|loopCode)TKN_RFUNBRACKET;

elseExpression:
    TKN_ELSE TKN_LFUNBRACKET (loopCode|code) TKN_RFUNBRACKET;

listExpression:
    listValue | listExpression TKN_CONCAT listValue;

listValue:
    TKN_LSQUARE valueList TKN_RSQUARE;

valueList:
    value | valueList TKN_COMMA value;

fullValueList:
    TKN_WHITESPACE | valueList;

argList:
    var_type TKN_VAR_ID | argList TKN_COMMA var_type TKN_VAR_ID;

fullArgList:
    TKN_WHITESPACE | argList;

loopCode:
    code | loopCode (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE loopCode |
    loopCode (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE |
    (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE loopCode | (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE;



## Opis i schemat struktury programu:
- Kod źródłowy jest wczytywany z pliku.
- Przechodzi przez skaner, który przekształca go na tokeny.
- Następnie tokeny są analizowane przez parser, który przyporządkowuje je do odpowiednich konstrukcji gramatycznych.
- Na podstawie parsowania, generowane są odpowiednie instrukcje w języku Python.
- Implementacja w języku Python obejmuje również klasę Listenera, która przetwarza drzewo parsowania i generuje kod w języku Python.

 ## Informacje o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych
ANTLR to generator parserów do czytania, przetwarzania, wykonywania lub tłumaczenia tekstu strukturalnego lub plików binarnych. Jest szeroko stosowany do tworzenia języków, narzędzi i frameworków. Na podstawie gramatyki, ANTLR generuje parser, który może budować i przechodzić przez drzewa parsowania.

##Informacje o zastosowaniu specyficznych metod rozwiązania problemu: 
ChinesePyPlus to język programowania stworzony z myślą o naszych bratach z Chin których język jest bardzo trudny lecz chciałyśmy docenić jego piękno. Język ten ułatwia pisanie kodu, którego słowa kluczowe są w języku chińskim. 



