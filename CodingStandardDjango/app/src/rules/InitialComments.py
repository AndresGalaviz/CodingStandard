"""
    The block of initial comments must be enclosed in a frame using /* */
    characters and contains:
    - Name of the file
    - Description of the application
    - Author name
    - Date
    - Version number

== Violation ==

    /* Hypothenuse program
    John */

== Good ==

    /*
        Hypothenuse.cpp

        This application calculates the hypothenuse
        of a triangle with the length of the sides
        given by the user

        John Dow
        2 / May / 2015
        version 1.0
    */

"""
from app.src.nsiqcppstyle_rulehelper import  *
from app.src.nsiqcppstyle_reporter import *
from app.src.nsiqcppstyle_rulemanager import *
import app.src.nsiqcppstyle_reporter as nsiqcppstyle_reporter
import datetime
import re

# Rule Definition
def RunRule(lexer, filename, dirname) :
    # We first obtain the first token and the type
    comment = lexer.GetNextToken()
    extractedFileName = str(re.search(r'([A-Z][a-z]*[0-9]*)+\.cpp$', filename).group())
    error = ""
    if(comment.type == "COMMENT"):
        timeNow = str(datetime.datetime.now().year)
        # Regex to match version number
        versionRegex = """(v|V)ersion(\s+)([0-9](\.)?[0-9])"""
        # Verify it includes filename
        if(extractedFileName not in comment.value):
            error = error + "Verify it has: Correct name of the file\n"
        # Verify it includes filename
        if(re.search(versionRegex, str(comment.value)) is None):
            error = error + "Verify it has: Version(e.g. Version 1.0)\n"
        # Verify it includes at least the year
        if(timeNow not in comment.value):
            error = error + "Verify it has: Complete Date (e.g. 2 / May / 2016 or May/ 2 / 2016)\n"
        # Append error message
        if(error):
            nsiqcppstyle_reporter.Error(comment, __name__, "\nDoes not comply with the standard.\n" + error)
    else:
        nsiqcppstyle_reporter.Error(comment, __name__, "Does not have initial comments")
ruleManager.AddFileStartRule(RunRule)

###########################################################################################
# Unit Test
###########################################################################################

from nsiqunittest.nsiqcppstyle_unittestbase import *
class testRule(nct):
    def setUpRule(self):
        ruleManager.AddRule(RunRule)   
        
    def test1(self):
        self.Analyze("Hypothenuse.cpp","""

    /*
        Hypothenuse.cpp

        This application calculates the hypothenuse
        of a triangle with the length of the sides
        given by the user

        John Dow
        2 / May / 2015
        version 1.0
    */
""")
        assert CheckErrorContent(__name__)
    def test2(self):
        self.Analyze("thisfile.c","""
  /* Hypothenuse program
    John */
""")
        assert not CheckErrorContent(__name__)