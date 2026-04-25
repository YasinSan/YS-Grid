import FreeCADGui as Gui
from .command import ToggleGrid

class ToggleGridCommand:
    def GetResources(self):
        return {
            "MenuText": "YS Grid Toggle",
            "ToolTip": "Toggle overlay grid"
        }

    def IsActive(self):
        return True

    def Activated(self):
        ToggleGrid().Activated()

Gui.addCommand("YSGridToggle", ToggleGridCommand())