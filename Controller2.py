# Classe Controller de Panlex App - 2016

import time
from datetime import datetime

from Task import Task
from DB import DB
from User import User

userList = []
taskList = []

def inicia():

    db = DB()
    
    db.dropTables()
    
    # Inicializando Banco de Dados
    db.__init__()
    db.createTask() # Cria tabela para Tasks
    db.createSubTask() # Cria tabela para SubTasks
    db.createUserSettings() # Cria tabela para armazenar informacoes do usuario
    
    # Inicializa Usuario contido no Banco de Dados
    userList = listUser()
    
    # Inicializa todas as Tasks contidas no Banco de Dados
    taskList = listTask()

# --- Metodos para manipulacao de Tasks ---

def createTask(description, workload, deadline, priority):
    db = DB()
    
    # Instancia objeto passando os parametros
    task = Task(description, workload, deadline, priority)
    
    # Procura max idTask do Banco
    task_counter = db.selectIdTask()

    if(task_counter is None):
        idTask = 0
    else:
        idTask = task_counter+1
    
    # Salva idTask na Task instanciada
    task.set_idTask(idTask)
    
    # Adiciona numa lista de Tasks
    taskList.append(task)
    
    # Salvar task no Banco de Dados...
    db.insertTask(task.get_idTask(), task.get_creationDate(), description, workload, deadline, priority, task.get_done(), task.get_weight())

# Recupera tuplas do BD e instancia em lista de objetos
def listTask():
    
    taskList = []
    
    db = DB()

    tasks = db.selectTask()
    
    for i in range(0, len(tasks)):
        cd = datetime.strptime(tasks[i][1], '%Y-%m-%d %H:%M:%S.%f') # To datetime
        dl = datetime.strptime(tasks[i][4], '%Y-%m-%d %H:%M:%S.%f') 
        
        t = Task(tasks[i][2], tasks[i][3], dl, tasks[i][5])

        t.set_idTask(int(tasks[i][0]))
        t.set_creationDate(cd)
        t.set_done(int(tasks[i][6]))
        t.set_weight()

        t.get_info()
        
        taskList.append(t)
    
    return taskList

def deleteTask(idTask):
    db = DB()
    
    # Deletar task no Banco de Dados...
    db.deleteTask(idTask)
    
    # Remove da lista de Tasks
    if len(__taskList) != 0:
        self.__taskList.pop(idTask)
    
def editTask(idTask, description, workload, deadline, priority, done):
    db = DB()
    # Atualizar informacoes na lista de objetos de Task
    taskList[idTask].set_info(description, workload, deadline, priority, done)
    
    new_Weight = taskList[idTask].get_weight()

    # Procurar task e editar no Banco de Dados...
    db.updateTask(idTask, description, workload, deadline, priority, done, new_Weight)

# --- Metodos para manipulacao de User ---

def createUser(username, numTasksDaily, workloadDaily):
    db = DB()
    # Instancia objeto user
    user = User(username, numTasksDaily, workloadDaily)
    
    userList.append(user)
    
    # Insere usuario no BD
    db.insertUserSettings(username, numTasksDaily, workloadDaily)

# Recupera usuarios e instancia em lista de objetos
def listUser():
    
    userList = []
    
    db = DB()

    users = db.selectUserSettings()
    
    for i in range(0, len(users)):
        u = User(users[i][0], users[i][1], users[i][2])
        userList.append(u)
        
    return userList

def editUser(username, numTasksDaily, workloadDaily):
    db = DB()
    
    userList[0].set_info(username, numTasksDaily, workloadDaily)
    
    db.updateUserSettings(username, numTasksDaily, workloadDaily)

def deleteUser(username):
    db = DB()
    
    # Deletar User no Banco de Dados...
    db.deleteUserSettings(username)
    
    # Remove da lista de User
    if len(userList) != 0:
        userList.pop(0)  