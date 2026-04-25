import FreeCAD as App
App.Console.PrintMessage("\n[YS-Grid] InitGui.py LOADED\n")
from .command import ToggleGrid

class YSGridWorkbench(Gui.Workbench):
    MenuText = "YS-Grid"
    ToolTip = "Overlay grid system"

    def Initialize(self):
        Gui.addCommand("YSGridToggle", ToggleGrid())

        self.appendToolbar("YS-Grid", ["YSGridToggle"])

    def Activated(self):
        pass

Gui.addWorkbench(YSGridWorkbench())