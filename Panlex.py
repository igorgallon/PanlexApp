from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition

# Declare both screens
class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class TaskScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class NewTaskScreen(Screen):
    pass

class EditTaskScreen(Screen):
    pass

class DeleteTaskScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("screen.kv")

class PanlexApp(App):
    def build(self):
        return presentation

PanlexApp().run()