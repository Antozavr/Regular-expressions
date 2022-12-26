import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_book = []

name_pattern = r'([А-Я])'
name_sub = r' \1'
for column in contacts_list[1:]:
    names = column[0] + column[1] + column[2]
    if len((re.sub(name_pattern, name_sub, names).split())) == 3:
        column[0] = re.sub(name_pattern, name_sub, names).split()[0]
        column[1] = re.sub(name_pattern, name_sub, names).split()[1]
        column[2] = re.sub(name_pattern, name_sub, names).split()[2]
    elif len((re.sub(name_pattern, name_sub, names).split())) == 2:
        column[0] = re.sub(name_pattern, name_sub, names).split()[0]
        column[1] = re.sub(name_pattern, name_sub, names).split()[1]
        column[2] = ''
    elif len((re.sub(name_pattern, name_sub, names).split())) == 1:
        column[0] = re.sub(name_pattern, name_sub, names).split()[0]
        column[1] = ''
        column[2] = ''
phone_pattern = re.compile(
    r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
for column in contacts_list:
    column[5] = phone_pattern.sub(phone_substitution, column[5])
    for column in contacts_list[1:]:
        first_name = column[0]
        last_name = column[1]
        for contact in contacts_list:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]
for contact in contacts_list:
    if contact not in new_book:
        new_book.append(contact)
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_book)
