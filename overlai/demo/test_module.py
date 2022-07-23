from kivy.app import App
from kivy.uix.image import Image

from kivy.graphics.texture import Texture

from PIL import Image as PILImage

import os
print(os.getcwd())

import PIL


class TestAppRoot(Image):
    def __init__(self, **kwargs):
        super(TestAppRoot, self).__init__(**kwargs)
        bitmap = PILImage.open("overlai/demo/img/corals_320x640.png")
        flipped_bitmap = bitmap.transpose(PIL.Image.Transpose.FLIP_TOP_BOTTOM)
        print(bitmap.size)
        t = Texture.create(size=bitmap.size, colorfmt="rgba")
        t.blit_buffer(flipped_bitmap.tobytes(), colorfmt="rgba")
        self.texture = t


class TestApp(App):
    def build(self):
        return TestAppRoot()


if __name__ == "__main__":
    TestApp().run()