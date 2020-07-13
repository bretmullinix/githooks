import unittest
import re
import sys
import os

from githooks.pre_commit_directory import markdownlint


class TestMDL(unittest.TestCase):

    def test_matching_characters_at_start_of_line(self) -> None:
        obj = markdownlint.MarkdownLint()
        match = obj.get_re_match_characters_at_start_of_line("#", "### Header")
        assert match
        assert(match.group(1) == '###')
        match = obj.get_re_match_characters_at_start_of_line(" ", "        Header")
        assert(match.group(1) == '        ')


if __name__ == '__main__':
    unittest.main()
