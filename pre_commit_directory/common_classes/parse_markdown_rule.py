import re
from githooks.pre_commit_directory.common_classes.markdown_rule import MarkdownRule


class ParseMarkdownRule:

    def __init__(self, raw_markdown_rule):
        self.raw_markdown_rule = raw_markdown_rule
        self._parse_raw_markdown_rule()

    def _parse_raw_markdown_rule(self):
        pattern = r'(.+):([0-9]+):\s(MD[0-9][0-9][0-9])\s(.+)'
        match_object = re.search(pattern, self.raw_markdown_rule)
        if match_object:
            self.rule = MarkdownRule(match_object)
        else:
            self.rule = None

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

    def get_rule(self):
        return self.rule
