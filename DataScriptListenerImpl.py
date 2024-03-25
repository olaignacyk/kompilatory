from DataScriptListener import DataScriptListener

class DataScriptCustomListener(DataScriptListener):
    def enterLoadDataStatement(self, ctx):
        print("Entering load data statement: " + ctx.STRING().getText())

    def exitLoadDataStatement(self, ctx):
        print("Exiting load data statement")

    def enterDisplayDataStatement(self, ctx):
        print("Entering display data statement: ")
        for string_ctx in ctx.STRING():
            print(string_ctx.getText())

    def exitDisplayDataStatement(self, ctx):
        print("Exiting display data statement")

    def enterSplitDataStatement(self, ctx):
        print("Entering split data statement: " + ctx.STRING().getText() + ", " + ctx.NUMBER().getText())

    def exitSplitDataStatement(self, ctx):
        print("Exiting split data statement")

    def enterLinearRegressionStatement(self, ctx):
        print("Entering linear regression statement: " + ctx.STRING(0).getText() + ", " + ctx.STRING(1).getText())

    def exitLinearRegressionStatement(self, ctx):
        print("Exiting linear regression statement")

    def enterModelEvaluationStatement(self, ctx):
        print("Entering model evaluation statement: " + ctx.STRING(0).getText() + ", " + ctx.STRING(1).getText())

    def exitModelEvaluationStatement(self, ctx):
        print("Exiting model evaluation statement")

    def enterMeanStatement(self, ctx):
        print("Entering mean statement: " + ctx.STRING().getText())

    def exitMeanStatement(self, ctx):
        print("Exiting mean statement")

    def enterPointPlotStatement(self, ctx):
        print("Entering point plot statement: " + ctx.STRING(0).getText() + ", " + ctx.STRING(1).getText() + ", " + ctx.STRING(2).getText())

    def exitPointPlotStatement(self, ctx):
        print("Exiting point plot statement")
