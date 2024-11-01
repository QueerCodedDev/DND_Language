from const.font import FONT


def code_message(s):
    s = s.upper()
    coded_message = []
    for c in s:
        if c in FONT:
            coded_message.append(FONT[c])
        else:
            # print(f"This character [ {c} ] has no representation.")
            coded_message.append(FONT[' '])

    return coded_message
