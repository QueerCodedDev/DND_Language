from const.font import font


def code_message(s):
    s = s.upper()
    coded_message = []
    for c in s:
        if c in font:
            coded_message.append(font[c])
        else:
            # print(f"This character [ {c} ] has no representation.")
            coded_message.append(font[' '])

    return coded_message
