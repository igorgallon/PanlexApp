# Classe Panlex de Panlex App - 2016
# Gerenciador da interface grafica

import datetime
from Controller import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.uix.button import Button

# Intancia Controller global
ctr = ControllerSingleton()

# Variavel global que define em qual Task o usuario selecionou
idTask = 0

class InitialScreen(Screen):
    # Tela inicial do aplicativo
    def updateWorks(self):
        # Atualiza lista de tarefas para trabalhar no dia
        self.manager.get_screen('workday').refresh()

class SeeTasksScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class WorkDayScreen(Screen):
    task1 = StringProperty()
    task2 = StringProperty()
    task3 = StringProperty()
    task4 = StringProperty()
    hours1 = StringProperty()
    hours2 = StringProperty()
    hours3 = StringProperty()
    hours4 = StringProperty()

    # Executado sempre quando a Screen eh iniciada
    def __init__(self, **kwargs):
        super(WorkDayScreen, self).__init__(**kwargs)
        self.refresh()

    # Atualiza informacoes na tela. Quais tasks o usuario devera realizar no dia
    # com base na carga horaria diaria definia pelo usuario

    def refresh(self):
        list = ctr.hoursPerTask()

        x = len(list)
        if x < 4:
            for z in range(0, 4-x):
                tup = ('', '')
                list.append(tup)

        self.task1 = str(list[0][1])
        self.task2 = str(list[1][1])
        self.task3 = str(list[2][1])
        self.task4 = str(list[3][1])
        self.hours1 = str(list[0][0])
        self.hours2 = str(list[1][0])
        self.hours3 = str(list[2][0])
        self.hours4 = str(list[3][0])

class TaskInfoScreen(Screen):
    # Exibe informacoes de uma Task
    description = StringProperty()
    descriptionShow = StringProperty()
    workload = StringProperty()
    deadline = StringProperty()
    priority = StringProperty()
    creation = StringProperty()
    done = StringProperty()

    # Executado sempre quando a Screen eh iniciada
    def __init__(self, **kwargs):
        super(TaskInfoScreen, self).__init__(**kwargs)
        self.setLabel()

    def setLabel(self):
        ID = int(idTask)
        for x in ctr.taskList:
            if x.get_idTask() == ID:
                self.description = x.get_description()
                self.descriptionShow = self.description[:20]+'...' # A string eh truncada, para poder aparecer na tela
                self.workload = str(x.get_workload())
                # O deadline padrao possui informacoes de horas, minutos, segundo e microsegundos, por isso truncamos para mostrar somente a data
                self.deadline = str(x.get_deadline())[:10]
                self.priority = str(x.get_priority())
                # O mesmo caso que o deadline
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

    # Executado sempre quando a Screen eh iniciada
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
        # Coletando informacoes inseridas pelo usuario
        self.description = self.ids['id_description'].text
        self.workload = self.ids['id_workload'].text
        self.deadline = self.ids['id_deadline'].text
        self.priority = self.ids['id_priority'].text
        self.done = self.ids['id_done'].text

        if self.description and self.workload and self.deadline and self.priority and self.done:
            # Eh esperado que o usuario preencha o campo dedline no padrao YYYY-MM-DD,
            # com isso adicionamos os valores para hora, minuto, segundo e microsegundo para poder usar a variavel datetime
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

    # Executado sempre quando a Screen eh iniciada
    def __init__(self, **kwargs):
        super(NewTaskScreen, self).__init__(**kwargs)
        self.clear()

    def clear(self):
        self.description = ''
        self.workload = ''
        self.deadline = ''
        self.priority = ''

    def ok_button(self):
        # Coletando informacoes inseridas pelo usuario
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

    # Executado sempre quando a Screen eh iniciada
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

    # Executado sempre quando a Screen eh iniciada
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

# Associacao de screens ao ScreenManagement
sm.add_widget(InitialScreen(name='initial'))
sm.add_widget(EditTaskScreen(name='edittask'))
sm.add_widget(NewTaskScreen(name='newtask'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(WorkDayScreen(name='workday'))
sm.add_widget(AboutScreen(name='about'))
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

    # Metodo para listar as tasks do usuário
    def view_tasks(self, root):
        if root.ids["task_panel"].children:
            root.ids["task_panel"].clear_widgets()
        task_view = TaskViewer()
        root.ids['task_panel'].add_widget(task_view)

        buttonList = []

        tasks = sorted(ctr.taskList, key=lambda y: y.get_weight(), reverse=True)

        # Eh criado uma lista de botões e associasse uma tela pra cada um deles
        for x in tasks:
            name = x.get_description()
            if len(x.get_description()) > 35:
                name = x.get_description()[:35] + '...'
            nameInfo = name + ' Urgency: ' + str(int(x.get_weight()))
            buttonList.append(Button(id=str(x.get_idTask()), text=nameInfo, size=(600, 60), size_hint=(None, None)))
            task_view.add_widget(buttonList[len(buttonList) - 1])
            change_screen = partial(self.change_screen, x.get_idTask())
            buttonList[len(buttonList) - 1].bind(on_press=change_screen)

if __name__ == '__main__':
    PanlexApp().run()