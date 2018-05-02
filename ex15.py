def revwords(phrase):
    phrase_list = phrase.split()
    rev_order = ''
    for item in phrase_list:
        rev_order = item + ' ' + rev_order
    return rev_order.rstrip()
