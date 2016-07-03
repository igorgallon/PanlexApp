# Classe Main de Panlex App - 2016
# Somente para testes com as estruturas de classes criadas

from Task import Task
from DB import DB
import time
import datetime
from Controller import Controller

print('Inicia controller e lista todos os users no BD e tasks')

ctr = Controller()

print('Cria usuario jarbas')
ctr.createUser('Jarbas', 5, 10)

print('Usuarios:')
user = ctr.listUser()

#print('Deleta joaozionho')
#ctr.deleteUser('Joaozinho')

print('mostra users')
ctr.listUserInfo()

deadline = datetime.datetime.now() + datetime.timedelta(10)

print ('Adicionando tasks...')
print(ctr.createTask('hehehe', 5, deadline, 10))
print(ctr.createTask('hahah', 9, deadline, 9))
print(ctr.createTask('uhuhuh', 6, deadline, 5))
print(ctr.createTask('hohoh', 3, deadline, 10))

print ('Mostra Tasks do BD...')
# t eh lista de tasks do BD
t = ctr.listTask()

print ('Deletar Task id=2')
print (ctr.deleteTask(2))

print ('Deletar Task id=1')
print (ctr.deleteTask(1))

print ('Mostra Tasks do BD depois de excluir Task id=2 e id=1')
ctr.listTaskInfo()

print ('Editar Task id=3')
print (ctr.editTask(3,'eu sou a  tres', 3, deadline, 10, 10))

print ('Mostra Tasks do BD depois de editar Task 1')
ctr.listTaskInfo()

print(ctr.createTask('hehehe', 5, deadline, 10))
print(ctr.createTask('hahah', 9, deadline, 9))
print(ctr.createTask('uhuhuh', 6, deadline, 5))
print(ctr.createTask('hohoh', 3, deadline, 10))

print('Lista tudo')
ctr.listTaskInfo()

print ('Deletar Task id=6')
print (ctr.deleteTask(6))

print('Lista tudo')
ctr.listTaskInfo()

print('Editar a task de id = 5')
print (ctr.editTask(5,'eu sou a cinco', 3, deadline, 10, 10))

print('Lista tudo')
ctr.listTaskInfo()

# print ('Criando subtask')
t[0].createSubTask('Eu sou uma subtask da Task 0', 8)
t[0].createSubTask('Eu sou uma subtask da Task 0', 3)

t[1].createSubTask('Eu sou uma subtask da Task 1', 5)
t[1].createSubTask('Eu sou uma subtask da Task 1', 6)

t[2].createSubTask('Eu sou uma subtask da Task 2', 3)
t[2].createSubTask('Eu sou uma subtask da Task 2', 4)
t[2].createSubTask('Eu sou uma subtask da Task 2', 1)

print('Mostra SubTask do BD da Task 1...')
t[1].listSubTaskInfo()

print('Mostra SubTask do BD da Task 2...')
t[2].listSubTaskInfo()

print('Mostra SubTask do BD da Task 0...')
t[0].listSubTaskInfo()

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