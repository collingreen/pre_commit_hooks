from __future__ import absolute_import
from __future__ import unicode_literals

from pre_commit_hooks.do_not_commit.do_not_commit import check_donotcommit


SUCCESS = [
    '',
    '"foo"',
    'this is ok do\nnot commit',
    'do not and then other words commit should work'
]

FAIL = [
    '"foo bar # DONOTCOMMIT" baz',
    'donotcommit things here',
    'doNOTcommit things where case doesnt matter',
    'spaced out do not commit should still count',
    "python\n# do not commit",
]


# content of test_class.py
class TestClass:

    def test_pass_generator(self):
        for contents in SUCCESS:
            yield self.check_result, contents, 0

    def test_fail_generator(self):
        for contents in FAIL:
            yield self.check_result, contents, 1

    def check_result(self, contents, expected):
        assert check_donotcommit(contents) == expected
