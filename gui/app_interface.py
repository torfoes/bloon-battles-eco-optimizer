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
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.effects.dampedscroll import DampedScrollEffect
from game_entities.cluster import Cluster
from file_loader import load_cluster_data
from kivy.effects.scroll import ScrollEffect
from kivy.properties import ObjectProperty
from simulator import Simulator
from kivy import Config

# Config.set('graphics', 'resizable', True)


class AppInterface(App):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_sim = Simulator()
    pass


class MainScreen(BoxLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)

    pass


# a subclass of button tha
class ClusterButton(Button, Cluster):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        self.embedded_cluster = Cluster(
            kwargs.get("bloon_id", 1))  # i have this just so i know what is happening --- also VAIRABLE NAEMS

    pass


# ahh
class GroupedGrid(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.height = self.width
        button_grid = GridLayout(cols=kwargs.get("cols", 2))

        self.bloon_data = load_cluster_data()

        for i, bloon in enumerate(self.bloon_data):
            button_grid.add_widget(ClusterButton(bloon_id=i, background_normal=bloon[11]))

        self.add_widget(button_grid)


class AttributeToggle(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_text(self):
        split_string = self.text.split()

        if split_string[0] == "Not":
            self.text = split_string[1]

        # Update the text of the button when it is pressed
        else:
            self.text = "Not " + split_string[0]


class StandardScroll(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.effect_cls =
    pass