import re

def generate_link(head):
    link = _remove_special_chars(head).lower()
    return link.replace(" ", "-")

def _remove_special_chars(string):
    regex = re.compile("[^0-9a-zA-Z ]")
    return re.sub(regex, "", string)