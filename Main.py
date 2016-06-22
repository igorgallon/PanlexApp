# Classe Main de Panlex App - 2016
# Somente para testes com as estruturas de classes criadas

from Controller import Controller
from Task import Task
import time
import datetime

user = Controller('Igor Gallon', 5, 10)

print('Usuario:')
user.get_info()

#deadline = datetime.datetime(year=2016, month=6, day=24, hour=18, minute=30)
subtask = 'nada'
deadline = datetime.datetime.now() + datetime.timedelta(10)

print(user.createTask('hehehe', 5, deadline, 10))
print(user.createTask('hahah', 9, deadline, 9))
print(user.createTask('uhuhuh', 6, deadline, 5))
print(user.createTask('hohoh', 3, deadline, 10))

print ('Mostra BD')
user.selectTask()

print ('Deletar Task 2')
print(user.deleteTask(2))

print ('Mostra BD')
user.selectTask()

print ('Editar Task 1')
print(user.editTask(1,'Olar', 3, deadline, 10, 10))

print ('Mostra BD')
print(user.selectTask())

#t1 = Task('auhau', 15, deadline, 9, 'nenhuma')
#t1.get_info()
#print (t1.get_idTask())
#t1.set_weight()
#print (t1.get_weight())
#t2 = Task('91818', 9, deadline, 8, 'nenhuma')
#t2.get_info()
#t2.get_idTask()
#print (t2.get_idTask())
#t3 = Task('blabla', 2, deadline, 5, 'nenhuma')
#t3.get_info()
#t3.get_idTask()
#print (t3.get_idTask())
#t4 = Task('hoho', 6, deadline, 9, 'nenhuma')
#t4.get_info()
#t4.get_idTask()
#print (t4.get_idTask())