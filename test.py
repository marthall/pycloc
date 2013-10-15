import os, sys

here = os.path.dirname(__file__)

   # Dette er en kommentar
def line_count(file_name):
    number_of_lines = 0
    for line in open(file_name).readlines():
        number_of_lines += 1
    return number_of_lines

print line_count(os.path.join(here, "test.py"))