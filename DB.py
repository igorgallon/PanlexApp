import sqlite3

class DB:
    
    # Inicia Banco de Dados no arquivo db_tasks.db
    def __init__(self):
        self.__conexao=sqlite3.connect("db_tasks.db")

    # Remove conexao com Bando de Dados
    def __del__(self):
        self.__db.close()        
    
    # Cria tabela Task no Banco de Dados, tendo idTask como PK
    def create(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''drop table if exists Task''')    
        cursor.execute('''create table if not exists Task(idTask int PRIMARY KEY,creationDate text,description text,workload int,deadline text,priority int,subtask text)''')  
        cursor.close()
        self.__conexao.commit()        
    
    # Insere tuplas na tabela Task
    def insert(self, idTask, creationDate, description, workload, deadline, priority, subtask):
        cursor = self.__conexao.cursor()
        cursor.execute('''INSERT into Task VALUES(?,?,?,?,?,?,?)''', [idTask, str(creationDate), description, workload, str(deadline), priority, subtask])
        cursor.close()
        self.__conexao.commit()        
    
    # Lista todas as tuplas da tabela Task em ordem crescente de idTask
    def select(self):
        cursor = self.__conexao.cursor()
        for row in cursor.execute('SELECT * FROM Task ORDER BY idTask'):
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        cursor.close()
        self.__conexao.commit()
    
    # Atualiza tuplas da tabela Task - buscando pelo idTask, sobrescreve campos nao editados
    def update(self, idTask, creationDate, description, workload, deadline, priority, subtask):
        cursor = self.__conexao.cursor()
        cursor.execute('''update Task 
                       set creationDate = ?, description = ?, workload = ?, deadline = ?, priority = ?, subtask = ? where idTask = ?''',
                       [str(creationDate), description, workload, str(deadline), priority, subtask, idTask])
        self.__conexao.commit()
    
    # Remove tupla pelo idTask da tabela Task
    def delete(self, idTask):
        cursor = self.__conexao.cursor()
        cursor.execute('''delete from Task where idTask = ?''', [idTask])
        self.__conexao.commit()