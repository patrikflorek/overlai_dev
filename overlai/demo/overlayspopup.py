from operator import imod
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


Builder.load_file("overlayspopup.kv")


class OverlaysPopup(Popup):
    items_container = ObjectProperty()

    def __init__(self, overlays, **kwargs):
        super(OverlaysPopup, self).__init__(**kwargs)
        print(overlays)