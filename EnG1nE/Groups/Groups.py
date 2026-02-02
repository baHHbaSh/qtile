import random
from libqtile import widget
# You might need to import the base widget class differently depending on your qtile version
# from libqtile.widgets import GroupBox 

class RandomColorGroupBox(widget.GroupBox):
    def get_random_color(self):
        return "#%06x" % random.randint(0, 0xFFFFFF)

    def draw(self):
        self.group_colors = {}
        for group in self.qtile.groups:
            self.group_colors[group.name] = self.get_random_color()
        super().draw()