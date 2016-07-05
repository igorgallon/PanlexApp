# Classe Panlex de Panlex App - 2016
# Gerenciador da interface grafica
import datetime
from Controller import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.uix.button import Button
from Task import Task

ctr = ControllerSingleton()
idTask = 0
class InitialScreen(Screen):
    # Tela inicial do aplicativo
    pass

class SeeTasksScreen(Screen):
    pass

class TaskInfoScreen(Screen):
    # Exibe informacoes de uma Task
    description = StringProperty()
    descriptionShow = StringProperty()
    workload = StringProperty()
    deadline = StringProperty()
    priority = StringProperty()
    creation = StringProperty()
    done = StringProperty()

    def __init__(self, **kwargs):
        super(TaskInfoScreen, self).__init__(**kwargs)
        self.setLabel()

    def setLabel(self):
        ID = int(idTask)
        for x in ctr.taskList:
            if x.get_idTask() == ID:
                self.description = x.get_description()
                self.descriptionShow = self.description[:20]+'...'
                self.workload = str(x.get_workload())
                self.deadline = str(x.get_deadline())[:10]
                self.priority = str(x.get_priority())
                self.creation = str(x.get_creationDate())[:10]
                self.done = str(x.get_done())

    def update(self):
        self.manager.get_screen('edittask').update()

class EditTaskScreen(Screen):
    # Edita as especificacoes de uma Task
    #    - Workload;
    #    - Deadline;
    #    - Prioridade;
    #    - Descricao;
    #    - Excluir task.

    description = StringProperty()
    workload = StringProperty()
    deadline = StringProperty()
    priority = StringProperty()
    done = StringProperty()

    def __init__(self, **kwargs):
        super(EditTaskScreen, self).__init__(**kwargs)
        self.update()

    def update(self):
        for x in ctr.taskList:
            if x.get_idTask() == idTask:
                self.description = x.get_description()
                self.workload = str(x.get_workload())
                self.deadline = str(x.get_deadline())[0:10]
                self.priority = str(x.get_priority())
                self.done = str(x.get_done())

    def ok_button(self):
        self.description = self.ids['id_description'].text
        self.workload = self.ids['id_workload'].text
        self.deadline = self.ids['id_deadline'].text
        self.priority = self.ids['id_priority'].text
        self.done = self.ids['id_done'].text

        if self.description and self.workload and self.deadline and self.priority and self.done:
            str = self.deadline + ' 00:00:00.000001'
            strDeadline = datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')
            ctr.editTask(idTask, self.description, int(self.workload), strDeadline, int(self.priority), int(self.done))
            self.update()

    def del_button(self):
        ctr.deleteTask(idTask)

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
            str = self.deadline + ' 00:00:00.000001'
            strDeadline = datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')
            # Deadline so importa a data, hora nao precisa
            ctr.createTask(self.description, int(self.workload), strDeadline, int(self.priority))
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
        else:
            ctr.createUser(self.username, int(self.numtasks), int(self.workload))

        self.manager.get_screen('settings').update()
        
class ScreenManagement(ScreenManager):
    pass

class TaskViewer(GridLayout):
    pass

Builder.load_file("ScreensPanlex.kv")

sm = ScreenManagement()

sm.add_widget(InitialScreen(name='initial'))
sm.add_widget(EditTaskScreen(name='edittask'))
sm.add_widget(NewTaskScreen(name='newtask'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(EditSettingsScreen(name='editsettings'))
sm.add_widget(SeeTasksScreen(name='seetasks'))
sm.add_widget(TaskInfoScreen(name='taskinfo'))

class PanlexApp(App):

    def build(self):
        return sm

    def change_screen(self, idtask, nothing):

        global idTask
        idTask = idtask
        taskinfo = TaskInfoScreen()
        sm.add_widget(taskinfo)
        App.get_running_app().root.current = sm.next()
        x = TaskInfoScreen()
        sm.switch_to(x)

    def view_tasks(self, root):
        if root.ids["task_panel"].children:
            root.ids["task_panel"].clear_widgets()
        task_view = TaskViewer()
        root.ids['task_panel'].add_widget(task_view)

        buttonList = []

        tasks = sorted(ctr.taskList, key=lambda y: y.get_weight(), reverse=True)

        for x in tasks:
            nameInfo = x.get_description()[:35]+'...' + ' Urgency: ' + str(int(x.get_weight()))
            buttonList.append(Button(id=str(x.get_idTask()), text=nameInfo, size=(600, 60), size_hint=(None, None)))
            task_view.add_widget(buttonList[len(buttonList) - 1])
            change_screen = partial(self.change_screen, x.get_idTask())
            buttonList[len(buttonList) - 1].bind(on_press=change_screen)

if __name__ == '__main__':
    PanlexApp().run()