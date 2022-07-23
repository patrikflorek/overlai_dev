from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from PIL import Image as PILImage

from sketcher.pen import Pen

from sketcher.sketcher import Sketcher

pen = Pen(size=(40, 40), color=(255, 255, 0, 127), mode="pen")

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
        "pen": pen
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

        overlay = self.sketcher.overlays_container.children[0]
        # overlay._draw_dot(0, 0)
        # overlay._draw_dot(279, 0)
        # overlay._draw_dot(279, 559)
        # overlay._draw_dot(0, 559)
        # overlay._draw_dot(139, 279)


class SketcherDemoApp(App):
    def build(self):
        return SketcherDemoAppRoot()

    def reset_transformations(self):
        print("reset_transformations")

    def clear_overlays(self):
        print("clear_overlays")

    def open_overlays_popup(self):
        print("open_overlays_popup")

    def open_pen_popup(self):
        print("open_pen_popup")

    def open_pen_mode_dropdown(self):
        print("open_pen_mode_dropdown")


if __name__ == "__main__":
    SketcherDemoApp().run()


# from kivy.graphics.texture import Texture
# from kivy.app import App
# from kivy.properties import ObjectProperty
# from kivy.uix.screenmanager import Screen

# from PIL import Image as PILImage

# from sketcher.sketcher import Sketcher

# from sketcher.pen import Pen

# SKETCHER_DATA = [
#     {
#         "id": "corals",
#         "active": True,
#         "opacity": 1.0,
#         "bitmap": PILImage.open("demo/img/corals_320x640.png"),
#         # "pen_bitmap": pen.bitmap,
#         "pen_mode": "pen"
#     },
#     {
#         "id": "octopus",
#         "active": False,
#         "opacity": 1.0,
#         "bitmap": PILImage.open("demo/img/octopus_320x640.png"),
#         # "pen_bitmap": pen.bitmap,
#         "pen_mode": "pen"
#     },
#     {
#         "id": "icecream",
#         "active": False,
#         "opacity": 1.0,
#         "bitmap": PILImage.open("demo/img/icecream_320x640.png"),
#         # "pen_bitmap": pen.bitmap,
#         "pen_mode": "pen"
#     }
# ]

# class SketcherDemoAppRoot(Screen):
#     sketcher_container = ObjectProperty()
    
#     def __init__(self, **kwargs):
#         super(SketcherDemoAppRoot, self).__init__(**kwargs)
#         self.sketcher = Sketcher(
#             background_color = (1, 0, 1, 0.4),
#             size = (280, 560)
#         )
#         self.sketcher_container.add_widget(self.sketcher)
#         # self.sketcher.set_data(SKETCHER_DATA)


# class SketcherDemoApp(App):
#     def build(self):
#         return SketcherDemoAppRoot()

#     def reset_transformations(self):
#         print("reset_transformations")
#         t = Texture.create(size=(100, 100))
#         print("done")
        
#     def clear_overlays(self):
#         print("clear_overlays")

#     def open_overlays_popup(self):
#         print("open_overlays_popup")

#     def open_pen_popup(self):
#         print("open_pen_popup")

#     def open_pen_mode_dropdown(self):
#         print("open_pen_mode_dropdown")


# if __name__ == "__main__":
#     SketcherDemoApp().run()
