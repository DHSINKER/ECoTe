# 18 괄호 변환 1회차x
def collect(s):
    o = 0
    for i in range(len(s)):
        if s[i] == '(':
            o+=1
        else:
            if o!=0:
                o-=1
            else:
                return False        
    return True

def solution(p):
    result = ''
    if p == '':
        return result
    u, v = '', ''
    o, c = 0, 0
    u+=p[0]
    if u[0] == '(':
        o+=1
    else:
        c+=1
    
    for i in range(1, len(p)):
        if o != c:
            u+=p[i]
            if p[i] =='(':
                o+=1
            else:
                c+=1
        else:
            v+=p[i]
    if collect(u):
        result = u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        result += "".join(u)
    
    return result
