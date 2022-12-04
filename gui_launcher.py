from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar


# class StatusIndicator(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.label = Label(text="Loading...")
#         self.progress_bar = ProgressBar()
#         self.add_widget(self.label)
#         self.add_widget(self.progress_bar)


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal")


        layout.add_widget(Button(text="Button 1"))
        layout.add_widget(Label(text="Hello, World!"))
        layout.add_widget(Button(text="Click me!", on_press=self.button_clicked))

        # layout.add_widget(StatusIndicator())

        return layout


    def button_clicked(self, instance):
        instance.text = "You clicked me!"