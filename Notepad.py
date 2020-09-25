from kivy.app import App
from kivy.uix.textinput import TextInput
import pyautogui

class NotePadApp(App):
	def build(self):
		t = TextInput(font_size=20)
		return t
if __name__ == '__main__':
	NotePadApp().run()