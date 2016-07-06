# Classe Controller de Panlex App - 2016

import time
from datetime import datetime
import math
from Task import Task
from DB import DB
from User import User

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Controller:
        
    def __init__(self):
    
        db = DB()
        
        db.createTask() # Cria tabela para Tasks
        db.createSubTask() # Cria tabela para SubTasks
        db.createUserSettings() # Cria tabela para armazenar informacoes do usuario
        
        # Inicializa Usuario contido no Banco de Dados
        self.userList = self.listUser()
        
        # Inicializa todas as Tasks contidas no Banco de Dados
        self.taskList = self.listTask()

    # --- Metodos para manipulacao de Tasks ---

    def hoursPerTask(self):
        tasks = sorted(self.taskList, key=lambda y: y.get_weight(), reverse=True)
        tasks = tasks[:self.userList[0].get_numTasksDaily()]

        y = 0
        list = []

        if len(tasks) != 0:
            for x in tasks:
                y += x.get_weight()

            hour = self.userList[0].get_workloadDaily() / y

            for x in tasks:
                tup = (str(float("{0:.1f}".format(hour * x.get_weight()))), x.get_description())
                list.append(tup)

        return list

    def createTask(self, description, workload, deadline, priority):
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
        self.taskList.append(task)
        
        # Salvar task no Banco de Dados...
        db.insertTask(task.get_idTask(), task.get_creationDate(), description, workload, deadline, priority, task.get_done(), task.get_weight())
    
    # Recupera tuplas do BD e instancia em lista de objetos
    def listTask(self):
        
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

            taskList.append(t)
        
        return taskList

    def deleteTask(self, idTask):
        db = DB()
        
        # Deletar task no Banco de Dados...
        db.deleteTask(idTask)
        
        # Remove da lista de Tasks
        if len(self.taskList) != 0:
            cnt = 0

            for x in self.taskList:
                if x.get_idTask() == idTask:
                    break
                else:
                    cnt += 1

            self.taskList.pop(cnt)
        
    def editTask(self, idTask, description, workload, deadline, priority, done):
        db = DB()
        cnt = 0
        # Atualizar informacoes na lista de objetos de Task
        for x in self.taskList:
            if x.get_idTask() == idTask:
                x.set_info(description, workload, deadline, priority, done)
                break
            else:
                cnt += 1

        new_Weight = self.taskList[cnt].get_weight()
    
        # Procurar task e editar no Banco de Dados...
        db.updateTask(idTask, description, workload, deadline, priority, done, new_Weight)
    
    # --- Metodos para manipulacao de User ---
    
    def createUser(self, username, numTasksDaily, workloadDaily):
        db = DB()
        # Instancia objeto user
        user = User(username, numTasksDaily, workloadDaily)
        
        self.userList.append(user)
        
        # Insere usuario no BD
        db.insertUserSettings(username, numTasksDaily, workloadDaily)
    
    # Recupera usuarios e instancia em lista de objetos
    def listUser(self):
        
        userList = []
        
        db = DB()
    
        users = db.selectUserSettings()
        
        for i in range(0, len(users)):
            u = User(users[i][1], users[i][2], users[i][3])
            userList.append(u)
            
        return userList
    
    def editUser(self, username, numTasksDaily, workloadDaily):
        db = DB()

        self.userList[0].set_info(username, numTasksDaily, workloadDaily)
        
        db.updateUserSettings(username, numTasksDaily, workloadDaily)
    
    def deleteUser(self):
        db = DB()
        
        # Deletar User no Banco de Dados...
        db.deleteUserSettings()
        
        # Remove da lista de User
        if len(self.userList) != 0:
            self.userList.pop(0)
            
class ControllerSingleton(Controller, metaclass=Singleton):
    pass