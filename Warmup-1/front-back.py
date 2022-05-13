
def front_back(a: str):
    if (len(a) == 0 or len(a) == 1):
        return a
    b = a[-1] + a[1:-1] + a[0]
    return b

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))