"""
Use spaces for indentation.
This rule check if the each line starts with tabs.
In addition, it suppresses the violation when the line contains only spaces and tabs.

== Violation ==

    void Hello() 
    {
    [TAB]         <== Don't care if the line is empty
    [TAB]Hello(); <== Violation. A tab is used for indentation.
    }

== Good ==

    void Hello() 
    {
    [TAB] <== Don't care.
    [SPACE][SPACE]Hello(); <== Good. Spaces are used for indentation.
    }

"""
from app.src.nsiqcppstyle_rulehelper import  *
from app.src.nsiqcppstyle_reporter import *
from app.src.nsiqcppstyle_rulemanager import *

# Rule Definition
def RunRule(lexer, line, lineno) :
    # If this is not an empty line
    if not Match("^\s*$", line) :
        # If we find a tab then we raise an error
        if Search("^\t", line) :
            nsiqcppstyle_reporter.Error(DummyToken(lexer.filename, line, lineno, 0), __name__, "Do not use tab for indent")

ruleManager.AddLineRule(RunRule)




###########################################################################################
# Unit Test
###########################################################################################

from nsiqunittest.nsiqcppstyle_unittestbase import *
class testRule(nct):
    def setUpRule(self):
        ruleManager.AddLineRule(RunRule)
    def test1(self):
        self.Analyze("test/thisFile.c", 
"\tbool CanHave() {\n\t}")
        assert  CheckErrorContent(__name__)    
    def test2(self):
        self.Analyze("test/thisFile.c", 
"""
class K {
    Hello
}""")
        assert not CheckErrorContent(__name__)    
    def test3(self):
        self.Analyze("test/thisFile.c", 
"""
class K {
            
Hello
}""")
        assert not CheckErrorContent(__name__)    
                