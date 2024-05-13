### ChinesePyPlus

## 1.Zalozenie projektu:
- Ogólne cele: Stworzenie języka programowania w języku chińskim, który jednocześnie swoją składnią poprawia trudności które sprawia programistom składnia Pythona. 
- Rodzaj translatora: Kompilator
- Planowany wynik działania programu: Kompilator ChinesePyPlus do języka Python (wynik w postaci pliku .py)
- Planowany język implementacji: Python
- Sposób implementacji skanera/parsera: Użycie generatora ANTLR


## 2. Tokeny 
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



## 3. Gramatyka:
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
    TKN_FUNCTION TKN_VAR_ID TKN_LBRACKET fullArgList TKN_RBRACKET TKN_DOTS code TKN_RETURN value TKN_END_LINE TKN_END |
    TKN_FUNCTION TKN_VAR_ID TKN_LBRACKET fullArgList TKN_RBRACKET TKN_DOTS code TKN_END;

functionCall:
    TKN_VAR_ID TKN_LBRACKET fullValueList TKN_RBRACKET;

expression:
    varDeclaration | varAssignment | printExpression | forLoopExpression | whileLoopExpression |
    conditionalExpression TKN_END | functionCall | functionDeclaration | TKN_RETURN value;

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
    arithmeticExpression (TKN_MUL | TKN_DIV) arithmeticExpression |
    arithmeticExpression (TKN_MINUS | TKN_PLUS) arithmeticExpression |
    TKN_NUMBER_VAL | TKN_VAR_ID | functionCall;

printExpression:
    TKN_PRINT value | TKN_PRINT TKN_LBRACKET value TKN_RBRACKET;

forLoopExpression:
    TKN_FOR TKN_VAR_ID TKN_FROM arithmeticExpression TKN_TO arithmeticExpression TKN_DOTS loopCode TKN_END;

whileLoopExpression:
    TKN_WHILE booleanExpression TKN_DOTS loopCode TKN_END;

conditionalExpression:
    TKN_IF booleanExpression TKN_DOTS (code|loopCode) |  TKN_IF booleanExpression TKN_DOTS (code|loopCode) elifExpression elseExpression |
    TKN_IF booleanExpression TKN_DOTS (code|loopCode) elifExpression | TKN_IF booleanExpression TKN_DOTS (code|loopCode) elseExpression;

elifExpression:
    TKN_ELIF booleanExpression TKN_DOTS (code|loopCode) | elifExpression TKN_ELIF booleanExpression TKN_DOTS (code|loopCode);

elseExpression:
    TKN_ELSE TKN_DOTS (loopCode|code);

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









## 4. Opis i schemat struktury programu:
-  Kod źródłowy jest wczytywany z pliku.
- Przechodzi przez skaner, który przekształca go na tokeny.
- Następnie tokeny są analizowane przez parser, który przyporządkowuje je do odpowiednich konstrukcji gramatycznych.
- Na podstawie parsowania, generowane są odpowiednie instrukcje w języku Python.
- Implementacja w języku Python obejmuje również klasę Listenera, która przetwarza drzewo parsowania i generuje kod w języku Python.

 ## 5. Informacje o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych
ANTLR to generator parserów do czytania, przetwarzania, wykonywania lub tłumaczenia tekstu strukturalnego lub plików binarnych. Jest szeroko stosowany do tworzenia języków, narzędzi i frameworków. Na podstawie gramatyki, ANTLR generuje parser, który może budować i przechodzić przez drzewa parsowania.

##Informacje o zastosowaniu specyficznych metod rozwiązania problemu: 
ChinesePyPlus to język programowania stworzony z myślą o naszych bratach z Chin których język jest bardzo trudny lecz chciałyśmy docenić jego piękno. Język ten ułatwia pisanie kodu, którego słowa kluczowe są w języku chińskim. 

## 6. Informacje o zastosowaniu specyficznych metod rozwiązania problemu: 
Język, który stworzyliśmy na potrzeby tego projektu jest językiem ułatwiającym naukę programowania. Poprzez zdefiniowanie słów kluczowych w języku chinskim młodsze osoby nie mają problemu ze zrozumieniem koncepcji ich działania. To rozwiązanie pozwoli dzieciom oswajać się z programowaniem już od najmłodszych lat.


