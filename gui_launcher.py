from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal")
        layout.add_widget(Label(text="Hello, World!"))
        layout.add_widget(Label(text="Hello, World!"))
        layout.add_widget(Button(text="Click me!", on_press=self.button_clicked))
        return layout

    def button_clicked(self, instance):
        instance.text = "You clicked me!"