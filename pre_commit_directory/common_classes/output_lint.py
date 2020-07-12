#!/usr/bin/python3
class OutputLint:
    def __init__(self, source, results, errors, has_fixes):
        self.source = source
        self.results = results
        self.errors = errors
        self.has_fixes = has_fixes

    def __str__(self):
        return "Source: " + self.source + "\n\t" + "Results = \n\t" + \
               str(self.results) + "\nErrors = \n\t" + str(self.errors)
