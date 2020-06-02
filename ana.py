from collections import defaultdict


def file_to_list(filename: str):
    lst = []
    with open(filename, 'r') as f:
        for line in f:
            lst.append(line.strip())
    return lst


def set_to_str(s):
    return ''.join(sorted(s))


def group_ana(lst):
    res = defaultdict(list)

    for i in range(len(lst)):
        key = set_to_str(lst[i].lower())
        res[key].append(lst[i])

    return res


def print_dict(d):
    for k in d:
        for w in d[k]:
            print(w, end=' ')
        print()


def write_dict(d, filename):
    with open(filename, 'w') as f:
        for k in d:
            for w in d[k]:
                f.write(w)
                f.write(' ')
            f.write('\n')


lst = file_to_list('ana_input.txt')
d = group_ana(lst)
print_dict(d)










