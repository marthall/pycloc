#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import print_function
import os
import sys
from argparse import ArgumentParser

here = os.getcwd()

LANGUAGES = {
    "Python": {"EXT": ["py"],
               "INLINE_COMMENT": ["#"],
               "BLOCK_COMMENT": ['"""', "'''"]}
}


def print_table():
    None


def line_count(file_name):
    number_of_lines = 0
    number_code_lines = 0
    number_of_comment_lines = 0
    number_of_blank_lines = 0
    files = 0

    ext = file_name.rsplit(".")[-1]
    language = None
    for lang in LANGUAGES:
        if ext in LANGUAGES[lang]["EXT"]:
            language = lang
            break
    if language is None:
        print("Extension not found!")
        sys.exit(0)

    for line in open(file_name).readlines():
        if line.strip() == "":
            number_of_blank_lines += 1
        elif line.lstrip()[0] in LANGUAGES[language]["INLINE_COMMENT"]:
            number_of_comment_lines += 1
        else:
            number_code_lines += 1
        number_of_lines += 1

    print(80 * "-")
    print("{lang:<16}{files:>16}{blank:>16}{comment:>16}{code:>16}".format(
        lang="language",
        files="files",
        blank="blank",
        comment="comments",
        code="code"
    ))
    print(80 * "-")
    for i in range(1):
        print("{lang:<16}{files:>16}{blank:>16}{comment:>16}{code:>16}".format(
            lang=language,
            files=files,
            blank=number_of_blank_lines,
            comment=number_of_comment_lines,
            code=number_code_lines
        ))
    print(80 * "-")

    return number_of_lines, number_code_lines, number_of_comment_lines,
    number_of_blank_lines


def get_args():
    parser = ArgumentParser(description="Python line counting tool?",
                            prog='pycloc')
    parser.add_argument('-f', '--file',
                        dest='file', help='input file')
    return parser.parse_args()


def main():
    args = get_args()
    if args.file:
        abs_path = os.path.join(here, args.file)
        line_count(abs_path)
        exit()


if __name__ == '__main__':
    main()
