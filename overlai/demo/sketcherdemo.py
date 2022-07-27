from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from PIL import Image as PILImage

from demo.penmodedropdown import PenModeDropDown
from demo.overlayspopup import OverlaysPopup
from demo.penpopup import PenPopup

from sketcher.pen import Pen
from sketcher.sketcher import Sketcher


pen = Pen(size=(40, 40), color=(255, 255, 0, 127), mode="replace")


SKETCHER_DATA = [
    {
        "id": "corals",
        "bitmap": PILImage.open("demo/img/corals_320x640.png"),
        "pen": pen,
        "active": False
    },
    {
        "id": "octopus",
        "bitmap": PILImage.open("demo/img/octopus_320x640.png"),
        "pen": pen,
        "active": False
    },
    {
        "id": "icecream",
        "bitmap": PILImage.open("demo/img/icecream_320x640.png"),
        "pen": pen,
        "active": True
    }
]


class SketcherDemoAppRoot(Screen):
    sketcher_container = ObjectProperty()

    def __init__(self, **kwargs):
        super(SketcherDemoAppRoot, self).__init__(**kwargs)
        self.sketcher = Sketcher(
            background_color=(1, 0, 1, 1),
            size=(280, 560)
        )
        self.sketcher_container.add_widget(self.sketcher)
        self.sketcher.set_data(SKETCHER_DATA)


class SketcherDemoApp(App):
    def __init__(self, **kwargs):
        super(SketcherDemoApp, self).__init__(**kwargs)

    def build(self):
        root = SketcherDemoAppRoot()
        self.sketcher = root.sketcher
        self.sketcher_container = root.sketcher_container
        return root

    def on_start(self):
        print("on_start")
        self.pen_popup = PenPopup(pen)
        self.overlays_popup = OverlaysPopup(self.sketcher.overlays_container.children)

    def reset_transformations(self):
        self.sketcher.apply_transform(self.sketcher.transform_inv)
        self.sketcher.center = self.sketcher_container.center

    def open_overlays_popup(self):
        print("open_overlays_popup")
        self.overlays_popup.open()

    def open_pen_popup(self):
        self.pen_popup.open() 

    def _set_pen_mode(self, instance, mode):
        self.root.pen_mode_dropdown_main_button.text = mode.upper()
        pen.mode = mode

    def open_pen_mode_dropdown(self, instance):
        dropdown = PenModeDropDown()
        dropdown.container.padding = [0, "10dp"]
        dropdown.bind(on_select=self._set_pen_mode)
        dropdown.open(instance)


if __name__ == "__main__":
    SketcherDemoApp().run()
