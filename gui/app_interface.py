from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.lang import Builder
from kivy import *
from kivy.uix.scrollview import ScrollView
from game_entities.cluster import Cluster
from file_loader import load_cluster_data


class AppInterface(App):
    pass


class MainScreen(BoxLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)

    pass


# a subclass of button tha
class ClusterButton(Button):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        self.embedded_cluster = Cluster(
            kwargs.get("bloon_id", 0))  # i have this just so i know what is happening --- also VAIRABLE NAEMS
        print(self.embedded_cluster.name)

    pass


# ahh
class GroupedGrid(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.height = self.width
        button_grid = GridLayout(cols=kwargs.get("cols", 2))

        bloon_data = load_cluster_data()

        for bloon in bloon_data:
            button_grid.add_widget(ClusterButton(text=str(bloon[1])))

        self.add_widget(button_grid)


class AttributeToggle(ToggleButton):
    def update_text(self):
        if self.text.split()[0] == "Not":
            self.text = "Camo"
        # Update the text of the button when it is pressed
        else:
            self.text = "Not Camo"
