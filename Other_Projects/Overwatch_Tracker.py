import sqlite3
from functools import wraps

conn = sqlite3.connect('B:\Programming Stuff\Python\Coding_Projects\Discord Bot\Overwatch_Tracker.db')
#conn = sqlite3.connect(':memory:')
c = conn.cursor()

#Creating Exceptions
#Invalid Player Exception
class InvalidPlayer(Exception):
    pass

def player_check(function):
    @wraps(function)
    def wrapper(*args):
        try:
            c.execute('SELECT * FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':args[0]})
            result = c.fetchone()
            if result == None:
                raise InvalidPlayer
        except InvalidPlayer:
            raise InvalidPlayer
        return function(*args)
    return wrapper


#Creating Fuctions to Update Table

#Adding Player Function
def add_player(player, Tank_Rank, Tank_Win, Tank_Loss, DPS_Rank, DPS_Win, DPS_Loss, Support_Rank, Support_Win, Support_Loss):
    with conn:
        c.execute('INSERT INTO Overwatch_Rank_Tracker values (:Name, :Tank_Rank, :Tank_Win, :Tank_Loss, :DPS_Rank, :DPS_Win, :DPS_Loss, :Support_Rank, :Support_Win, :Support_Loss)',
        {'Name':player, 'Tank_Rank':Tank_Rank, 'Tank_Win':Tank_Win, 'Tank_Loss':Tank_Loss,'DPS_Rank':DPS_Rank, 'DPS_Win':DPS_Win, 'DPS_Loss':DPS_Loss, 'Support_Rank':Support_Rank, 'Support_Win':Support_Win, 'Support_Loss':Support_Loss})

#Deleting Player Function
@player_check
def delete_player(player):
    with conn:
        c.execute('DELETE FROM Overwatch_Rank_Tracker WHERE Name = :Name', {'Name':player})

#Update Tank Rank
@player_check
def update_Tank_Rank(player, Tank_Rank):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET Tank_rank = :Tank_Rank WHERE Name = :Name',{'Tank_Rank':Tank_Rank, 'Name':player})

#Adding Tank Win
@player_check
def add_Tank_Win(player):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET Tank_Win = Tank_Win + 1 WHERE Name = :Name',{'Name':player})
    c.execute('SELECT Tank_Win FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':player})
    Tank_Win = c.fetchone()
    if Tank_Win != None:
        for x in Tank_Win:
            if x == 7:
                with conn:
                    c.execute('UPDATE Overwatch_Rank_Tracker SET Tank_Win = 0 WHERE Name = :Name',{'Name':player})
            else:
                pass
    else:
        pass

#Adding Tank Loss
@player_check
def add_Tank_Loss(player):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET Tank_Loss = Tank_Loss + 1 WHERE Name = :Name',{'Name':player})
    c.execute('SELECT Tank_Loss FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':player})
    Tank_Loss = c.fetchone()
    if Tank_Loss != None:
        for x in Tank_Loss:
            if x == 20:
                c.execute('UPDATE Overwatch_Rank_Tracker SET Tank_Loss = 0 WHERE Name = :Name',{'Name':player})
            else:
                pass
    else:
        pass

#Update DPS Rank
@player_check
def update_DPS_Rank(player, DPS_Rank):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET DPS_Rank = :DPS_Rank WHERE Name = :Name',{'DPS_Rank':DPS_Rank, 'Name':player})

#Update DPS Win
@player_check
def add_DPS_Win(player):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET DPS_Win = DPS_Win + 1 WHERE Name = :Name',{'Name':player})
    c.execute('SELECT DPS_Win FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':player})
    DPS_Win = c.fetchone()
    if DPS_Win != None:
        for x in DPS_Win:
            if x == 7:
                with conn:
                    c.execute('UPDATE Overwatch_Rank_Tracker SET DPS_Win = 0 WHERE Name = :Name',{'Name':player})
            else:
                pass
    else:
        pass

