# import sqlite3
# from functools import wraps

# conn = sqlite3.connect(':memory:')
# c = conn.cursor()

# #Creating Exception Class
# class InvalidName(Exception):
#     pass

# #Creating Name Check Decorator
# def name_check(function):
#     @wraps(function)
#     def wrapper(*args):
#         try:
#             c.execute('SELECT * FROM Person WHERE name = :name',{'name':args[0]})
#             result = c.fetchone()
#             if result is None:
#                 raise InvalidName
#             else:
#                 pass
#         except InvalidName:
#             print('name does not exist')
#         return function(*args)
#     return wrapper

# #Add Person Function
# def add_person(name, age, height, weight):
#     with conn:
#         c.execute('INSERT INTO Person values (:name, :age, :height, :weight)',
#         {'name':name, 'age':age, 'height':height, 'weight':weight})

# #Add Age Function
# @name_check
# def add_age(name):
#     with conn:
#         c.execute('UPDATE Person SET age = age + 1 WHERE name = :name',{'name':name})
#     c.execute('SELECT age FROM PERSON WHERE name = :name',{'name':name})
#     age = c.fetchone()
#     if age != None:
#         for x in age:
#             if x == 22:
#                 with conn:
#                     c.execute('UPDATE Person SET age = 20 WHERE name = :name',{'name':name})
#             else:
#                 pass
#     else:
#         pass

# #Creating Table
# c.execute('''CREATE TABLE IF NOT EXISTS Person (
#             {0} text,
#             {1} integer,
#             {2} text,
#             {3} text
#             )'''.format('name', 'age', 'height', 'weight'))

# #Testing Commands
# add_person('James', 20, '170cm', '60kg')
# c.execute('SELECT * FROM Person WHERE name = :name',{'name':'James'})
# result = c.fetchone()
# print(result)

# add_age('John')

# add_age('James')
# c.execute('SELECT * FROM Person WHERE name = :name',{'name':'James'})
# result = c.fetchone()
# print(result)
# add_age('James')
# c.execute('SELECT * FROM Person WHERE name = :name',{'name':'James'})
# result = c.fetchone()
# print(result)

class testexception(Exception):
    pass

def exception():
    raise testexception
