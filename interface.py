
from antlr4.error.ErrorListener import ErrorListener
from tkinter import *
from tkinter import scrolledtext, messagebox
from antlr4 import *
from ChinesePyPlus import ChinesePyPlusLexer, ChinesePyPlusParser
import ChinesePyPlusImpl

class CustomErrorListener(ErrorListener):
    def __init__(self, output):
        super().__init__()
        self.output = output
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append((line, column, msg))

    def get_errors(self):
        return self.errors

class ChinesePyPlusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ChinesePyPlus Translator")

        self.create_widgets()

    def create_widgets(self):
        self.input_label = Label(self.root, text="Input-ChinesePyPlus")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_text = scrolledtext.ScrolledText(self.root, width=70, height=30, wrap=WORD)
        self.input_text.grid(row=1, column=0, padx=5, pady=5)

        self.translate_button = Button(self.root, text="Translate", command=self.translate_code)
        self.translate_button.grid(row=2, column=0, padx=5, pady=5)

        self.output_label = Label(self.root, text="Output")
        self.output_label.grid(row=0, column=1, padx=5, pady=5)

        self.output_text = scrolledtext.ScrolledText(self.root, width=70, height=30, wrap=WORD)
        self.output_text.grid(row=1, column=1, padx=5, pady=5)

        self.error_label = Label(self.root, text="Message")
        self.error_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.error_text = scrolledtext.ScrolledText(self.root, width=100, height=5, wrap=WORD)
        self.error_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def translate_code(self):
        input_code = self.input_text.get("1.0", END)
        try:
            translated_code, errors = self.translate_chinese_py_plus(input_code)
            self.error_text.delete("1.0", END)
            self.error_text.insert("1.0", errors)
            self.output_text.delete("1.0", END)
            self.output_text.insert("1.0", translated_code)
        except Exception as e:
            self.error_text.delete("1.0", END)
            self.error_text.insert("1.0", str(e))

    def translate_chinese_py_plus(self, code):
        input_stream = InputStream(code)
        lexer = ChinesePyPlusLexer.ChinesePyPlusLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ChinesePyPlusParser.ChinesePyPlusParser(stream)
        error_listener = CustomErrorListener(self.error_text)
        parser._listeners = [error_listener]
        tree = parser.program()

        errors = error_listener.get_errors()

        if errors:
            annotated_code = self.annotate_errors(code, errors)
            error_messages = '\n'.join([f"line {line}:{column} {msg}" for line, column, msg in errors])
            return annotated_code, error_messages
        else:
            listener = ChinesePyPlusImpl.ChinesePyPlusImpl()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            error_messages = "OK"
            return listener.code, error_messages

    def annotate_errors(self, code, errors):
        lines = code.split('\n')
        for line, column, msg in errors:
            if line - 1 < len(lines) and column - 1 < len(lines[line - 1]):
                lines[line - 1] = lines[line - 1][:column - 1] + '->' + lines[line - 1][column - 1:]
        return '\n'.join(lines)


if __name__ == "__main__":
    root = Tk()
    app = ChinesePyPlusGUI(root)
    root.mainloop()
