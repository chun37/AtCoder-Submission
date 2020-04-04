def is_similar_coffee(s):
    if s[2] != s[3]:
        return False
    elif s[4] != s[5]:
        return False
    return True


s = input()
if is_similar_coffee(s):
    print("Yes")
else:
    print("No")
