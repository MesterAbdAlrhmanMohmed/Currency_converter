from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from CurrencyConverter import convert
import dic
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("محول العملات")
        self.إظهار1=qt.QLabel("التحويل من")
        self.من=qt.QComboBox()
        self.من.setAccessibleName("التحويل من")
        self.من.addItems(dic.currencies.values())
        self.إظهار2=qt.QLabel("التحويل الى")
        self.الى=qt.QComboBox()
        self.الى.setAccessibleName("التحويل الى")
        self.الى.addItems(dic.currencies.values())
        self.إظهار3=qt.QLabel("إدخال القيمة")
        self.القيمة=qt.QLineEdit()
        self.القيمة.setAccessibleName("إدخال القيمة")
        self.إظهار4=qt.QLabel("النتيجة")
        self.النتيجة=qt.QLineEdit()
        self.النتيجة.setAccessibleName("النتيجة")
        self.التحويل=qt.QPushButton("تحويل")
        self.التحويل.setDefault(True)
        self.التحويل.clicked.connect(self.c)
        l=qt.QVBoxLayout()        
        l.addWidget(self.إظهار1)        
        l.addWidget(self.من)
        l.addWidget(self.إظهار2)
        l.addWidget(self.الى)
        l.addWidget(self.إظهار3)
        l.addWidget(self.القيمة)
        l.addWidget(self.التحويل)
        l.addWidget(self.إظهار4)
        l.addWidget(self.النتيجة)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def c(self):
        try:
            c1=next((key for key, value in dic.currencies.items() if value == self.من.currentText()), None)
            c2=next((key for key, value in dic.currencies.items() if value == self.الى.currentText()), None)
            result=convert(c1,c2,int   (self.القيمة.text()))
            self.النتيجة.setText(result)
            self.النتيجة.setFocus()
        except:
            qt.QMessageBox.warning(self,"تنبيه","عفوا حدث خطأ, يرجى التأكد من الإتصال بالإنترنت")
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()