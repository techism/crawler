def m(s,r):
    import re
    p=re.compile(r)
    matches=p.finditer(s)
    for match in matches:
        print match.groupdict()

s=''
r=''
m(s,r)

