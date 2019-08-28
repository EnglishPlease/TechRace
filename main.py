s = input()

def f(chr):
    c = chr.lower()
    if c == 'a':
        return '4'
    elif c == 'l':
        return '1'
    elif c == 'i':
        return '!'
    elif c == 'h':
        return '#'
    elif c == 's':
        return '5'
    elif c == 't':
        return '7'
    elif c == 'o':
        return '0'
    elif c == 'b':
        return '8'
    elif c == 'e':
        return '3'
    elif c == 'z':
        return '2'
    else:
        return chr

s1 = ''

for c in s:
    s1 += f(c)

print(s1)
