import FreeCADGui as Gui
from pivy import coin

class GridOverlay:
    def __init__(self):
        self.root = coin.SoSeparator()
        self.visible = False
        self.build()

    def line(self, p1, p2, color):
        sep = coin.SoSeparator()

        c = coin.SoBaseColor()
        c.rgb = color

        coords = coin.SoCoordinate3()
        coords.point.setValues(0, 2, [p1, p2])

        line = coin.SoLineSet()
        line.numVertices.setValues(0, 1, [2])

        sep.addChild(c)
        sep.addChild(coords)
        sep.addChild(line)

        return sep

    def build(self):
        self.root.removeAllChildren()

        w = 200
        h = 200

        minor = (0.41, 0.40, 0.45)   # #696773
        major = (0.93, 0.94, 0.95)   # #EFF1F3
        xcol  = (1, 0, 0)
        ycol  = (0, 1, 0)

        for x in range(-100, 101):
            if x == 0:
                color = ycol
            elif x % 10 == 0:
                color = major
            else:
                color = minor

            self.root.addChild(self.line((x, -100, 0), (x, 100, 0), color))

        for y in range(-100, 101):
            if y == 0:
                color = xcol
            elif y % 10 == 0:
                color = major
            else:
                color = minor

            self.root.addChild(self.line((-100, y, 0), (100, y, 0), color))

    def show(self):
        if not self.visible:
            Gui.ActiveDocument.ActiveView.getSceneGraph().addChild(self.root)
            self.visible = True

    def hide(self):
        if self.visible:
            Gui.ActiveDocument.ActiveView.getSceneGraph().removeChild(self.root)
            self.visible = False

grid_overlay = GridOverlay()