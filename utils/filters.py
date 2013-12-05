import re


def regexp(reg):
    """
    Get regular expression filter
    """
    compiled_reg = re.compile(reg)

    def check_regexp(text):
        return compiled_reg.match(text)

    return check_regexp
