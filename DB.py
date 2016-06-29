import sqlite3

class DB:
    
    # Inicia Banco de Dados no arquivo db_tasks.db
    def __init__(self):
        self.__conexao=sqlite3.connect("db_panlex.db")

    # Remove conexao com Bando de Dados
    def __del__(self):
        self.__db.close()
    
    # Cria tabela Task no Banco de Dados, tendo idTask como PK
    def createTask(self):
        cursor = self.__conexao.cursor()
        #cursor.execute('''DROP TABLE IF EXISTS Task''') # Exclui tabela anterior em BD
        cursor.execute('''CREATE TABLE IF NOT EXISTS Task(idTask int PRIMARY KEY,
        creationDate text,description text,workload int,deadline text,priority int, done int, weight real)''')  
        cursor.close()
        self.__conexao.commit()
        
    # Cria tabela SubTask no Banco de Dados, tendo idSubTask como FK de Task
    def createSubTask(self):
        cursor = self.__conexao.cursor()
        #cursor.execute(''' DROP TABLE IF EXISTS SubTask ''') # Exclui tabela anterior em BD
        cursor.execute(''' CREATE TABLE IF NOT EXISTS SubTask(idTask int, idSubTask int, description text, done int,
                           FOREIGN KEY(idTask) REFERENCES Task(idTask)
                           PRIMARY KEY(idTask, idSubTask))''')
        cursor.close()
        self.__conexao.commit() 

    # Cria tabela que armazena configuracoes do Usuario
    def createUserSettings(self):
        cursor = self.__conexao.cursor()
        #cursor.execute('''DROP TABLE IF EXISTS User''') # Exclui tabela anterior em BD
        cursor.execute('''CREATE TABLE IF NOT EXISTS User(username text, numTasksDaily int, workloadDaily int)''')  
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
        cursor.execute('''INSERT INTO User VALUES(?,?,?)''', [username, numTasksDaily, workloadDaily])
        cursor.close()
        self.__conexao.commit()     
    
    # Lista todas as tuplas da tabela Task em ordem crescente de idTask
    def selectTask(self):
        tasks = []
        cursor = self.__conexao.cursor()
        for row in cursor.execute('SELECT * FROM Task ORDER BY idTask'):
            #print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            tasks.append(row)    
        cursor.close()
        self.__conexao.commit()
        return tasks
    
    # Lista todas as tuplas da tabela SubTask para uma determinada Task de idTask
    def selectSubTask(self, idTask):
        subTask = []
        cursor = self.__conexao.cursor()
        for row in cursor.execute('''SELECT * FROM SubTask WHERE idTask = ? ORDER by idSubTask''', [idTask]):
            #print(row[0], row[1], row[2], row[3])
            subTask.append(row)
        cursor.close()
        self.__conexao.commit()
        return subTask

    # Lista as informacoes do usuario
    def selectUserSettings(self):
        user = []
        cursor = self.__conexao.cursor()
        for row in cursor.execute('SELECT * FROM User'):
            #print(row[0], row[1], row[2])
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
        cursor.execute('''UPDATE User SET username = ?, numTaskDaily = ?, worloadDaily = ? WHERE username = ?''',
                        [username, numTasksDaily, workloadDaily, username])
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
    def deleteUserSettings(self, username):
        cursor = self.__conexao.cursor()
        cursor.execute('''DELETE FROM User WHERE username LIKE ? ''', [username])
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