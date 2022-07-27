from PIL import Image as PILImage

from kivy.uix.image import Image
from kivy.properties import ObjectProperty

from sketcher.texture import bitmap_to_texture

class Overlay(Image):
    bitmap = ObjectProperty()

    def __init__(self, data, size, **kwargs):
        super(Overlay, self).__init__(**kwargs)
        self.id = data['id']
        self.set_data(data, size)
        
    def get_data(self):
        data = {
            'id': self.id,
            'active': self.active,
            'opacity': self.opacity,
            'bitmap': self.bitmap,
            "pen": self.pen
        }
        return data

    def set_data(self, data, size):
        if self.id != data['id']:
            return False

        self.size = size

        if 'active' in data:
            self.active = data['active']
        elif not hasattr(self, 'active'):
            self.active = True

        if 'opacity' in data:
            self.opacity = data['opacity']
        elif not hasattr(self, 'opacity'):
            self.opacity = 1.0

        self.bitmap = data['bitmap'].resize(self.size).convert("RGBA")

        self.pen = data["pen"]

    def clear(self):
        self.bitmap = PILImage.new("RGBA", self.bitmap.size)

    def on_bitmap(self, instance, bitmap):
        self.texture = bitmap_to_texture(bitmap)

    def _draw_dot(self, x, y):
        pen_width, pen_height = self.pen.size
        pen_x = x - pen_width // 2
        pen_y = self.height - y - pen_height // 2 - 1
        if self.pen.mode == "replace":
            self.bitmap.paste(self.pen.bitmap, (pen_x, pen_y), self.pen.pen_mask)
        
        if self.pen.mode == "erase":
            self.bitmap.paste(self.pen.eraser_bitmap, (pen_x, pen_y), self.pen.pen_mask)
        
        self.texture = bitmap_to_texture(self.bitmap)

    def _draw_line(self, x, y, prev_x, prev_y):
        pen_width, pen_height = self.pen.size
        x_dist = abs(x - prev_x)
        y_dist = abs(y - prev_y)
        max_dist = max(x_dist, y_dist)
        dx = 0 if max_dist == 0 else (x - prev_x) / max_dist
        dy = 0 if max_dist == 0 else (y - prev_y) / max_dist
        for i in range(int(max_dist)):
            x_i = int(prev_x + i * dx)
            y_i = int(prev_y + i * dy)

            if not self.collide_point(x_i, y_i):
                continue

            pen_x_i = x_i - pen_width // 2
            pen_y_i = self.height - y_i - pen_height // 2 - 1
            
            if self.pen.mode == "replace":
                self.bitmap.paste(self.pen.bitmap, (pen_x_i, pen_y_i), self.pen.pen_mask)
        
            if self.pen.mode == "erase":
                self.bitmap.paste(self.pen.eraser_bitmap, (pen_x_i, pen_y_i), self.pen.pen_mask)
        
        self.texture = bitmap_to_texture(self.bitmap)

    def on_touch_move(self, touch):
        if not self.active:
            return False

        x = int(touch.x)
        y = int(touch.y)
        prev_x = int(touch.ud['stroke'][-2][0])
        prev_y = int(touch.ud['stroke'][-2][1])
        
        self._draw_line(x, y, prev_x, prev_y)

        return False  # Other overlays can process the touch event too
   
    def on_touch_up(self, touch):
        if not self.active:
            return False

        x = int(touch.x)
        y = int(touch.y)

        if len(touch.ud['stroke']) == 2:
            # There was no touch move between touch down and touch up events.
            self._draw_dot(x, y)

        return False  # Other overlays can process the touch event too
