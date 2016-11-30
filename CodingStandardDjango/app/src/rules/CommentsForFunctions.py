import app.src.nsiqcppstyle_reporter as nsiqcppstyle_reporter
from app.src.nsiqcppstyle_rulemanager import *

# Rule Definition
def RunRule(lexer, fullName, decl, contextStack, typeContext):

    # Peek 2 previous tokens
    lexer.PushTokenIndex()
    lexer.GetPrevTokenSkipWhiteSpace()
    t = lexer.GetPrevTokenSkipWhiteSpace()
    lexer.PopTokenIndex()

    if t.type != "COMMENT": # if the previous 2 tokens is not a block comment
        nsiqcppstyle_reporter.Error(t, __name__, "There is not a comment before the function")
    else:
        commentLines = t.value.splitlines() # separate
        if len(commentLines) < 5:
            nsiqcppstyle_reporter.Error(t, __name__, "Function comment is missing documentation")
            return

        firstLineOpenBlockComment = "/*" == t.line
        secondLineFunctionName = len(commentLines[1].split()) == 1
        thirdLineEmpty = commentLines[2] == ""
        fourthLineDescription = len(commentLines[3].split()) > 1 # minimum 2 words

        if not(firstLineOpenBlockComment and secondLineFunctionName and thirdLineEmpty and fourthLineDescription):
            nsiqcppstyle_reporter.Error(t, __name__, "Function comment doesn't follow format style")
        else:
            nsiqcppstyle_reporter.Total(t, __name__, "Function comment follows format style")


ruleManager.AddFunctionNameRule(RunRule)

from nsiqunittest.nsiqcppstyle_unittestbase import *

class testRule(nct):
    def setUpRule(self):
        ruleManager.AddFunctionNameRule(RunRule)

# Error because the Hello can't be there there. Weong
    def test1(self):
        self.Analyze("thisfile.c", """
/* Hello

   say hello
*/
void Hello() {
}
""")
        assert CheckErrorContent(__name__)

    def test2(self):
        self.Analyze("thisfile.c", """
/*
    Hello

    say hello
*/
void Hello() {
}
""")
        assert not CheckErrorContent(__name__)

# Wrong because the description of the function has to have 2 words at least
    def test3(self):
        self.Analyze("thisfile.c", """
/*
Hello

hello
*/
void Hello() {
}
""")
        assert CheckErrorContent(__name__)

# Wrong because it needs to have space between the name of the function and the description
    def test4(self):
        self.Analyze("thisfile.c", """
/*
Hello
says hello
*/
void Hello() {
}
""")
        assert CheckErrorContent(__name__)

# Wrong because there is no comment for the function
    def test5(self):
        self.Analyze("thisfile.c", """
/*
void Hello() {
}
""")
        assert CheckErrorContent(__name__)