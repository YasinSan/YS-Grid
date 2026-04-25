import FreeCADGui as Gui
from .command import ToggleGrid, ShowPrefs

class YSGridWorkbench(Gui.Workbench):
    MenuText = "YS-Grid"
    ToolTip = "Global CAD-style overlay grid"
    Icon = ""

    def Initialize(self):
        Gui.addCommand("YSGridToggle", ToggleGrid())
        Gui.addCommand("YSGridPrefs", ShowPrefs())

        self.appendToolbar("YS-Grid", ["YSGridToggle", "YSGridPrefs"])

    def Activated(self):
        pass

    def Deactivated(self):
        pass

Gui.addWorkbench(YSGridWorkbench())