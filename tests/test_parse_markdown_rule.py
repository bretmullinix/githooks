import unittest
import re
import sys
import os

from githooks.pre_commit_directory.common_classes.parse_markdown_rule import ParseMarkdownRule


class TestParseMarkdownRule(unittest.TestCase):
    MOCK_RAW_MARKDOWN_RULE = '/test/dummy/file.md:15: MD009 Trailing Spaces'

    def setup(self) -> None:
        obj = ParseMarkdownRule(self.MOCK_RAW_MARKDOWN_RULE)

    def test_markdown_rule_exists(self):
        obj = ParseMarkdownRule(self.MOCK_RAW_MARKDOWN_RULE)
        assert obj.is_rule

    def test_get_markdown_rule(self):
        obj = ParseMarkdownRule(self.MOCK_RAW_MARKDOWN_RULE)
        rule = obj.get_rule()


if __name__ == '__main__':
    unittest.main()