#Update DPS Loss
@player_check
def add_DPS_Loss(player):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET DPS_Loss = DPS_Loss + 1 WHERE Name = :Name',{'Name':player})
    c.execute('SELECT DPS_Loss FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':player})
    DPS_Loss = c.fetchone()
    if DPS_Loss != None:
        for x in DPS_Loss:
            if x == 20:
                with conn:
                    c.execute('UPDATE Overwatch_Rank_Tracker SET DPS_Loss = 0 WHERE Name = :Name',{'Name':player})
            else:
                pass
    else:
        pass

#Update Support Rank
@player_check
def update_Support_Rank(player, Support_Rank):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET Support_Rank = :Support_Rank WHERE Name = :Name',{'Support_Rank':Support_Rank, 'Name':player})

#Update Support Win
@player_check
def add_Support_Win(player):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET Support_Win = Support_Win + 1 WHERE Name = :Name',{'Name':player})
    c.execute('SELECT Support_Win FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':player})
    Support_Win = c.fetchone()
    if Support_Win != None:
        for x in Support_Win:
            if x == 7:
                with conn:
                    c.execute('UPDATE Overwatch_Rank_Tracker SET Support_Win = 0 WHERE Name = :Name',{'Name':player})
            else:
                pass
    else:
        pass

#Update Support Loss
@player_check
def add_Support_Loss(player):
    with conn:
        c.execute('UPDATE Overwatch_Rank_Tracker SET Support_Loss = Support_Loss + 1 WHERE Name = :Name',{'Name':player})
    c.execute('SELECT Support_Loss FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':player})
    Support_Loss = c.fetchone()
    if Support_Loss != None:
        for x in Support_Loss:
            if x == 20:
                with conn:
                    c.execute('UPDATE Overwatch_Rank_Tracker SET Support_Loss = 0 WHERE Name = :Name',{'Name':player})
            else:
                pass
    else:
        pass

#Creating Table
c.execute('''CREATE TABLE IF NOT EXISTS Overwatch_Rank_Tracker (
            {0} text,
            {1} text,
            {2} integer,
            {3} integer,
            {4} text,
            {5} integer,
            {6} integer,
            {7} text,
            {8} integer,
            {9} interger
            )'''.format('Name', 'Tank_Rank', 'Tank_Win', 'Tank_Loss', 'DPS_Rank', 'DPS_Win', 'DPS_Loss', 'Support_Rank', 'Support_Win', 'Support_Loss'))

#Inserting player
# add_player('Soh Fun Yi', 'Silver 3', 3, 0, 'Gold 5', 1, 0, 'Silver 2', 3, 0)
# add_player('WitchDoc', 'Silver 4', 3, 0, 'Silver 4', 3, 0, 'Gold 4', 3, 0)
# add_player('Gondor', 'Silver 4', 3, 0, 'Bronze 1', 3, 0, 'Silver 3', 3, 0)
# add_player('Shirosensei', 'Bruh', 3, 0, 'Silver 3', 3, 0, 'Silver 3', 3, 0)
# add_player('Jellaz', 'Silver 3', 3, 0, 'Silver 3', 3, 0, 'Gold 3', 3, 0)


#testing
# c.execute('SELECT * FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':'Gondr'})
# result = c.fetchone()
# print(result)

# add_Support_Loss('Gondr')

# add_Support_Loss('Gondor')

# update_Support_Rank('Gay', 'Gay')

# update_Support_Rank('Gondor', 'Gold 5')

# c.execute('SELECT * FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':'Gondor'})
# result = c.fetchone()
# print(result)

# check_player('Gondor')
# c.execute('SELECT * FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':'Gondor'})
# result = c.fetchone()
# print(result)

# add_Tank_Win('Gondor')
# c.execute('SELECT * FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':'Gondor'})
# result = c.fetchone()
# print(result)
# check_player('Gondor')
# c.execute('SELECT * FROM Overwatch_Rank_Tracker WHERE Name = :Name',{'Name':'Gondor'})
# result = c.fetchone()
# print(result)


# conn.commit()
# conn.close()