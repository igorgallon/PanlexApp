''' Classe Usu�rio
    name: Nome do usu�rio
    numTasksDaily: N�mero m�ximo de tarefas que o usu�rio quer executar diariamente
    workloadDaily: Quantidade de horas di�rias para executar as tarefas (em horas)  
'''

class User:
    
    def __init__ (self, name, numTasksDaily, workloadDaily):
        self.__name = name
        self.__numTasksDaily = numTasksDaily
        self.__worloadDaily = workloadDaily