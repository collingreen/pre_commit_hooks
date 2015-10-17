from __future__ import absolute_import
from __future__ import unicode_literals

import argparse
import io
import re


pattern = re.compile(r"do ?not ?commit", re.I)
error_message = """Found {match} in {filename}"""


def check_donotcommit(src, filename='<unknown>'):
    """Returns nonzero if the source includes strings like
    DONOTCOMMIT.
    """

    match = pattern.search(src)

    if match:
        print(error_message.format(
            filename=filename,
            match=match.group(0)
        ))

    return 0 if match is None else 1


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        contents = io.open(filename).read()
        retv |= check_donotcommit(contents, filename=filename)

    return retv
