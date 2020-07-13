import re

class ParseMarkdownRule():

    def __init__(self, raw_markdown_rule):
        self.raw_markdown_rule = raw_markdown_rule

    def parse_raw_markdown_rule(self):
        pattern = r'(.+):([0-9]+):\s(MD[0-9][0-9][0-9])\s(.+)'
        results = re.search(pattern, self.raw_markdown_rule)
        return results
