from PIL import Image as PILImage
from PIL import ImageDraw

class Pen():
    def __init__(self, size=(30, 30), color=(255, 255, 255, 255), mode="replace"):
        self._size = size
        self._color = color
        self.mode = mode
        self._update_pen()

    def _update_pen(self):
        width, height = self.size
        
        self.bitmap = PILImage.new("RGBA", self.size)
        draw_bitmap = ImageDraw.Draw(self.bitmap)
        draw_bitmap.ellipse([0, 0, width - 1, height - 1], fill=self.color)

        self.pen_mask = PILImage.new("RGBA", self.size)
        draw_pen_mask = ImageDraw.Draw(self.pen_mask)
        draw_pen_mask.ellipse([0, 0, width - 1, height - 1], fill=(255, 255, 255, 255))

        self.eraser_bitmap = PILImage.new("RGBA", self.size)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._update_pen()

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
        self._update_pen()
