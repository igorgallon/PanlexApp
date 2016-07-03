# Classe Panlex de Panlex App - 2016
# Gerenciador da interface grafica
from Controller import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty

ctr = ControllerSingleton()

class InitialScreen(Screen):
    # Tela inicial do aplicativo
    pass

class SeeTasksScreen(Screen):
    # Lista todas as Tasks que o usuario possui
    pass

class TaskInfoScreen(Screen):
    # Exibe informacoes de uma Task
    pass

class EditTaskScreen(Screen):
    # Edita as especificacoes de uma Task
    #    - Workload;
    #    - Deadline;
    #    - Prioridade;
    #    - Descricao;
    #    - Excluir task.
    pass

class NewTaskScreen(Screen):
    # Cria task
    # - Description
    # - Workload
    # - Deadline
    # - Priority
    description = StringProperty()
    workload = StringProperty()
    deadline = StringProperty()
    priority = StringProperty()

    def __init__(self, **kwargs):
        super(NewTaskScreen, self).__init__(**kwargs)
        self.clear()

    def clear(self):
        self.description = ''
        self.workload = ''
        self.deadline = ''
        self.priority = ''

    def ok_button(self):
        self.description = self.ids['id_description'].text
        self.workload = self.ids['id_workload'].text
        self.deadline = self.ids['id_deadline'].text
        self.priority = self.ids['id_priority'].text
        # Nao adiciona Task se campos estiverem vazios
        if self.description and self.workload and self.deadline and self.priority:
            strDeadline = datetime.strptime(self.deadline, '%Y-%m-%d')
            # Deadline so importa a data, hora nao precisa
            strDeadline.replace(hour=0, minute=0, second=0)
            ctr.createTask(self.description, int(self.workload), strDeadline, int(self.priority))
            ctr.listTaskInfo()
        self.clear()

class SettingsScreen(Screen):
    # Exibe informacoes atuais do usuario:
    # - Username
    # - Workload daily
    # - Number of daily tasks
    username = StringProperty()
    workload = StringProperty()
    numtasks = StringProperty()

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.update()

    def update(self):
        if len(ctr.userList) != 0:
            self.username = ctr.userList[0].get_username()
            self.workload = str(ctr.userList[0].get_workloadDaily())
            self.numtasks = str(ctr.userList[0].get_numTasksDaily())
            print('Inicia settings', self.username, self.workload, self.numtasks)
        else:
            self.username = 'None'
            self.workload = 'None'
            self.numtasks = 'None'
        
class EditSettingsScreen(Screen):
    # Editar informacoes de usuario:
    # - Username
    # - Workload daily
    # - Number of daily Tasks
    username = StringProperty()
    workload = StringProperty()
    numtasks = StringProperty()
    
    def __init__(self, **kwargs):
        super(EditSettingsScreen, self).__init__(**kwargs)
        self.update()

    def update(self):
        if len(ctr.userList) != 0:
            self.username = ctr.userList[0].get_username()
            self.workload = str(ctr.userList[0].get_workloadDaily())
            self.numtasks = str(ctr.userList[0].get_numTasksDaily())
        else:
            self.username = 'None'
            self.workload = 'None'
            self.numtasks = 'None'
            
    def ok_button(self):
        self.username = self.ids['id_username'].text
        self.workload = self.ids['id_workload'].text
        self.numtasks = self.ids['id_numtasks'].text

        if len(ctr.userList) != 0:
            ctr.editUser(self.username, int(self.numtasks), int(self.workload))
            print(ctr.userList[0].get_username(), ctr.userList[0].get_workloadDaily(), ctr.userList[0].get_numTasksDaily())
        else:
            ctr.createUser(self.username, int(self.numtasks), int(self.workload))

        self.manager.get_screen('settings').update()
        
class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("ScreensPanlex.kv")

class PanlexApp(App):
        
    def build(self):
        return presentation

if __name__ == '__main__':
    PanlexApp().run()