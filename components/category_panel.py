
from PyQt5 import QtCore, QtGui, QtWidgets

class CategoryPanel(QtWidgets.QFrame):
  def __init__(self, parent=None, name="", on_click = None):
    super().__init__()
    self.parent = parent
    self.name = name
    self.setupUi()
    self.on_click = on_click


  def setupUi(self):
    self.setFixedSize(400, 500)
    self.setObjectName("CategoryPanel")
    
    self.verticalLayout = QtWidgets.QVBoxLayout(self)

    self.image_label = QtWidgets.QLabel(self)
    

    self.label = QtWidgets.QLabel(self)
    self.label.setObjectName("category_panel_label")
    self.label.setFont(QtGui.QFont('Helvetica', 40, QtGui.QFont.Bold))
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setText(self.name.title())


    self_style = f"color:white; background: url('assets/{self.name}.jpg');  background-position: center; border-radius: 10px;"
    self.image_label.setStyleSheet(self_style)
   
    self.mousePressEvent = self.clicked

    
    self.verticalLayout.addWidget(self.image_label, 2)
    self.verticalLayout.addWidget(self.label)

  def clicked(self, event):
    self.on_click(self.name)
    