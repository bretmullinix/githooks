import re


class ParseMarkdownRule():

    def __init__(self, raw_markdown_rule):
        self.raw_markdown_rule = raw_markdown_rule

    def parse_raw_markdown_rule(self):
        pattern = r'(.+):([0-9]+):\s(MD[0-9][0-9][0-9])\s(.+)'
        results = re.search(pattern, self.raw_markdown_rule)
        return results

    def is_rule(self):
        raw_markdown = self.parse_raw_markdown_rule()
        if not raw_markdown:
            return False
        if not raw_markdown.group[1]:
            return False
        if not raw_markdown.group[2]:
            return False
        if not raw_markdown.group[3]:
            return False
        if not raw_markdown.group[4]:
            return False

        return True
