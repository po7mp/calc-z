from PyQt5.QtWidgets import*
app = QApplication([])
okno = QWidget()
textchisla=""
line1 = QVBoxLayout()
okno.setLayout(line1)
line2 = QHBoxLayout()
line1.addLayout(line2)
text1 = QLabel("+")
line1.addWidget(text1)
vvod1= QLineEdit()
line1.addWidget(vvod1)
chislo1 = vvod1.text()
vvod2= QLineEdit()
line2.addWidget(vvod2)
chislo2 = vvod2.text()
text2 = QLabel("=")
line1.addWidget(text2)
text3 = QPushButton('Найти')
line1.addWidget(text3)
line2 = QHBoxLayout()
line1.addLayout(line2)
text4 = QLabel("-")
line1.addWidget(text4)
vvod5= QLineEdit()
line1.addWidget(vvod5)
chislo4 = vvod5.text()
vvod4= QLineEdit()
line2.addWidget(vvod4)
chislo5 = vvod4.text()
text5 = QPushButton('Найти')
line1.addWidget(text5)
text6 = QLabel("=")
line1.addWidget(text6)
line2 = QHBoxLayout()
line1.addLayout(line2)
text9 = QLabel("x")
line1.addWidget(text9)
vvod6= QLineEdit()
line1.addWidget(vvod6)
chislo6 = vvod6.text()
vvod7= QLineEdit()
line2.addWidget(vvod7)
chislo7 = vvod7.text()
text7 = QPushButton('Найти')
line1.addWidget(text7)
text8 = QLabel("=")
line1.addWidget(text8)

line2 = QHBoxLayout()
line1.addLayout(line2)
text10 = QLabel(":")
line1.addWidget(text10)
vvod10= QLineEdit()
line1.addWidget(vvod10)
chislo9 = vvod10.text()
vvod11= QLineEdit()
line2.addWidget(vvod11)
chislo12 = vvod11.text()
text11 = QPushButton('Найти')
line1.addWidget(text11)
text12 = QLabel("=")
line1.addWidget(text12)


def plus():
    a = int(vvod1.text())
    b = int(vvod2.text())
    text2.setText(str(a+b))

text3.clicked.connect(plus)


def minus():
    a = int(vvod4.text())
    b = int(vvod5.text())
    text6.setText(str(a-b))

text5.clicked.connect(minus)


def umnog():
    a = int(vvod6.text())
    b = int(vvod7.text())
    text8.setText(str(a*b))

text7.clicked.connect(umnog)

def delen():
    a = int(vvod11.text())
    b = int(vvod10.text())
    text12.setText(str(a/b))

text11.clicked.connect(delen)

text1.setStyleSheet('''
QLabel{color:red; 
font-size: 25px;
}
''')


text2.setStyleSheet('''
QLabel{color:red;
font-size: 25px;
} 
''')

text6.setStyleSheet('''
QLabel{color:red;
font-size: 25px;
} 
''')

text8.setStyleSheet('''
QLabel{color:red;
font-size: 25px;
} 
''')

text12.setStyleSheet('''
QLabel{color:red;
font-size: 25px;
} 
''')


text3.setStyleSheet('''
QPushButton{color:red;
font-size: 25px;
background:white;
} 
''')

text4.setStyleSheet('''
QLabel{color:red;
font-size: 30px;
} 
''')

text9.setStyleSheet('''
QLabel{color:red;
font-size: 30px;
} 
''')

text10.setStyleSheet('''
QLabel{color:red;
font-size: 30px;
} 
''')

text5.setStyleSheet('''
QPushButton{color:red;
font-size: 25px;
background:white;
} 
''')

text7.setStyleSheet('''
QPushButton{color:red;
font-size: 25px;
background:white;
} 
''')

text11.setStyleSheet('''
QPushButton{color:red;
font-size: 25px;
background:white;
} 
''')

okno.setStyleSheet('''
QWidget{
background:qlineargradient(
x0: 0,y0:0,x1: 2,y1:3
stop: 1 white, stop: 0 black    
);   
}
''')



okno.show()
app.exec_()
