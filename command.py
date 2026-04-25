import FreeCADGui as Gui
import FreeCAD as App
from .grid_overlay import grid_overlay
from .preferences import PrefDialog

class ToggleGrid:
    def GetResources(self):
        return {
            "MenuText": "Toggle YS-Grid",
            "ToolTip": "Show/Hide overlay grid",
            "Pixmap": ""
        }

    def Activated(self):
        p = App.ParamGet("User parameter:BaseApp/Preferences/YSGrid")
        visible = p.GetBool("Visible", True)

        if visible:
            grid_overlay.hide()
            p.SetBool("Visible", False)
        else:
            grid_overlay.show()
            p.SetBool("Visible", True)

class ShowPrefs:
    def GetResources(self):
        return {"MenuText": "YS-Grid Settings"}

    def Activated(self):
        dlg = PrefDialog()
        dlg.exec_()

Gui.addCommand("YSGridToggle", ToggleGrid())
Gui.addCommand("YSGridPrefs", ShowPrefs())