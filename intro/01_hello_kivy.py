from kivy.app import App
from kivy.uix.label import Label

#Every Kivy application needs to subclass App
#and override build()
class MainApp(App):
	def build(self):
		label = Label(text="Hello from Kivy",
			size_hint=(.5, .5), #width, height
			pos_hint={'center_x': .5, 'center_y': .5})

		return label

if __name__ == '__main__':
	app=MainApp()
	app.run() #to make the application run