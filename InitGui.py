import FreeCADGui as Gui
from .command import ToggleGrid, ShowPrefs

class YSGridWorkbench(Gui.Workbench):
    MenuText = "YS-Grid"
    ToolTip = "Global overlay grid"

    def Initialize(self):
        Gui.addCommand("YSGridToggle", ToggleGrid())
        Gui.addCommand("YSGridPrefs", ShowPrefs())

        self.appendToolbar("YS-Grid", ["YSGridToggle", "YSGridPrefs"])

Gui.addWorkbench(YSGridWorkbench())
