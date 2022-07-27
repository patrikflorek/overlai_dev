from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.properties import ColorProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from sketcher.texture import bitmap_to_texture


Builder.load_file("penpopup.kv")


PALETTE_COLORS = [
    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), 
    (0, 1, 1), (0, 0, 1), (1, 0, 1), (1, 1, 1)
]


class PenColorSwatchBox(BoxLayout):
    swatch_button = ObjectProperty()

    def __init__(self, color=(0, 0, 0), **kwargs):
        super(PenColorSwatchBox, self).__init__(**kwargs)
        self.color = color


class PenColorPaletteBox(BoxLayout):
    selected_color = ColorProperty()

    swatches_container = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(PenColorPaletteBox, self).__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, dt):
        for color in PALETTE_COLORS:
            swatch = PenColorSwatchBox(color=color)
            swatch.swatch_button.bind(on_release=self._select_pen_color) 
            self.swatches_container.add_widget(swatch)

    def _select_pen_color(self, swatch_button):
        self.selected_color = swatch_button.color[:3]

    def on_selected_color(self, instance, color):
        for swatch in self.swatches_container.children:
            if swatch.color == color[:3]:
                swatch.padding = "0dp"
            else:
                swatch.padding = "5dp"


class PenPreviewBox(BoxLayout):
    pen_bitmap = ObjectProperty()

    preview_image = ObjectProperty()

    def on_pen_bitmap(self, instance, bitmap):
        self.preview_image.size = bitmap.size 
        self.preview_image.texture = bitmap_to_texture(bitmap)


class PenPopup(Popup):
    size_slider = ObjectProperty()
    colors_palette = ObjectProperty()
    alpha_slider = ObjectProperty()
    preview = ObjectProperty()

    def __init__(self, pen, **kwargs):
        super(PenPopup, self).__init__(**kwargs)
        self.pen = pen
        self.size_slider.pen_size_slider.bind(value=self.update_pen_size)
        self.colors_palette.bind(selected_color=self.update_pen_color)
        self.alpha_slider.pen_alpha_slider.bind(value=self.update_pen_alpha)
    
    def update_pen_size(self, instance, size):
        self.pen.size = (size, size)
        self.preview.pen_bitmap = self.pen.bitmap

    def update_pen_color(self, instance, color):
        self.pen.color = tuple([int(x * 255) for x in color[:3]] + [self.pen.color[3]])
        self.preview.pen_bitmap = self.pen.bitmap

    def update_pen_alpha(self, instance, alpha):
        self.pen.color = self.pen.color[:3] + (int(alpha * 255),)
        self.preview.pen_bitmap = self.pen.bitmap

    def on_open(self):
        self.size_slider.pen_size = self.pen.size[0]
        self.colors_palette.selected_color = [x / 255 for x in self.pen.color[:3]]
        self.alpha_slider.pen_alpha = self.pen.color[3] / 255
        self.preview.pen_bitmap = self.pen.bitmap
