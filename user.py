''' Classe Usu�rio
    name: Nome do usu�rio
    numTasksDaily: N�mero m�ximo de tarefas que o usu�rio quer executar diariamente
    workloadDaily: Quantidade de horas di�rias para executar as tarefas (em horas)  
'''
import time
import datetime

class User:
    
    def __init__ (self, name, numTasksDaily, workloadDaily):
        self.__name = name
        self.__numTasksDaily = numTasksDaily
        self.__workloadDaily = workloadDaily
        
    # M�todos set
    
    def set_name(self, name):
        self.__name = name
        
    def set_numTasksDaily(self, numTaksDaily):
        self.__numTasksDaily = numTasksDaily
    
    def set_workloadDaily(self, workloadDaily):
        self.__workloadDaily = workloadDaily
        
    # M�todos get
    
    def get_name(self):
        return self.__name
    
    def get__numTasksDaily(self):
        return self.__numTasksDaily
    
    def get_workloadDaily(self):
        return self.__workloadDaily
    
    # M�todos para manipulacao de tarefas
    
    def createTask(description, workload, deadline, priority, subtask):
        creationDate = datetime.datetime.now()
        done = 0
        task = Task(creationDate, description, workload, deadline, priority, subtask, done)
        # Salvar task no Banco de Dados!
        
    def deleteTask(task):
        del task
        # Deletar task no Banco de Dados!
        
    #def editTask(task):
        # Procurar task e editar no Banco de Dados!
        
        