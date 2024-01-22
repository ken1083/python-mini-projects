import string

print("Change x with base a to y with base b")
x, a, b=input("Enter x, a, b(seperated by space): ").split()

enumerate = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
enumerate_reverse = {v:k for k,v in enumerate.items()}
enumerate_reverse2 = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}

def to_decimal(num, base):
    ret = 0
    base = int(base)
    pow = len(num) - 1
    for ch in num:
        if ch in string.digits:
            ret += int(ch) * base ** pow
        elif ch in enumerate_reverse:
            ret += enumerate_reverse[ch] * base ** pow
        else:
            ret += enumerate_reverse2[ch] * base ** pow
        pow -= 1
    return ret

def to_base(num, base):
    if num == 0:
        return '0'
    ret = []
    base = int(base)
    if base <= 10:
        while num:
            num, rem = divmod(num, base)
            ret.append(str(rem))
    else:
        while num:
            num, rem = divmod(num, base)
            if(rem >= 10):
                rem = enumerate[rem]
            ret.append(str(rem))
    return ''.join(ret[::-1])

dec = to_decimal(x, a)
ans = to_base(dec, b)
print(ans)

