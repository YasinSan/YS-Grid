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

        size = 200
        step = 1
        major = 10

        minor = (0.41, 0.40, 0.45)
        major_c = (0.93, 0.94, 0.95)
        x_axis = (1, 0, 0)
        y_axis = (0, 1, 0)

        x = -size // 2
        while x <= size // 2:

            if x == 0:
                color = y_axis
            elif x % major == 0:
                color = major_c
            else:
                color = minor

            self.root.addChild(self.line((x, -size/2, 0), (x, size/2, 0), color))
            x += step

        y = -size // 2
        while y <= size // 2:

            if y == 0:
                color = x_axis
            elif y % major == 0:
                color = major_c
            else:
                color = minor

            self.root.addChild(self.line((-size/2, y, 0), (size/2, y, 0), color))
            y += step

    def show(self):
        if not self.visible:
            Gui.ActiveDocument.ActiveView.getSceneGraph().addChild(self.root)
            self.visible = True

    def hide(self):
        if self.visible:
            Gui.ActiveDocument.ActiveView.getSceneGraph().removeChild(self.root)
            self.visible = False


grid = GridOverlay()