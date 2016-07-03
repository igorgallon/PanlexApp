# Classe Main de Panlex App - 2016
# Somente para testes com as estruturas de classes criadas

#from Controller import Controller
from Controller2 import *
from Task import Task
from DB import DB
import time
import datetime

print('Inicia controller e lista todos os users no BD e tasks')
inicia()

print('Cria usuario joaozinho')
createUser('Joaozinho', 3, 8)

print('Usuarios:')
user = listUser()
print('printa')

user[0].get_username

deadline = datetime.datetime.now() + datetime.timedelta(10)

print ('Adicionando tasks...')
print(createTask('hehehe', 5, deadline, 10))
print(createTask('hahah', 9, deadline, 9))
print(createTask('uhuhuh', 6, deadline, 5))
print(createTask('hohoh', 3, deadline, 10))

print ('Mostra Tasks do BD...')
# t é lista de tasks do BD
t = listTask()

print ('Criando subtask')
t[0].createSubTask('Eu sou uma subtask da Task 0', 8)
t[0].createSubTask('Eu sou uma subtask da Task 0', 3)

t[1].createSubTask('Eu sou uma subtask da Task 1', 5)
t[1].createSubTask('Eu sou uma subtask da Task 1', 6)

t[2].createSubTask('Eu sou uma subtask da Task 2', 3)
t[2].createSubTask('Eu sou uma subtask da Task 2', 4)
t[2].createSubTask('Eu sou uma subtask da Task 2', 1)

print('Mostra SubTask do BD da Task 1...')
t[1].listSubTask()

print('Mostra SubTask do BD da Task 2...')
t[2].listSubTask()

#print ('Deletar Task 2')
#print (ctr.deleteTask(2))

#print ('Mostra Tasks do BD depois de excluir Task 2')
#ctr.listTask()

#print ('Editar Task 1')
#print (ctr.editTask(1,'Olar', 3, deadline, 10, 10))

#print ('Mostra Tasks do BD depois de editar Task 1')
#ctr.listTask()

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