

# main app class run on a kivy  fronternd



import kivy
from kivy.app import App

from kivy.lang import Builder

from screensandstuff import *


kvfile = Builder.load_file("backend.kv")


class TrajectoryApp(App):
    
    def build(self):
        return kvfile


if '__main__' == __name__:
    TrajectoryApp().run()