## 7. Krótka instrukcja obsługi:
Na początku musimy pobrać kompletny plik JAR ANTLR. Po stworzeniu pliku .g4 składającego się z opisanych tokenów i gramatyki należy go skompilować w użyciem pobranego wcześniej JAR'a ANTLR. Używamy polecenia:

```java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 ChinesePyPlus.g4```
Aby użyć wygenerowanego pliku Pythona, potrzebujemy naszej własnej klasy Listenera, która dziedziczy z wygenerowanego wcześniej Listenera (jest on nowym elementem projektu ANTLR 4 i został zaprojektowany, aby ułatwić pisanie kodu, który obsługuje zdarzenia z parsera, bez wpływu na zmianę gramatyki i ponownej kompilacji). Po stworzeniu takowej klasy możemy użyć naszego programu. Aby tego dokonać tworzymy prosty skrypt zamieszczony poniżej.
 ```
 def translate(input_file, output_file):

    input_stream = FileStream(input_file, encoding='utf-8')

    lexer = ChinesePyPlusLexer.ChinesePyPlusLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ChinesePyPlusParser.ChinesePyPlusParser(stream)

    tree = parser.program()

    parse_tree_walker = ParseTreeWalker()
    listener = ChinesePyPlusImpl.ChinesePyPlusImpl()

    parse_tree_walker.walk(listener, tree)

    file = open(output_file, "w+", encoding='utf-8')
    file.write(listener.code)
    file.close()


path = str(sys.argv[1])
target = str(sys.argv[2])
translate(path, target)
```

Kompilator uruchamiamy z konsoli z użyciem polecenia:
```python translator.py <plik w języku ChinesePyPlus (.txt)> <plik wyjściowy (.py)>```
Otrzymujemy plik wyjściowy w języku Python, który możemy w dowolny sposób uruchomić.

Dodatkowo został stworzony interfejs graficzny. Uruchamiamy go z konsoli z uzyciem polecenia:
``` python interface.py``` . 
Na ekarnie pojawia się interfejs gdzie widoczne są dwa okienka. 
W lewym oknie wpisujemy kod w języku ChinesePyPlus i po naciśnięciu przycisku "TRANSLATE" w prawym oknie pojawia się kod w języku Python. 


## Przykładowy kod:
```
數位 lista <- [1,2,4,5];
數位 indeks <- 0;
列印(indeks);

儘管 indeks<=10:
    indeks <- indeks+1;
    如果 indeks = 4:
        列印("Jestem 4");
    的:
        列印(indeks);
      結尾;  
結尾;
```

W pythonie ten kod:
```	
lista = [1, 2, 4, 5]
indeks = 0
print(indeks)
while indeks <= 10:
	indeks = indeks + 1
	if indeks == 4:
		print("Jestem 4")
	else:
		print(indeks)	
```
Przyklad z pętlami i funkcją.
```
# Wyliczanie ciagu fibonacciego

功能 fibonacci(數位 liczba):
    如果 liczba = 1:
        返回 0;
    否則 liczba = 2:
        返回 1;  
    的:
        a <- 0;
        b <- 1;
        給 indeks 打 2 遏 liczba:
            wynik <- a + b;
            a <- b;
            b <- a + b;
        結尾;
    返回 wynik;
    結尾;
結尾;

給 indeks 打 2 遏 10:
    如果 indeks < 7:
        列印(fibonacci(indeks));
    否則 indeks = 9:
        休息;
    的:
        列印(indeks);
        繼續;
    結尾;
結尾;
```
Po skompilowaniu:
```
# Wyliczanie ciagu fibonacciego

def fibonacci(liczba):
	if liczba == 1:
		return 0
	elif liczba == 2:
		return 1
	else:
		a = 0
		b = 1
		for indeks in range(2, liczba):
			wynik = a + b
			a = b
			b = a + b
			
		return wynik
		
	
for indeks in range(2, 10):
	if indeks < 7:
		print(fibonacci(indeks))
	elif indeks == 9:
		break
	else:
		print(indeks)
		continue
```