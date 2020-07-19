

class MarkdownRule:
    def __init__(self):
        pass

    def __init__(self, regex_match):
        self.re_match = regex_match
        self._parse_re_match()

    def _parse_re_match(self):
        self.rule = self.re_match.group(3)
        self.rule_description = self.re_match.group(4)
        self.file = self.re_match.group(1)
        self.file_line_number = int(self.re_match.group(2))
