
def sleep_in(weekday: bool, vacation: bool):
    return (not weekday) or vacation

print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))