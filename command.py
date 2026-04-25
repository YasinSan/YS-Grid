import FreeCADGui as Gui
from .grid_overlay import grid

class ToggleGrid:
    def GetResources(self):
        return {
            "MenuText": "YS Grid Toggle",
            "ToolTip": "Toggle overlay grid",
            "Pixmap": ""
        }

    def IsActive(self):
        return True

    def Activated(self):
        if grid.visible:
            grid.hide()
        else:
            grid.show()

Gui.addCommand("YSGridToggle", ToggleGrid())