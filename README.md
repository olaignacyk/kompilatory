## DataScript

DataScript to język programowania stworzony z myślą o analizie danych, uczeniu maszynowym i przetwarzaniu danych. Jest zoptymalizowany pod kątem szybkiego i efektywnego manipulowania dużymi zbiorami danych, a także oferuje narzędzia do wizualizacji i eksploracji danych.

 ## Cechy języka:

- ** Prostota i czytelność kodu: Składnia DataScript jest zaprojektowana tak, aby być intuicyjną i czytelną dla użytkowników. Oparta jest na zrozumiałych dla człowieka konstrukcjach, co ułatwia pisanie, zrozumienie i utrzymanie kodu.
- ** Obsługa danych tabularnych: DataScript oferuje wbudowane mechanizmy do obsługi danych tabularnych, takich jak ramki danych (data frames). Umożliwia to łatwe wczytywanie, manipulowanie i przetwarzanie danych w formie tabelarycznej.
- ** Bogate biblioteki do analizy danych: Język ten zawiera bogate biblioteki do analizy danych, uczenia maszynowego i przetwarzania statystycznego. Obejmuje to operacje takie jak filtrowanie, grupowanie, agregacja, modelowanie i wizualizacja danych.
- ** Integracja z narzędziami do analizy danych: DataScript integruje się z popularnymi narzędziami i bibliotekami używanymi w analizie danych, takimi jak NumPy, Pandas, Matplotlib, TensorFlow, scikit-learn itp. Dzięki temu użytkownicy mogą wykorzystać istniejące rozwiązania i biblioteki w swoich projektach.
- ** Wsparcie dla przetwarzania równoległego i rozproszonego: DataScript oferuje mechanizmy do przetwarzania równoległego i rozproszonego, co pozwala efektywnie przetwarzać duże zbiory danych na wielu procesorach lub w klastrach komputerowych.
- ** Elastyczność i rozszerzalność: Język ten jest elastyczny i łatwo rozszerzalny. Użytkownicy mogą tworzyć własne funkcje i biblioteki do manipulacji danych, dostosowane do ich konkretnych potrzeb i wymagań.
- ** Wsparcie dla pracy interaktywnej: DataScript umożliwia pracę w trybie interaktywnym, co pozwala użytkownikom eksplorować dane, testować kod i tworzyć analizy w czasie rzeczywistym.

## Zalozenie projektu:
- **Ogólne cele: Stworzenie języka programowania, który ułatwi analizę i przetwarzanie danych, zwłaszcza w dziedzinie analizy danych, uczenia maszynowego i przetwarzania statystycznego.
- **Rodzaj translatora: Kompilator
- **Planowany wynik działania programu: Kompilator DataScript do języka Python (wynik w postaci pliku .py)
- **Planowany język implementacji: Python
- **Sposób implementacji skanera/parsera: Użycie generatora ANTLR


## Przykładowy kod:

# Wczytanie danych z pliku CSV
dane <- wczytaj_dane("dane.csv")

# Wyświetlenie pierwszych 5 wierszy danych
wyswietl(dane, 5)

# Obliczenie średniej wartości w kolumnie "Wiek"
srednia_wiek <- srednia(dane["Wiek"])

# Wyświetlenie wyniku
wyswietl("Średni wiek:", srednia_wiek)


Modelowanie danych:
# Podział danych na zbiór treningowy i testowy
treningowe_dane, testowe_dane <- podzial_danych(dane, proporcja=0.8)

# Utworzenie modelu regresji liniowej
model <- regresja_liniowa(treningowe_dane["Wiek"], treningowe_dane["Wynik"])

# Ocena modelu na zbiorze testowym
wyniki <- ocena_modelu(model, testowe_dane["Wiek"], testowe_dane["Wynik"])

# Wyświetlenie wyników
wyswietl("Współczynniki regresji:", model.wspolczynniki)
wyswietl("MSE (Mean Squared Error):", wyniki.MSE)
wyswietl("R^2 (Coefficient of Determination):", wyniki.R2)


