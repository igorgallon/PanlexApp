''' Classe Usuário
    name: Nome do usuário
    numTasksDaily: Número máximo de tarefas que o usuário quer executar diariamente
    workloadDaily: Quantidade de horas diárias para executar as tarefas (em horas)  
'''

class User:
    
    def __init__ (self, name, numTasksDaily, workloadDaily):
        self.__name = name
        self.__numTasksDaily = numTasksDaily
        self.__worloadDaily = workloadDaily