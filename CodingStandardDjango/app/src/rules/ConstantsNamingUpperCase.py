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
from app.src.nsiqcppstyle_rulehelper import  *
from app.src.nsiqcppstyle_reporter import *
from app.src.nsiqcppstyle_rulemanager import *
import re

# Rule Definition
def RunRule(lexer, contextStack) :
    # We first obtain the first token and the type
    t = lexer.GetCurToken()
    if t.type == "CONST":
        # We also obtain the next two tokens, first one to get the name and the second one
        # to verify if this is an array definition
        t2 = lexer.GetNextTokenSkipWhiteSpace();
        if t2.type == "INT" or t2.type == "BOOL" or t2.type == "FLOAT" or t2.type == "STRINGTYPE" or t2.type == "CHAR":
            
            t3 = lexer.GetNextTokenSkipWhiteSpace();
            
            # We obtain the prefix name from the type and add Arr if this is an array
            prefixType = t2.type[0].lower()

            t4 = lexer.GetNextTokenSkipWhiteSpace();

            if(t4.type == "LBRACKET"):
                prefixType = prefixType + "Arr"
            
            # Finally we create a regex that matches the desired variable definition
            variableRegex = re.escape(prefixType) + r"([A-Z]*)+$"

            # If this is not the main function and the 
            if(not bool(re.search(variableRegex, t3.value))):
                nsiqcppstyle_reporter.Error(t, __name__, 
                          t.type + " constant declaration (Prefix Type: " + prefixType + 
                          " + UPPERCASE): \'" + t3.value + "\' is incorrect")
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