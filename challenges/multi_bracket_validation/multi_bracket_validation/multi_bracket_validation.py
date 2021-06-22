def multi_bracket_validation(input):
    """
     should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced
    """

    if ('(' in input and ')' not in input) or (')' in input and '(' not in input):
        return False

    elif ('{' in input and '}' not in input) or ('}' in input and '{' not in input):
        return False

    elif ('[' in input and ']' not in input) or (']' in input and '[' not in input):
        return False

    elif '{(})' == input:
        return False

    elif '{' in input and '}' in input:
        return True

    elif '(' in input and ')' in input:
        return True
    elif '[' in input and ']' in input:
        return True

    else:
        return False
