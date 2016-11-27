import nsiqcppstyle_reporter
from nsiqcppstyle_rulemanager import *

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

        frstLineOpenBlockComment = "/*" == t.line
        scndLineFunctionName = len(commentLines[1].split()) == 1
        thrdLineEmpty = commentLines[2] == ""
        frthLineDescription = len(commentLines[3].split()) > 1 # minimum 2 words

        if not(frstLineOpenBlockComment and scndLineFunctionName and thrdLineEmpty and frthLineDescription):
            nsiqcppstyle_reporter.Error(t, __name__, "Function comment doesn't follow format style")


ruleManager.AddFunctionNameRule(RunRule)