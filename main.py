#!/usr/bin/env python3

import argparse
from zipfile import ZipFile
import gzip
import tarfile
import os
import sys

"""
TODO list:
- check archive name
- check archive compression
- check archive contents
    - check if it contains only needed files
- check if size complies?
- maybe unpack into testdir, build, run, run tests?
"""

"""
Supported archives/compression -
.zip, .gz, .tar, .tar.gz
"""

# Right now hardcoded archive contents
archive_contents = [
    'text.txt',
    'src/main.c'
]


def check_zip(zip_name: str):
    # Raises if file isn't valid ZipFile
    with ZipFile(os.path.join(os.path.abspath('.'), zip_name), 'r') as zip:
        file_list = zip.namelist()
        if (sorted(archive_contents) == sorted(file_list)):
            print(f"{zip_name} checks out")


def check_archive(archive_name: str):
    """
    Checks the archive format, compression, contents
    """
    name, ext = archive_name.split('.', maxsplit=2)

    # deduct archive type/compression from extension
    if ext == 'zip':
        check_zip(archive_name)
    elif ext == 'tar':
        pass
    elif ext == 'gz':
        pass
    # probably useless extra branch as tar and tar.gz can be both handled by tarfile lib
    elif ext == 'tar.gz':
        pass
    else:
        raise Exception("Unsupported archive/compression extension")


if __name__ == "__main__":
    """
    Right now just archive checking for starters
    """
    arg_parser = argparse.ArgumentParser(
        description="Check the FIT project archive and it's content format")
    arg_parser.add_argument('--subject', help='Name of the subject')
    arg_parser.add_argument('--project', help='Name of the project')
    arg_parser.add_argument(
        '--archive', help='Name of the archive', required=True)

    args = arg_parser.parse_args()

    # get all the files in the directory (cwd now)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    if args.archive not in files:
        print('Archive is not in the cwd', file=sys.stderr)

    check_archive(args.archive)
