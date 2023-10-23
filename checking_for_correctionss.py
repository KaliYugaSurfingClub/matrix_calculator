import re

def checking_is_num(string):
    return string.isdigit() and string != "0"

def matrix_name_checking_for_correctness(name):
    return re.match("^[A-Za-z]*$", name) and len(name) == 1

  



    