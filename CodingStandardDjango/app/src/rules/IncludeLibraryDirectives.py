"""
    Every library must begin with #include and the correct name of the library between <>

== Violation ==

    include <stdio.h>
    #include (stdio.h)
    #include <stdo.h>


== Good ==

    #include <stdio.h>
    #include <math.h>

"""
from nsiqcppstyle_rulehelper import *
from nsiqcppstyle_reporter import *
from nsiqcppstyle_rulemanager import *

STANDARD_LIBRARIES = " cstddef limits climits cfloat cstdint new typeinfo exception ciso646 exception_list " \
                    "initializer_list csignal csetjmp cstdalign cstdarg cstdbool ctime stdexcept cassert cerrno " \
                    "system_error utility tuple optional any memory memory_resource scoped_allocator cstdlib " \
                    "bitset functional type_traits ratio chrono ctime typeindex string cctype cwctype cstring " \
                    "string_view cwchar cuchar locale codecvt clocale array deque forward_list list vector map " \
                    "set unordered_map unordered_set queue stack iterator algorithm execution_policy cfenv " \
                    "complex random valarray numeric cmath ctgmath iosfwd iostream ios streambuf istream ostream " \
                    "iomanip sstream fstream filesystem cstdio cinttypes regex thread mutex atomic shared_mutex " \
                    "condition_variable future assert ctype errno fenv float inttyp limits locale math setjmp " \
                    "signal stdarg stddef stdint stdio stdlib string time uchar wchar wctype "
# Rule Definition
def RunRule(lexer, contextStack):
    token = lexer.GetCurToken()

    # Verify if the include doesn't have #
    if (token.type == "ID" and token.value.find("include") != -1):
        nsiqcppstyle_reporter.Error(token, __name__, "it Should include preprocessor #")
    elif (token.type == "PREPROCESSOR" and token.value == "#include"):
        lt = lexer.PeekNextTokenSkipWhiteSpaceAndComment()

        # If it is a custom library it is correct
        if (lt.type == "STRING"):
            return

        hasLessThanToken = lt.type == "LT"

        # peek next four tokens to find greater than sign san save the library name
        lexer.PushTokenIndex()
        lexer.GetNextTokenSkipWhiteSpaceAndComment()
        libraryName = lexer.GetNextTokenSkipWhiteSpaceAndComment().value
        lexer.GetNextTokenSkipWhiteSpaceAndComment()
        lexer.GetNextTokenSkipWhiteSpaceAndComment()
        gt = lexer.GetNextTokenSkipWhiteSpaceAndComment()
        lexer.PopTokenIndex()

        hasGreaterThanToken = gt.type == "GT"

        # Verify if it has proper format between <>
        if not(hasLessThanToken and hasGreaterThanToken):
            nsiqcppstyle_reporter.Error(token, __name__, "Library must have proper format between <>")

        # Verify if it is a standard library
        if STANDARD_LIBRARIES.find(" " + libraryName + " ") == -1:
            nsiqcppstyle_reporter.Error(token, __name__, "Library name must be part of C++ standard libraries")


ruleManager.AddRule(RunRule)
ruleManager.AddPreprocessRule(RunRule)

###########################################################################################
# Unit Test
###########################################################################################

from nsiqunittest.nsiqcppstyle_unittestbase import *


class testRule(nct):
    def setUpRule(self):
        ruleManager.AddRule(RunRule)
        ruleManager.AddPreprocessRule(RunRule)

    def test1(self):
        self.Analyze("thisfile.cpp", """
#include <math.h>
""")
        assert not CheckErrorContent(__name__)

# library mat doesn't exit
    def test2(self):
        self.Analyze("thisfile.cpp", """
#include <mat.h>
""")
        assert CheckErrorContent(__name__)

# library must be between <>
    def test3(self):
        self.Analyze("thisfile.cpp", """
#include (math.h)
""")
        assert CheckErrorContent(__name__)

# include doesnt have preprocessor
    def test4(self):
        self.Analyze("thisfile.cpp", """
include <math.h>
""")
        assert CheckErrorContent(__name__)