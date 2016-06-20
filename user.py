# Classe User de Panlex App - 2016

import time
import datetime

from Task import Task
from DB import DB

class User:
    
    def __init__ (self, name, numTasksDaily, workloadDaily):
        
        # Inicializando Banco de Dados
        DB.__init__(self)
        DB.create(self)
        
        self.__name = name
        self.__numTasksDaily = numTasksDaily
        self.__workloadDaily = workloadDaily
        
    # Metodos set
    
    def set_name(self, name):
        self.__name = name
        
    def set_numTasksDaily(self, numTaksDaily):
        self.__numTasksDaily = numTasksDaily
    
    def set_workloadDaily(self, workloadDaily):
        self.__workloadDaily = workloadDaily
        
    # Metodos get
    
    def get_name(self):
        return self.__name
    
    def get_numTasksDaily(self):
        return self.__numTasksDaily
    
    def get_workloadDaily(self):
        return self.__workloadDaily
    
    def get_info(self):
        print (self.__name, self.__numTasksDaily, self.__workloadDaily)
    
    name = property(fget=get_name, fset=set_name)
    numTasksDaily = property(fget=get_numTasksDaily, fset=set_numTasksDaily)
    workloadDaily = property(fget=get_workloadDaily, fset=set_workloadDaily)
        
    # Metodos para manipulacao de Tasks
    
    def createTask(self, description, workload, deadline, priority, subtask):
        creationDate = datetime.datetime.now()
        task = Task(creationDate, description, workload, deadline, priority, subtask)
        # Colocar num vetor de task
        
        # Salvar task no Banco de Dados...
        DB.insert(self, task.get_idTask(), creationDate, description, workload, deadline, priority, subtask)

        return task
    
    def selectTask(self):
        return DB.select(self)
        
        
#    def deleteTask(task):
#       del task
        # Deletar task no Banco de Dados...
        
    #def editTask(task):
        # Procurar task e editar no Banco de Dados...