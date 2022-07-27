import PIL

from kivy.graphics.texture import Texture


def bitmap_to_texture(bitmap):
    texture = Texture.create(bitmap.size, colorfmt="rgba")
    flipped_bitmap = bitmap.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    texture.blit_buffer(flipped_bitmap.tobytes(), colorfmt="rgba")
    return texture