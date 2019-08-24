import csv

with open('users.csv', 'r', encoding='utf-8') as f:
    fields = ['login', 'firstname', 'lastname', 'password']
    reader = csv.DictReader(f, fields, delimiter = ',')

    users = []
    for row in reader:
        users.append(dict(login=row['login'], password=row['password']))
    
    print(users)