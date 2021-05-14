
import threading, sys

from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.lang import Builder

from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager , WipeTransition , FadeTransition  , SlideTransition
from kivy.uix.textinput import TextInput

from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty  , StringProperty , ListProperty , NumericProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from  graphbook import GraphBook
Window.size = 400,400


helpinfo = """
   
    This app was designed for game developers  to  get
     a list of a desired imagined trajectory .
     
     All you have to do is draw it and it will be saved to
     the default Desktop/trajectory  folderin a text file
     You can also save a file with a name of your liking.
     After that your job will now be to read the data

     Get the source code at-
     
https://github.com/victhepythonista/Trajectory Calculator

     email me any new features and bugs at-
     
letingvictoripkemboi@gmail.com  
            """
class MainScreen(Screen):
    graph_book_open = ObjectProperty()
    def quitapp(self, app):
        app.stop()
        sys.exit()
    def open_graphbook(self,app):
        GraphBook().run()
        app.stop()

class HelpScreen(Screen):
    info = ObjectProperty()
    def on_kv_post(self, instance):
        self.info.text = helpinfo        
    pass
    

class Manager(ScreenManager):
    pass
