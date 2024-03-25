from antlr4 import *
from DataScriptLexer import DataScriptLexer
from DataScriptParser import DataScriptParser
from DataScriptCustomListener import DataScriptCustomListener

def main():
    input_file = "example.datascript"  # Plik źródłowy w języku DataScript

    # Wczytanie pliku źródłowego
    with open(input_file, "r") as file:
        input_data = file.read()

    # Utworzenie strumienia wejściowego na podstawie wczytanego tekstu
    input_stream = InputStream(input_data)

    # Utworzenie skanera na podstawie strumienia wejściowego
    lexer = DataScriptLexer(input_stream)

    # Utworzenie strumienia tokenów na podstawie skanera
    token_stream = CommonTokenStream(lexer)

    # Utworzenie parsera na podstawie strumienia tokenów
    parser = DataScriptParser(token_stream)

    # Rozpoczęcie analizy gramatycznej od reguły 'program'
    tree = parser.program()

    # Utworzenie obiektu Listenera
    listener = DataScriptCustomListener()

    # Przechodzenie po drzewie parsowania i przekazywanie zdarzeń do Listenera
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
