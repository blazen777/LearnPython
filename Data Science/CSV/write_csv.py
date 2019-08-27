import csv

users= [{'login': 'jsmith', 'password': 'p@ssw3rd'}, {'login': 'janesmith', 'password': 's3cret'},
        {'login': 'joesmith', 'password': 'blackd0g'}, {'login': 'jimsmith', 'password': 'wh1it3cAt'},
        {'login': 'jacksmith', 'password': 'blu3FisH'}, {'login': 'johndoe', 'password': 'R3dHors3'},
        {'login': 'janedoe', 'password': 'GreenFr0g'}, {'login': 'msanders', 'password': 'YellowTurtle'},
        {'login': 'boballen', 'password': 'PurpleSnake'}, {'login': 'jamesq', 'password': 'PinkPig'},
        {'login': 'mscott', 'password': 'WhiteZebra'}, {'login': 'jhalprin', 'password': 'BlackTurkey'},
        {'login': 'tjones', 'password': 'BlueHawk'}, {'login': 'tomjones', 'password': 'GreenTree'},
        {'login': 'greggjones', 'password': 'OrangeFish'}, {'login': 'dthompson', 'password': 'RedBoat'},
        {'login': 'pjones', 'password': 'BlackSnake'}, {'login': 'fsmith', 'password': 'WhiteHorse'},
        {'login': 'fransmith', 'password': 'YellowDuck'}, {'login': 'cthompson', 'password': 'BlueEel'}]

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['login', 'password']
    writer = csv.DictWriter(f,fields,delimiter=';')
    # 1-я строка - название полей
    writer.writeheader()

    for user in users:
        writer.writerow(user)