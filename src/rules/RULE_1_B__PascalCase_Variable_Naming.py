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
def RunRule(lexer, contextStack) :
    t = lexer.GetCurToken()
    if t.type == "INT" or t.type == "BOOL" or t.type == "FLOAT" or t.type == "STRINGTYPE" or t.type == "CHAR":
        t2 = lexer.GetNextTokenSkipWhiteSpace();
        t3 = lexer.GetNextTokenSkipWhiteSpace();
        prefixType = t.type[0].lower()
        if(t3.type == "LBRACKET"):
            prefixType = prefixType + "Arr"
        variableRegex = re.escape(prefixType) + r"([A-Z][a-z]*[0-9]*)+$"
        if(t2.value != "main" and not bool(re.search(variableRegex, t2.value))):
            nsiqcppstyle_reporter.Error(t, __name__, 
                      t.type + " variable declaration (Prefix Type: " + prefixType + 
                      " + PascalCase): \'" + t2.value + "\' is incorrect")
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