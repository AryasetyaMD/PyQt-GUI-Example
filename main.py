########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
########################################################################
# IMPORT GUI FILE
from ui_gui_example import *
########################################################################

from Custom_Widgets.Widgets import *

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		########################################################################
		# APPLY JSON STYLESHEET
		########################################################################
		# self = QMainWindow class
		# self.ui = Ui_MainWindow / user interface class
		loadJsonStyle(self, self.ui)
		########################################################################

		#######################################################################
		# SHOW WINDOW
		#######################################################################
		self.show()
		########################################################################
		##
		########################################################################

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
	app = QApplication(sys.argv)
	########################################################################
	##
	########################################################################
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
########################################################################
## END===>
########################################################################
