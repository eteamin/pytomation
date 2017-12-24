from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from remote.networking.client import TCPRemoteClient


class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()
        with TCPRemoteClient():


