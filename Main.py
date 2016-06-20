# Classe Main de Panlex App - 2016
# Somente para testes com as estruturas de classes criadas

from User import User
from Task import Task
import time
import datetime

user = User('Igor Gallon', 5, 10)

print('Usuario: ')
user.get_info()

deadline = datetime.datetime.now()
subtask = 'nada'

user.createTask('hehehe', 5, deadline, 10, subtask)
user.createTask('hahah', 9, deadline, 9, subtask)
user.createTask('uhuhuh', 6, deadline, 5, subtask)
user.createTask('hohoh', 3, deadline, 10, subtask)

print ('Mostra BD')
user.selectTask()

#t1 = Task(str(datetime.datetime.now()), 'auhau', 15, datetime.datetime.now(), 10, 'nenhuma')
#t1.get_info()
#print (t1.get_idTask())
#t2 = Task(str(datetime.datetime.now()), '91818', 9, datetime.datetime.now(), 8, 'nenhuma')
#t2.get_info()
#t2.get_idTask()
#print (t2.get_idTask())
#t3 = Task(str(datetime.datetime.now()), 'blabla', 2, datetime.datetime.now(), 5, 'nenhuma')
#t3.get_info()
#t3.get_idTask()
#print (t3.get_idTask())
#t4 = Task(str(datetime.datetime.now()), 'hoho', 6, datetime.datetime.now(), 9, 'nenhuma')
#t4.get_info()
#t4.get_idTask()
#print (t4.get_idTask())