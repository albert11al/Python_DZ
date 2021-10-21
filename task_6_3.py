from itertools import zip_longest
from json import dump

users_lines = ['Abdullaev, Albert, Elshanovic\n', 'Ivanov, Yriy, Markovic']
hobby_lines = ['football, basketball']
with open('users.csv', 'w', encoding='utf-8') as users:
   users.writelines(users_lines)
with open('hobby.csv', 'w', encoding='utf-8') as hobby:
    hobby.writelines(hobby_lines)

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open('dict_sev', 'w', encoding='utf-8') as dict:
                all_list = zip_longest((' '.join(i.split(',')) for i in users), hobby, fillvalue=None)
                dict_u_h = {str(n[0]).strip(): str(n[1]).strip() for n in all_list}

                dump(dict_u_h, dict, ensure_ascii=False, indent=4)
            print(dict_u_h)
        else:
            exit(1)