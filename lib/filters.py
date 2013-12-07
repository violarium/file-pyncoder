import re


def match_regexp(reg):
    """
    Get filter, which check if string matches regular expression
    """
    compiled_reg = re.compile(reg)

    def check_regexp(text):
        return compiled_reg.match(text) is not None
    return check_regexp


def do_not_match_regexp(reg):
    """
    Get filter, which check if string does not match regular expression
    """
    compiled_reg = re.compile(reg)

    def check_regexp(text):
        return compiled_reg.match(text) is None
    return check_regexp


def has_extension(ext_string):
    """
    Get filter, which check if string has one extension from the list
    """
    ext_list = ext_string.split(',')

    def check_ext(text):
        valid = False
        for ext in ext_list:
            valid = valid or (text[-len(ext):] == ext)
        return valid
    return check_ext


def has_no_extension(ext_string):
    """
    Get filter, which check if string has no extension from the list
    """
    ext_list = ext_string.split(',')

    def check_ext(text):
        valid = True
        for ext in ext_list:
            valid = valid and (text[-len(ext):] != ext)
        return valid
    return check_ext