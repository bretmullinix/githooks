import unittest
import re
import sys
import os

from githooks.pre_commit_directory.common_classes.parse_markdown_rule import ParseMarkdownRule


class TestParseMarkdownRule(unittest.TestCase):
    MOCK_RAW_MARKDOWN_RULE = '/test/dummy/file.md:15: MD009 Trailing Spaces'

    def test_parse_raw_markdown_rule(self) -> None:
        obj = ParseMarkdownRule(self.MOCK_RAW_MARKDOWN_RULE)
        match = obj.parse_raw_markdown_rule()

        assert match

if __name__ == '__main__':
    unittest.main()
