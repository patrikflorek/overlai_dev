from kivy.uix.scatter import Scatter

from kivy.properties import BoundedNumericProperty, ObjectProperty
from kivy.lang.builder import Builder

from sketcher.overlay import Overlay


Builder.load_string("""
#:import OverlaysContainer sketcher.overlays_container.OverlaysContainer

<Sketcher>:
    overlays_container: overlays_container
    background_color: 0, 0, 0, 0
    size_hint: None, None
    OverlaysContainer:
        id: overlays_container
        size: root.size
        canvas:
            Color:
                rgba: root.background_color
            Rectangle:
                pos: self.pos
                size: self.size
""")


class Sketcher(Scatter):
    translation_touches = BoundedNumericProperty(2, min=2)  # min 2 fingers for translations
 
    overlays_container = ObjectProperty()

    def __init__(self, background_color=(0, 0, 0, 0), **kwargs):
        super(Sketcher, self).__init__(**kwargs)
        self.background_color = background_color
        self._overlays_order = []
        self._overlays_dict = {}

    def get_data(self):
        data = []
        for overlay_id in self._overlays_order:
            overlay = self._overlays_dict[overlay_id]
            overlay_data = overlay.get_data()
            data.append(overlay_data) 

        return data

    def set_data(self, data):
        self.overlays_container.clear_widgets()
        self._overlays_order = []
        self._overlays_dict = {}

        for overlay_data in data:
            overlay_id = overlay_data['id']
            self._overlays_order.append(overlay_id)
            
            overlay = Overlay(overlay_data, size=self.size)
            self._overlays_dict[overlay_id] = overlay
            self.overlays_container.add_widget(overlay)

    def add_overlay(self, data, index):
        overlay_id = data["id"]
        self._overlays_order.insert(overlay_id, index)
        overlay = Overlay(data, size=self.size)
        self._overlays_dict[overlay_id] = overlay
        container_index = len(self._overlays_order) - 1 - index
        self.overlays_container.add_widget(overlay, container_index)

    def remove_overlay(self, overlay_id):
        overlay = self._overlays_dict[overlay_id]
        self.overlays_container.remove_widget(overlay)
        self._overlays_order.remove(overlay_id)
        del self._overlays_dict[overlay_id]

    def get_overlays_order(self):
        return self._overlays_order[:]

    def set_overlays_order(self, overlay_ids):
        omitted_overlay_ids = set(self._overlays_dict.keys()) - set(overlay_ids)
        for omitted_overlay_id in omitted_overlay_ids:
            del self._overlays_dict[omitted_overlay_id]

        self.overlays_container.clear_widgets()
        self._overlays_order = []
        
        for overlay_id in overlay_ids:
            if overlay_id not in self._overlays_dict.keys():
                continue

            self._overlays_order.append(overlay_id)
            overlay = self._overlays_dict[overlay_id]
            self.overlays_container.add_widget(overlay)
