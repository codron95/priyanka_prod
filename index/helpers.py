import re

def remove_special_chars(string):
    regex = re.compile("[^0-9a-zA-Z\-]")
    return re.sub(regex, "", string)