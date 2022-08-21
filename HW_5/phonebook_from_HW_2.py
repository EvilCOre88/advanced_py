import csv
import re

from module import logger


def book_reader(filename):
    with open(filename, encoding="utf-8") as f:
      rows = csv.reader(f, delimiter=',')
      old_list = list(rows)
    return old_list

def book_writer(filename, new_list):
    with open(filename, "w",encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)

@logger('log.txt')
def split_name(old_list):
    pattern =re.compile(r'\w+')
    for l, list_ in enumerate(old_list):
        name = pattern.findall(list_[0])
        if len(name) == 1:
            name = pattern.findall(list_[1])
            if len(name) == 1:
                old_list[l][1] = name[0]
            elif len(name) == 2:
                old_list[l][1] = name[0]
                old_list[l][2] = name[1]
        elif len(name) == 2:
            old_list[l][0] = name[0]
            old_list[l][1] = name[1]
        elif len(name) == 3:
            old_list[l][0] = name[0]
            old_list[l][1] = name[1]
            old_list[l][2] = name[2]
    return old_list

@logger('log.txt')
def todo_phones(old_list):
    search_pattern = r'(\+7|8)[\s(]*(\d{3})[)\s-]*(\d{3})-*(\d{2})-*(\d{2})[\s(]*(доб\.)*\s*(\d{4})*\)*'
    replace_pattern = r'+7(\2)\3-\4-\5 \6\7'
    for l, list in enumerate(old_list):
        new_phone = re.sub(search_pattern, replace_pattern, list[5])
        old_list[l][5] = new_phone.strip()
    return old_list

@logger('log.txt')
def clear_doubles(old_list):
    new_list = []
    last_names = [name[1] for name in old_list]
    names = [name[0] for name in old_list]
    for l, list_ in enumerate(old_list):
        print(list_)
        if (names.count(list_[0]) and last_names.count(list_[1])) == 1:
            new_list.append(list_)
        else:
            sec_index = [i for i in range(l+1, len(old_list)) if old_list[i][0] == list_[0]]
            try:
                if sec_index[0] is not None:
                    indexes = [l]
                    indexes.append(sec_index[0])
                for i, item in enumerate(old_list[l]):
                    if item == '':
                        old_list[l][i] = old_list[indexes[1]][i]
                new_list.append(old_list[l])
            except IndexError:
                pass
    return new_list


if __name__ == '__main__':
    old_list = book_reader("phonebook_raw.csv")
    split_name(old_list)
    todo_phones(old_list)
    new_list = clear_doubles(old_list)
    book_writer("phonebook.csv", new_list)


