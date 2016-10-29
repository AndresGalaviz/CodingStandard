"""
Do not use question(?) keyword.
if it's shown... this rule reports a violation.

== Violation ==

    void a() {
        c = t ? 1 : 2;  <== Violation. ? keyword is used. 
    }

== Good ==

    void a() {
        if (t) { <== OK.
           c = 1;
        } else {
           c = 2;
        }
    }

"""
from nsiqcppstyle_rulehelper import  *
from nsiqcppstyle_reporter import *
from nsiqcppstyle_rulemanager import *
import re

# Rule Definition
def RunRule(lexer, contextStack) :
    # We first obtain the first token and the type
    t = lexer.GetCurToken()
    if t.type == "INT" or t.type == "BOOL" or t.type == "FLOAT" or t.type == "STRINGTYPE" or t.type == "CHAR":
        # We also obtain the next token to see if this is a function
        t2 = lexer.GetNextTokenSkipWhiteSpace();
        if(t2.type == "FUNCTION"):
            if(not bool(re.search(r"^[a-z]+([A-Z][a-z]*[0-9]*)+$"), t2.value)):
                nsiqcppstyle_reporter.Error(t, __name__, 
                      t.type + " function declaration " + t2.value + " is incorrect")
       
ruleManager.AddRule(RunRule)
###########################################################################################
# Unit Test
###########################################################################################

from nsiqunittest.nsiqcppstyle_unittestbase import *
class testRule(nct):
    def setUpRule(self):
        ruleManager.AddRule(RunRule)   
        
    def test1(self):
        self.Analyze("thisfile.c","""
void Hello() {
   int iarrPotato[1] = {1};
}
""")
        assert CheckErrorContent(__name__)
    def test2(self):
        self.Analyze("thisfile.c","""
int iArrPotato[1] = {1};
void Hello() {
}
""")
        assert not CheckErrorContent(__name__)