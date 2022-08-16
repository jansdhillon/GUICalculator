from PyQt5.QtWidgets import *
import sys

#create instance of QApplication
app = QApplication(sys.argv)

#Create an instance of GUI
window = QWidget()
#title of app
window.setWindowTitle('PyQt5 App')
#1, 2 are position of gui on screnee, 3,4 are size of window
window.setGeometry(100, 100, 200, 80)
#moves window to coords
window.move(60, 15)
#Displays label, parent is window widget
helloMsg = QLabel('<h1>Hello World</h1>', parent=window)
#puts the label in the middle of the window
helloMsg.move(60, 15)

#shows the GUI
window.show()

#run event loop
sys.exit(app.exec_())