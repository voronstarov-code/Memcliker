import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random

class MainApp(App):
    def build(self):
        self.coins = 0
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="0")
        btn = Button(text="Клик")
        btn.bind(on_press=self.click)
        self.layout.add_widget(btn)
        self.layout.add_widget(self.label)
        return self.layout
    
    def click(self, instance):
        self.coins += 1
        self.label.text = str(self.coins)

if __name__ == "__main__":
    MainApp().run()
