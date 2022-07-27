from operator import imod
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


Builder.load_file("overlayspopup.kv")


class OverlayItem(BoxLayout):
    def __init__(self, overlay, **kwargs):
        self.overlay = overlay
        self.overlay_id = overlay.id
        self.overlay_active = overlay.active
        self.overlay_visible = int(overlay.opacity > 0)


class OverlaysPopup(Popup):
    items_container = ObjectProperty()

    def __init__(self, sketcher, **kwargs):
        super(OverlaysPopup, self).__init__(**kwargs)
        self.sketcher = sketcher
       
        for overlay in sketcher.:
            item = OverlayItem(overlay)
        