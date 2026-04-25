import FreeCAD as App
App.Console.PrintMessage("\n[YS-Grid] Init.py LOADED\n")
from .grid_overlay import grid

def on_startup():
    p = App.ParamGet("User parameter:BaseApp/Preferences/YSGrid")
    auto = p.GetBool("AutoShow", True)

    if auto:
        try:
            grid.show()
        except:
            pass

App.addStartCallback(on_startup)