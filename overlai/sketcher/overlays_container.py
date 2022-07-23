from kivy.uix.relativelayout import RelativeLayout


class OverlaysContainer(RelativeLayout):
    def __init__(self, **kwargs):
        super(OverlaysContainer, self).__init__(**kwargs)

        self._touches = []
        self._stroke_touch = None

    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            return False

        # Track all touches.
        self._touches.append(touch)
        touch.grab(self)

        if 'multitouch_sim' in touch.profile:
            return False  # ignore multitouch simulation

        if len(self._touches) > 1:
            self._stroke_touch = None  # Only one stroke touch allowed
            return  False

        # Create a stroke.
        self._stroke_touch = touch
        touch.ud['stroke'] = [touch.pos]

        super(OverlaysContainer, self).on_touch_down(touch)

        return False

    def on_touch_move(self, touch):
        if touch != self._stroke_touch:
            return False

        touch.ud['stroke'].append(touch.pos)  # Touch position to be used by overlays.

        prev_x = touch.ud['stroke'][-2][0]
        prev_y = touch.ud['stroke'][-2][1]
        if not (self.collide_point(touch.x, touch.y) or self.collide_point(prev_x, prev_y)):
            return False

        super(OverlaysContainer, self).on_touch_move(touch)

        return True

    def on_touch_up(self, touch):
        # Stop tracking the touch.
        if touch.grab_current == self:
            touch.ungrab(self)

        if touch in self._touches:
            self._touches.remove(touch)

        if touch != self._stroke_touch:
            return False

        touch.ud['stroke'].append(touch.pos)

        self._stroke_touch = None

        if self.collide_point(touch.x, touch.y):
            super(OverlaysContainer, self).on_touch_up(touch)

        return False
