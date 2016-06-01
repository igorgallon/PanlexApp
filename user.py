import time
import datetime

from task import Task

class User:
    
    def __init__ (self, name, numTasksDaily, workloadDaily):
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
    
    def get__numTasksDaily(self):
        return self.__numTasksDaily
    
    def get_workloadDaily(self):
        return self.__workloadDaily
    
    # Metodos para manipulacao de tarefas
    
    def createTask(self, description, workload, deadline, priority, subtask):
        creationDate = datetime.datetime.now()
        task = Task(creationDate, description, workload, deadline, priority, subtask)
        return task
        # Salvar task no Banco de Dados...
        
    def deleteTask(task):
        del task
        # Deletar task no Banco de Dados...
        
    #def editTask(task):
        # Procurar task e editar no Banco de Dados...