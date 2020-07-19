import unittest
import re
import sys
import os
from unittest import mock
from unittest.mock import Mock, patch
from githooks.pre_commit_directory.common_classes.parse_markdown_rule import MarkdownRule
from re import Match


class TestMarkdownRule(unittest.TestCase):

    raw_markdown_re_groups = ['/test/readme.md:15: MD009: No Trailing Spaces','/test/readme.md', '15', 'MD009', 'No Trailing Spaces.']
    def my_side_effect(self, *args):
        return self.raw_markdown_re_groups[args[0]]

    def test_generate_rule(self):
        match = mock.Mock()
        match.group.side_effect = self.my_side_effect
        obj = MarkdownRule(match)
        assert (obj.rule == 'MD009')
        assert (obj.file_line_number == 15)


if __name__ == '__main__':
    unittest.main()
