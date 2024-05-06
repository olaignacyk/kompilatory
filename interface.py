import tkinter as tk
from tkinter import scrolledtext
from antlr4 import *
from ChinesePyPlus import ChinesePyPlusLexer, ChinesePyPlusParser
import ChinesePyPlusImpl

class ChinesePyPlusGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator ChinesePyPlus")
        self.root.geometry("1000x1000")

        self.create_widgets()

    def create_widgets(self):
        self.input_text = scrolledtext.ScrolledText(self.root, width=60, height=40, wrap=tk.WORD)
        self.input_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.output_text = scrolledtext.ScrolledText(self.root, width=60, height=40, wrap=tk.WORD)
        self.output_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_code)
        self.translate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def translate_code(self):
        input_code = self.input_text.get("1.0", tk.END)
        translated_code = self.translate_chinese_py_plus(input_code)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", translated_code)

    def translate_chinese_py_plus(self, code):
        input_stream = InputStream(code)
        lexer = ChinesePyPlusLexer.ChinesePyPlusLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ChinesePyPlusParser.ChinesePyPlusParser(stream)
        tree = parser.program()

        listener = ChinesePyPlusImpl.ChinesePyPlusImpl()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.code

if __name__ == "__main__":
    root = tk.Tk()
    app = ChinesePyPlusGUI(root)
    root.mainloop()
