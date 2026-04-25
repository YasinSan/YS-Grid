import FreeCAD as App
from PySide import QtWidgets

class PrefDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YS-Grid Preferences")

        layout = QtWidgets.QFormLayout(self)

        self.auto = QtWidgets.QCheckBox()
        self.auto.setChecked(self.load_auto())

        layout.addRow("Auto show on startup", self.auto)

        btn = QtWidgets.QPushButton("Save")
        btn.clicked.connect(self.save)
        layout.addRow(btn)

    def load_auto(self):
        p = App.ParamGet("User parameter:BaseApp/Preferences/YSGrid")
        return p.GetBool("AutoShow", True)

    def save(self):
        p = App.ParamGet("User parameter:BaseApp/Preferences/YSGrid")
        p.SetBool("AutoShow", self.auto.isChecked())
        self.accept()