
def not_string(a: str):
    return 'not ' + a if not a[:3] == "not" else a

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))