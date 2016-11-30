# Copyright (c) 2009 NHN Inc. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#    * Neither the name of NHN Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

class _NsiqCppStyleState(object):
    """Maintains module-wide state.."""
    def __init__(self):
        self.error_count = 0    # global count of reported errors
        self.total_count = 0    # global count of reported and non-reported
        # filters to apply when emitting error messages
        self.checkers = []
        self.errorPerChecker = {}
        self.totalPerChecker = {}
        self.errorPerFile = {}
        self.totalPerFile = {}
        # output format:
        # "emacs" - format that emacs can parse (default)
        # "vs7" - format that Microsoft Visual Studio 7 can parse
        self.output_format = 'vs7'
        self.verbose = False
        self.showUrl = False
        self.reportError = False
        self.suppressRules = {}
        self.varMap = {}
        self.output_location = None

    def SetOutPutCSV(self, output_location):
        """Sets the output location for errors."""
        self.output_location = output_location

    def SetOutputFormat(self, output_format):
        """Sets the output format for errors."""
        self.output_format = output_format

    def SetVerboseLevel(self, level):
        """Sets the module's verbosity, and returns the previous setting."""
        last_verbose_level = self.verbose_level
        self.verbose_level = level
        return last_verbose_level

    def SetCheckers(self, checkers):
        self.checkers = checkers
   
    def ResetErrorCount(self):
        """Sets the module's error statistic back to zero."""
        self.error_count = 0
        self.total_count = 0
        self.errorPerChecker = {}
        self.totalPerChecker = {}
        self.errorPerFile = {}
        self.totalPerFile = {}

    def IncrementErrorCount(self, category, file):
        """Bumps the module's error statistic."""
        self.error_count += 1
        self.total_count += 1

        self.errorPerChecker[category] = self.errorPerChecker.get(category, 0) + 1
        self.totalPerChecker[category] = self.totalPerChecker.get(category, 0) + 1

        errorsPerFile = self.errorPerFile.get(file, {})
        totalsPerFile = self.totalPerFile.get(file, {})

        errorsPerFile[category] = errorsPerFile.get(category, 0) + 1
        totalsPerFile[category] = totalsPerFile.get(category, 0) + 1

        self.errorPerFile[file] = errorsPerFile
        self.totalPerFile[file] = totalsPerFile

    def IncrementTotalCount(self, category, file):
        self.total_count += 1
        self.totalPerChecker[category] = self.totalPerChecker.get(category, 0) + 1
        totalsPerFile = self.totalPerFile.get(file, {})
        totalsPerFile[category] = totalsPerFile.get(category, 0) + 1
        self.totalPerFile[file] = totalsPerFile

    def SuppressRule(self, ruleName):
        self.suppressRules[ruleName] = True
  
    def ResetRuleSuppression(self):
        self.suppressRules = {}
  
    def CheckRuleSuppression(self, ruleName):
        return self.suppressRules.get(ruleName, False)
      
    def GetVar(self, key, defaultValue):
        return self.varMap.get(key, defaultValue)

    def GetOutPutCSV(self):
        """Gets the output location for errors."""
        return self.output_location

_nsiqcppstyle_state = _NsiqCppStyleState()
