from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from googletrans import Translator

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.t1 = Translator()
        self.ui.comboBox.addItems(['en','fr','ru','de','ua'])
        self.ui.pushButton.clicked.connect(self.translate_text)
    def translate_text(self):
        text = self.ui.lineEdit.text()
        lang = self.ui.comboBox.currentText()
        if text:
            translated = self.t1.translate(text,dest=lang)
            self.ui.textEdit.setPlainText(translated.text)
    


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()