"""
Filenames should use PascalCase formating.

== Violation ==

    TheLongAndWindingRoad.cpp <== Error
    TheLongAndWindingRoad.h <== Error

== Good ==
    thelongAndwindingroad.cpp
    BdSc.h

"""
from app.src.nsiqcppstyle_reporter import  * #@UnusedWildImport
from app.src.nsiqcppstyle_rulemanager import * #@UnusedWildImport
import re

# Rule Definition
def RunRule(lexer, filename, dirname) :
    # If the filename does not match the following regex then we raise an error
    # Regex: After any 44 characters and pascal case variable naming a ".cpp" should follow
    if not bool(re.search(r'^.{44}([A-Z][a-z]*[0-9]*)+\.cpp$', filename)):
        nsiqcppstyle_reporter.Error(nsiqcppstyle_reporter.DummyToken(lexer.filename, "", 0, 0), __name__, "Filename %s should use PascalCase formating." % filename)
    else:
        nsiqcppstyle_reporter.Total(nsiqcppstyle_reporter.DummyToken(lexer.filename, "", 0, 0), __name__, "Filename %s is correct." % filename)
# This rule is only added to be run on the filename
ruleManager.AddFileStartRule(RunRule)


###########################################################################################
# Unit Test
###########################################################################################

from nsiqunittest.nsiqcppstyle_unittestbase import *

class testRule(nct):
    def setUpRule(self):
        ruleManager.AddFileStartRule(RunRule)
        
    def test1(self):
        self.Analyze("thelongAndwindingroad.cpp", "")
        assert CheckErrorContent(__name__)
    def test2(self):
        self.Analyze("TheLongAndWindingRoad.cpp", "")
        assert not CheckErrorContent(__name__)
