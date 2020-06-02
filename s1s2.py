def is_s1_less_s2(s1, s2):
    if len(s1) < len(s2):
        return True
    if len(s1) == len(s2):
        if s1 < s2:
            return True
    return False


def closest_non_z(s):
    for i in range(len(s) - 1, 0 - 1, -1):
        if s[i] != 'z':
            return i
    return -1


def next_s(s):
    i = closest_non_z(s)
    if i == -1:
        return 'a' * (len(s) + 1)

    left = s[:i]
    center = chr(ord(s[i]) + 1)
    right = (len(s) - i - 1) * 'a'
    return left + center + right


str1 = 'zzy'
str2 = 'aaac'

if is_s1_less_s2(str2, str1):
    str1, str2 = str2, str1

s = str1
print(s)
while is_s1_less_s2(s, str2):
    s = next_s(s)
    print(s)


