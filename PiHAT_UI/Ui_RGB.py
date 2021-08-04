from  PyQt5 import QtCore,QtGui,QtWidgets
from pihatui import Ui_form
from RGB import RGB_set
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

class pihatui(QtWidgets.QMainWindow,Ui_form):
    def __init__(self):
        super(pihatui,self).__init__()
        self.ui = Ui_form()
        self.rgb = RGB_set()
        self.ui.setupUi(self)
        self.ui.button_RED.toggled.connect(self.button_RED)
        self.ui.button_GREEN.toggled.connect(self.button_GREEN)
        self.ui.button_BLUE.toggled.connect(self.button_BLUE)

    def button_RED(self,value):
            if(value == True):
                print("RED is Selected")
                self.rgb.RED_toggle(1)
            else:
                print("RED is De_Seleced")
                self.rgb.RED_toggle(0)

    def button_GREEN(self,value):
            if(value == True):
                print("GREEN is Selected")
                self.rgb.GREEN_toggle(1)
            else:
                print("GREEN is De_Seleced")
                self.rgb.GREEN_toggle(0)

    def button_BLUE(self,value):
            if(value == True):
                print("BLUE is Selected")
                self.rgb.BLUE_toggle(1)
            else:
                print("BLUE is De_Seleced")
                self.rgb.BLUE_toggle(0)

app = QtWidgets.QApplication([])
window = pihatui()
window.show()
app.exec()