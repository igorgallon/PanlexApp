# Classe Controller de Panlex App - 2016

import time
import datetime

from Task import Task
from DB import DB

class Controller:    
    
    def __init__ (self, username, numTasksDaily, workloadDaily):
        
        # Inicializando Banco de Dados
        DB.__init__(self)
        DB.createTask(self) # Cria tabela para Tasks
        DB.createSubTask(self) # Cria tabela para SubTasks
        DB.createUserSettings(self) # Cria tabela para armazenar informacoes do usuario

        self.__username = username
        self.__numTasksDaily = numTasksDaily
        self.__workloadDaily = workloadDaily        
        
        self.__taskList = []
        
        # Salva informacoes do usuario no Banco de Dados
        DB.insertUserSettings(self, self.__username, self.__numTasksDaily, self.__workloadDaily)
        
    # Metodos set
    
    def set_username(self, name):
        self.__username = name
        DB.insertUserSettings(self, self.__username, self.__numTasksDaily, self.__workloadDaily)
        
    def set_numTasksDaily(self, numTaksDaily):
        self.__numTasksDaily = numTasksDaily
        DB.insertUserSettings(self, self.__username, self.__numTasksDaily, self.__workloadDaily)
    
    def set_workloadDaily(self, workloadDaily):
        self.__workloadDaily = workloadDaily
        DB.insertUserSettings(self, self.__username, self.__numTasksDaily, self.__workloadDaily)
        
    # Metodos get
    
    def get_username(self):
        return self.__username
    
    def get_numTasksDaily(self):
        return self.__numTasksDaily
    
    def get_workloadDaily(self):
        return self.__workloadDaily
    
    def get_info(self):
        print (self.__username, self.__numTasksDaily, self.__workloadDaily)
        
    # Metodos para manipulacao de Tasks
    
    def createTask(self, description, workload, deadline, priority):
        
        # Instancia objeto passando os parametros
        task = Task(description, workload, deadline, priority)
        
        # Adiciona numa lista de Tasks
        self.__taskList.append(task)
        
        # Salvar task no Banco de Dados...
        DB.insertTask(self, task.get_idTask(), task.get_creationDate(), description, workload, deadline, priority, task.get_weight())

        return  self.__taskList
    
    def selectTask(self):
        return DB.selectTask(self)
                
    def deleteTask(self, idTask):
        # Deletar task no Banco de Dados...
        DB.deleteTask(self, idTask)
        
        # Remove da lista de Tasks
        self.__taskList.pop(idTask)
        
        return self.__taskList
        
    def editTask(self,idTask,description, workload, deadline, priority, weight):
        # Procurar task e editar no Banco de Dados...
        DB.updateTask(self,idTask,description,workload,deadline,priority,weight)