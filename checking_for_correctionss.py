import re

def matrix_name_is_correct(name):
    return re.match("^[A-Za-z]*$", name) and len(name) == 1

  



    