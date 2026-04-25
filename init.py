import FreeCAD as App
from .grid_overlay import grid_overlay

def on_startup():
    # Load saved state
    p = App.ParamGet("User parameter:BaseApp/Preferences/YSGrid")
    auto_show = p.GetBool("AutoShow", True)

    if auto_show:
        try:
            grid_overlay.show()
        except Exception as e:
            print("[YS-Grid] Startup error:", e)

# register startup hook
App.addStartCallback(on_startup)