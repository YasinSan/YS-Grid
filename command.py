import FreeCADGui as Gui
from .grid_overlay import grid

class ToggleGrid:
    def Activated(self):
        if grid.visible:
            grid.hide()
        else:
            grid.show()