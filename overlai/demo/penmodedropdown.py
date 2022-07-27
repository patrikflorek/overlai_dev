from kivy.lang.builder import Builder
from kivy.uix.dropdown import DropDown

Builder.load_string("""
<PenModeDropDown>:
    Button:
        text: 'Replace'
        size_hint_y: None
        height: '40dp'
        on_release: root.select('replace')
    Button:
        text: 'Erase'
        size_hint_y: None
        height: '40dp'
        on_release: root.select('erase')
""")


class PenModeDropDown(DropDown):
    pass