Wizualizacja danych:
# Wykres punktowy wieku w stosunku do wyniku
wykres_punktowy(dane["Wiek"], dane["Wynik"], tytul="Zależność wieku od wyniku", x_label="Wiek", y_label="Wynik")

## Tokeny 
TKN_LOAD_DATA           :('wczytaj_dane');
TKN_DISPLAY             :('wyswietl');
TKN_SPLIT_DATA          :('podzial_danych');
TKN_LINEAR_REGRESSION   :('regresja_liniowa');
TKN_MODEL_EVALUATION    :('ocena_modelu');
TKN_MEAN                :('srednia');
TKN_POINT_PLOT          :('wykres_punktowy');
TKN_CSV_FILE            :('dane.csv');
TKN_PROPORTION          :('proporcja');
TKN_TITLE               :('tytul');
TKN_X_LABEL             :('x_label');
TKN_Y_LABEL             :('y_label');
TKN_TRAINING_DATA       :('treningowe_dane');
TKN_TEST_DATA           :('testowe_dane');
TKN_RESULT              :('wyniki');
TKN_MSE                 :('MSE');
TKN_R2                  :('R2');


## Gramatyka:
program:
    code EOF;

code:
    dataManipulationExpression TKN_END_LINE |
    dataManipulationExpression TKN_END_LINE code |
    TKN_COMMENT code;

dataManipulationExpression:
    loadDataExpression |
    displayDataExpression |
    splitDataExpression |
    linearRegressionExpression |
    modelEvaluationExpression |
    meanExpression |
    pointPlotExpression;

loadDataExpression:
    TKN_LOAD_DATA TKN_LBRACKET TKN_CSV_FILE TKN_RBRACKET;

displayDataExpression:
    TKN_DISPLAY valueList;

splitDataExpression:
    TKN_SPLIT_DATA TKN_LBRACKET value COMMA TKN_PROPORTION EQUALS value TKN_RBRACKET;

linearRegressionExpression:
    TKN_LINEAR_REGRESSION TKN_LBRACKET value COMMA value TKN_RBRACKET;

modelEvaluationExpression:
    TKN_MODEL_EVALUATION TKN_LBRACKET value COMMA value TKN_RBRACKET;

meanExpression:
    TKN_MEAN TKN_LBRACKET value TKN_RBRACKET;

pointPlotExpression:
    TKN_POINT_PLOT TKN_LBRACKET value COMMA value COMMA TKN_TITLE EQUALS value COMMA TKN_X_LABEL EQUALS value COMMA TKN_Y_LABEL EQUALS value TKN_RBRACKET;

value:
    NUMBER | STRING | VARIABLE_ID;

valueList:
    value | valueList COMMA value;

NUMBER:
    ('0'..'9')+;

STRING:
    '"' (ESC | ~["\\])* '"';

VARIABLE_ID:
    [a-zA-Z_][a-zA-Z_0-9]*;

TKN_WHITESPACE:
    (' ' | '\t' | '\n') -> skip;

TKN_COMMENT:
    ('#' .*? '\n' | '//' .*? '\n') -> skip;

fragment ESC:
    '\\' (["\\/bfnrt] | UNICODE);


##Opis i schemat struktury programu:
- ** Kod źródłowy jest wczytywany z pliku.
- **Przechodzi przez skaner, który przekształca go na tokeny.
- **Następnie tokeny są analizowane przez parser, który przyporządkowuje je do odpowiednich konstrukcji gramatycznych.
- **Na podstawie parsowania, generowane są odpowiednie instrukcje w języku Python.
- **Implementacja w języku Python obejmuje również klasę Listenera, która przetwarza drzewo parsowania i generuje kod w języku Python.

 ##Informacje o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych
W projekcie wykorzystujemy generator parserów ANTLR oraz język Python.

##Informacje o zastosowaniu specyficznych metod rozwiązania problemu
Język DataScript został zaprojektowany z myślą o łatwej analizie danych oraz integracji z istniejącymi narzędziami do analizy danych. Implementacja w oparciu o ANTLR i Pythona umożliwia elastyczne przetwarzanie i generowanie kodu.

