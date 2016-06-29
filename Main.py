# Classe Main de Panlex App - 2016
# Somente para testes com as estruturas de classes criadas

from Controller import Controller
from Task import Task
import time
import datetime

print('Inicia controller e lista todos os users no BD e tasks')
ctr = Controller()

#print('Cria usuario jarbas')
#ctr.createUser('Jarbas', 5, 10)

#print('Cria usuario joaozinho')
#ctr.createUser('Joaozinho', 3, 8)

print('Usuarios:')
user = ctr.listUser()

print('Deleta joaozionho')
ctr.deleteUser('Joaozinho')

print('mostra users')
ctr.listUser()

#deadline = datetime.datetime(year=2016, month=6, day=24, hour=18, minute=30)
#subtask = 'nada'
deadline = datetime.datetime.now() + datetime.timedelta(10)

print ('Adicionando tasks...')
print(ctr.createTask('hehehe', 5, deadline, 10))
print(ctr.createTask('hahah', 9, deadline, 9))
print(ctr.createTask('uhuhuh', 6, deadline, 5))
print(ctr.createTask('hohoh', 3, deadline, 10))

print ('Mostra Tasks do BD...')
ctr.listTask()

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