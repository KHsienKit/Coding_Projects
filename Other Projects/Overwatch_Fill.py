import random

roles = ['Tank', 'DPS', 'DPS', 'Support', 'Support']
roles_removed = []
players = []
loop = True


def roles_append():
    for role in roles_removed:
        roles.append(role)


def role_removed_remove():
    for role in roles_removed:
        roles_removed.remove(role)
    roles_removed.remove(roles_removed[0])
    print(roles_removed)

class NumberTooBig(Exception): #Number more than 5
    pass

class NegativeNumber(Exception): #Negative number exception
    pass

while True:
    try:
        number_of_players = int(input('Number of players: '))
        if number_of_players > 5:
            raise NumberTooBig
        if number_of_players < 0:
            raise NegativeNumber
    except ValueError:
        print('Value is not a number. Try again')
        continue
    except NumberTooBig:
        print('Number too big. Try Again')
        continue
    except NegativeNumber:
        print('You cannot have negative numbe of players. Try Again')
    else:
        break


x = number_of_players

while x != 0:
    players.append(input('Player names: '))
    x -= 1



while True:
    for player in players:
        role_chosen = random.choice(roles)
        roles.remove(role_chosen)
        print(f'{player} is playing {role_chosen}')
        roles_removed.append(role_chosen)
    if input('continue?') == 'y':
        roles_append()
        roles_removed = []
        print(roles)
    else:
        break