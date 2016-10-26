"""
Filenames should use PascalCase formating.

== Violation ==

    TheLongAndWindingRoad.cpp <== Error
    TheLongAndWindingRoad.h <== Error

== Good ==
    thelongAndwindingroad.cpp
    BdSc.h

"""
from nsiqcppstyle_reporter import  * #@UnusedWildImport
from nsiqcppstyle_rulemanager import * #@UnusedWildImport
import re

def RunRule(lexer, filename, dirname) :
    if not bool(re.search(r'(?!.)*([A-Z][a-z]*[0-9]*)+\.cpp$', filename)):
        nsiqcppstyle_reporter.Error(nsiqcppstyle_reporter.DummyToken(lexer.filename, "", 0, 0), __name__, "Filename %s should use PascalCase formating." % filename)
    
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
