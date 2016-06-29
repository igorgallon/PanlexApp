# Classe Controller de Panlex App - 2016

import time
from datetime import datetime

from Task import Task
from DB import DB
from User import User

class Controller:    
    
    def __init__ (self):
        
        # Inicializando Banco de Dados
        DB.__init__(self)
        DB.createTask(self) # Cria tabela para Tasks
        DB.createSubTask(self) # Cria tabela para SubTasks
        DB.createUserSettings(self) # Cria tabela para armazenar informacoes do usuario
        
        # Inicializacao de listas de objetos que serao instanciados
        self.__taskList = []
        self.__userList = []
        self.__subTaskList = []
        
        # Inicializa Usuario contido no Banco de Dados
        Controller.listUser(self)
        
        # Inicializa todas as Tasks contidas no Banco de Dados
        Controller.listTask(self)

    # --- Metodos para manipulacao de Tasks ---
    
    def createTask(self, description, workload, deadline, priority):
        
        # Instancia objeto passando os parametros
        task = Task(description, workload, deadline, priority)
        
        # Procura max idTask do Banco
        task_counter = DB.selectIdTask(self)

        if(task_counter is None):
            idTask = 0
        else:
            idTask = task_counter+1
        
        # Salva idTask na Task instanciada
        task.set_idTask(idTask)
        
        # Adiciona numa lista de Tasks
        self.__taskList.append(task)
        
        # Salvar task no Banco de Dados...
        DB.insertTask(self, task.get_idTask(), task.get_creationDate(), description, workload, deadline, priority, task.get_done(), task.get_weight())
        
        return  self.__taskList
    
    # Recupera tuplas do BD e instancia em lista de objetos
    def listTask(self):
        
        tasks = DB.selectTask(self)
        
        for i in range(0, len(tasks)):
            cd = datetime.strptime(tasks[i][1], '%Y-%m-%d %H:%M:%S.%f') # To datetime
            dl = datetime.strptime(tasks[i][4], '%Y-%m-%d %H:%M:%S.%f') 
            
            t = Task(tasks[i][2], tasks[i][3], dl, tasks[i][5])

            t.set_idTask(int(tasks[i][0]))
            t.set_creationDate(cd)
            t.set_done(int(tasks[i][6]))
            t.set_weight()

            t.get_info()

            self.__taskList.append(t)
            
        return self.__taskList
    
    def deleteTask(self, idTask):
        # Deletar task no Banco de Dados...
        DB.deleteTask(self, idTask)
        
        # Remove da lista de Tasks
        self.__taskList.pop(idTask)
        
        return self.__taskList
        
    def editTask(self,idTask,description, workload, deadline, priority, done):
        # Atualizar informacoes na lista de objetos de Task
        self.__taskList[idTask].set_info(description, workload, deadline, priority, done)
        
        new_Weight = self.__taskList[idTask].get_weight()

        # Procurar task e editar no Banco de Dados...
        DB.updateTask(self, idTask, description, workload, deadline, priority, done, new_Weight)
        
        return self.__taskList[idTask]
    
    # --- Metodos para manipulacao de User ---
    
    def createUser(self,username, numTasksDaily, workloadDaily):
        # Instancia objeto user
        user = User(username, numTasksDaily, workloadDaily)
        
        self.__userList.append(user)
        
        # Insere usuario no BD
        DB.insertUserSettings(self, username, numTasksDaily, workloadDaily)
        
        #return self.__userList
    
    # Recupera usuarios e instancia em lista de objetos
    def listUser(self):
        users = DB.selectUserSettings(self)
        
        for i in range(0, len(users)):
            u = User(users[i][0], users[i][1], users[i][2])
            u.get_info()
            self.__userList.append(u)
            
        return self.__userList
    
    def editUser(self, username, numTasksDaily, workloadDaily):
        
        self.__userList.set_info(username, numTasksDaily, workloadDaily)
        
        DB.updateUserSettings(self, username, numTasksDaily, workloadDaily)
        
        return self.__userList
    
    def deleteUser(self, username):
        # Deletar User no Banco de Dados...
        DB.deleteUserSettings(self, username)
        
        # Remove da lista de User
        self.__userList.pop()
           
        return self.__userList
    
        