import FreeCAD as App
from .grid_overlay import grid

def start():
    p = App.ParamGet("User parameter:BaseApp/Preferences/YSGrid")
    if p.GetBool("AutoShow", False):
        grid.show()

App.addStartCallback(start)