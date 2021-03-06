import sqlite3

class DB:
    
    # Inicia Banco de Dados no arquivo db_tasks.db
    def __init__(self):
        self.__conexao=sqlite3.connect("db_panlex.db")

    # Remove conexao com Bando de Dados
    def __del__(self):
        self.__conexao.close()
        
    # Remove todas as tabelas do Banco de Dados
    def dropTables(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''DROP TABLE IF EXISTS Task''') # Exclui tabela anterior em BD
        cursor.execute('''DROP TABLE IF EXISTS SubTask''')
        cursor.execute('''DROP TABLE IF EXISTS User''')
        cursor.close()
        self.__conexao.commit()

    # Remove todas as tabelas do Banco de Dados
    def dropTask(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''DROP TABLE IF EXISTS Task''') # Exclui tabela anterior em BD
        cursor.close()
        self.__conexao.commit()

    # Remove todas as tabelas do Banco de Dados
    def dropSubTask(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''DROP TABLE IF EXISTS SubTask''')
        cursor.close()
        self.__conexao.commit()

    def dropUser(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''DROP TABLE IF EXISTS User''')
        cursor.close()
        self.__conexao.commit()

    # Cria tabela Task no Banco de Dados, tendo idTask como PK
    def createTask(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Task(idTask int PRIMARY KEY,
        creationDate text,description text,workload int,deadline text,priority int, done int, weight real)''')  
        cursor.close()
        self.__conexao.commit()
        
    # Cria tabela SubTask no Banco de Dados, tendo idSubTask como FK de Task
    def createSubTask(self):
        cursor = self.__conexao.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS SubTask(idTask int, idSubTask int, description text, done int,
                           FOREIGN KEY(idTask) REFERENCES Task(idTask)
                           PRIMARY KEY(idTask, idSubTask))''')
        cursor.close()
        self.__conexao.commit() 

    # Cria tabela que armazena configuracoes do Usuario

    def createUserSettings(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS User(idUser int, username text, numTasksDaily int, workloadDaily int)''')
        cursor.close()
        self.__conexao.commit()
    
    # Insere tuplas na tabela Task
    def insertTask(self, idTask, creationDate, description, workload, deadline, priority, done, weight):
        cursor = self.__conexao.cursor()
        cursor.execute('''INSERT INTO Task VALUES(?,?,?,?,?,?,?,?)''',
                       [idTask, creationDate, description, workload, deadline, priority, done, weight])
        cursor.close()
        self.__conexao.commit()
    
    # Insere tuplas na tabela SubTask
    def insertSubTask(self, idTask, idSubTask, description, done):
        cursor = self.__conexao.cursor()
        cursor.execute('''INSERT INTO SubTask VALUES(?,?,?,?)''', [idTask, idSubTask, description, done])
        cursor.close()
        self.__conexao.commit()
    
    # Insere informacoes do usuario
    def insertUserSettings(self, username, numTasksDaily, workloadDaily):
        cursor = self.__conexao.cursor()
        cursor.execute('''INSERT INTO User VALUES(0,?,?,?)''', [username, numTasksDaily, workloadDaily])
        cursor.close()
        self.__conexao.commit()     
    
    # Lista todas as tuplas da tabela Task em ordem crescente de idTask

    def selectTask(self):
        tasks = []
        cursor = self.__conexao.cursor()
        for row in cursor.execute('SELECT * FROM Task ORDER BY idTask'):
            tasks.append(row)    
        cursor.close()
        self.__conexao.commit()
        return tasks
    
    # Lista todas as tuplas da tabela SubTask para uma determinada Task de idTask
    def selectSubTask(self, idTask):
        subTask = []
        cursor = self.__conexao.cursor()
        for row in cursor.execute('''SELECT * FROM SubTask WHERE idTask = ? ORDER by idSubTask''', [idTask]):
            subTask.append(row)
        cursor.close()
        self.__conexao.commit()
        return subTask

    # Lista as informacoes do usuario
    def selectUserSettings(self):
        user = []
        cursor = self.__conexao.cursor()
        for row in cursor.execute('SELECT * FROM User'):
            user.append(row)
        cursor.close()
        self.__conexao.commit()
        return user
        
    # Atualiza tuplas da tabela Task - buscando pelo idTask, sobrescreve campos nao editados
    def updateTask(self, idTask, description, workload, deadline, priority, done, weight):
        cursor = self.__conexao.cursor()
        cursor.execute('''UPDATE Task SET description = ?, workload = ?, deadline = ?, priority = ?, done = ?, weight = ? WHERE idTask = ?''',
                        [description, workload, str(deadline), priority, done, weight, idTask])
        cursor.close()
        self.__conexao.commit()
        
    # Atualiza tuplas da tabela Task - buscando pelo idTask, sobrescreve campos nao editados
    def updateSubTask(self, idTask, idSubTask, description, done):
        cursor = self.__conexao.cursor()
        cursor.execute('''UPDATE SubTask SET description = ?, done = ? WHERE idTask = ? AND idSubTask = ?''',
                        [description, done, idTask, idSubTask])
        cursor.close()
        self.__conexao.commit()

    # Atualiza informacoes do usuario
    def updateUserSettings(self, username, numTasksDaily, workloadDaily):
        cursor = self.__conexao.cursor()
        cursor.execute('''UPDATE User SET username = ?, numTasksDaily = ?, workloadDaily = ? WHERE idUser = 0''',
                        [username, numTasksDaily, workloadDaily])
        cursor.close()
        self.__conexao.commit()

    # Remove tupla pelo idTask da tabela Task
    def deleteTask(self, idTask):
        cursor = self.__conexao.cursor()
        cursor.execute('''DELETE FROM Task WHERE idTask = ?''', [idTask])
        cursor.close()
        self.__conexao.commit()

    # Remove tupla de SubTask pelo idTask e idSubTask
    def deleteSubTask(self, idTask, idSubTask):
        cursor = self.__conexao.cursor()
        cursor.execute('''DELETE FROM SubTask WHERE idTask = ? AND idSubTask = ?''', [idTask, idSubTask])
        cursor.close()
        self.__conexao.commit()
        
    # Remove tupla da tabela User
    def deleteUserSettings(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''DELETE FROM User WHERE idUser = 0 ''')
        cursor.close()
        self.__conexao.commit()
        
    # Retorna maior idTask da Tabela Task
    def selectIdTask(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''SELECT MAX(idTask) FROM Task''')
        idTask = cursor.fetchone()
        cursor.close()
        self.__conexao.commit()
        return idTask[0]
    
    # Retorna maior idSubTask da Tabela SubTask para uma determinada Task
    def selectIdSubTask(self, idTask):
        cursor = self.__conexao.cursor()
        cursor.execute('''SELECT MAX(idSubTask) FROM SubTask WHERE idTask = ?''', [idTask])
        idSubTask = cursor.fetchone()
        cursor.close()
        self.__conexao.commit()
        return idSubTask[0]