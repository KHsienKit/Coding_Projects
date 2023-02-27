import random

#Roles in LoL
Roles = ['Top', 'Jungle', 'Mid', 'ADC', 'Support']
Roles_left = [x.lower() for x in Roles]

#Fillers
List_of_Fillers = []
Number_of_Fillers = int(input('No. of people who called Fill: '))
while Number_of_Fillers > 5:
    print('Try again retard')
    Number_of_Fillers = int(input('No. of people who called Fill: '))
a = Number_of_Fillers
while a != 0:
    Name_of_Filler = input('Name of Filler: ')
    List_of_Fillers.append(Name_of_Filler)
    a -= 1
    

#Role Minusing
Number_of_roles_left = 5 - Number_of_Fillers
b = Number_of_roles_left
while b != 0:
    Called_Role = (input('Role that is called: '))
    if Called_Role.lower() == 'jg':
        Roles_left.remove('jungle')
        b -= 1
    elif Called_Role.lower() == 'supp':
        Roles_left.remove('support')
        b -= 1
    elif Called_Role.lower() not in Roles_left:
        print('try again')
    else:
        Roles_left.remove(Called_Role)
        b -= 1

#Random Picking Time
def fill(x):
    d = -1
    while d != (len(x)):
        if len(Roles_left) == 1:
            print(x[d], 'will play', Roles_left[0])
            break
        else:
            c = random.randint(1, len(Roles_left))
            print(x[d], 'will play', Roles_left[c-1])
            Roles_left.remove(Roles_left[c-1])
            x.remove(x[d])

#Fill
for x in List_of_Fillers:
    fill(List_of_Fillers)
    
