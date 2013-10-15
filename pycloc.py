from __future__ import print_function
import os, sys

here = os.path.dirname(__file__)

LANGUAGES = {
    "Python": {"EXT": ["py"], "INLINE_COMMENT": ["#"], "BLOCK_COMMENT": ['"""', "'''"]}
}

def line_count(file_name):
    number_of_lines = 0
    number_code_lines = 0
    number_of_comment_lines = 0
    number_of_blank_lines = 0

    ext = file_name.rsplit(".")[-1]
    for lang in LANGUAGES:
        if ext in LANGUAGES[lang]["EXT"]:
            language = lang

    for line in open(file_name).readlines():
        if line.strip() == "":
            number_of_blank_lines += 1
        elif line.lstrip()[0] in LANGUAGES[language]["INLINE_COMMENT"]:
            number_of_comment_lines += 1
        else:
            number_code_lines += 1
        number_of_lines += 1
    
    print(80 * "-")
    print("Language".ljust(20) + "files".rjust(10) + "blank".rjust(16) + "comment".rjust(16) + "code".rjust(16))
    print(80 * "-")
    for i in range(1):
        print(language.ljust(20) + "%10d%16d%16d%16d" % (100, number_of_blank_lines, number_of_comment_lines, number_code_lines))
    print(80 * "-")

    return number_of_lines, number_code_lines, number_of_comment_lines, number_of_blank_lines

line_count(os.path.join(here, "test.py"))