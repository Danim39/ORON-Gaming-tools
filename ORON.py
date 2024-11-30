import sys
import random
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*

class Oron(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("ORON")
        self.setGeometry(0, 0, 570, 330)
        self.setWindowIcon(QIcon('ORON ICON.ico'))


        #labels
        self.label=QLabel(self)
        self.label.setGeometry(-200, -150, 771, 511)
        self.label.setPixmap(QPixmap('back.jpg'))

        self.label_text=QLabel('Chose the cuntry(iran, Emirates...)',self)
        self.label_text.setGeometry(200, 150, 300, 50)
        self.label_text.setFont(QFont("MV Boli", 13))
        self.label_text.hide()

        self.label_text2=QLabel('Develope by ',self)
        self.label_text2.setGeometry(10, 270, 300, 50)
        self.label_text2.setFont(QFont("Arial", 15))

        self.label_text3=QLabel('Danim',self)
        self.label_text3.setStyleSheet("color:rgb(128,0,128);")
        self.label_text3.setGeometry(130, 270, 300, 50)
        self.label_text3.setFont(QFont("Arial", 20))


        #Start buttons
        self.btn_start=QPushButton('Start',self)
        self.btn_start.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        self.btn_start.setGeometry(170, 220, 230, 50)
        self.btn_start.clicked.connect(self.hide_and_show_button)
        self.btn_start.setFont(QFont('Arial',30))
        
        self.btn_next=QPushButton('Next',self)
        self.btn_next.setGeometry(270, 250, 100, 20)
        self.btn_next.clicked.connect(self.next_btn)
        self.btn_next.hide()
        self.btn_next.setDisabled(True)  # Initially disable the button

        self.btn_generate=QPushButton('Gengenerate',self)
        self.btn_generate.setGeometry(270, 250, 100, 20)
        self.btn_generate.clicked.connect(self.next_btn2)
        self.btn_generate.clicked.connect(self.generate_button)
        self.btn_generate.hide()

        
        #Qline edites 
        self.Qcunline=QLineEdit(self)
        self.Qcunline.setGeometry(150, 190, 350, 41)
        self.Qcunline.setFont(QFont("MV Boli", 15))
        self.Qcunline.setStyleSheet('background-color: rgb(64, 64, 64);')
        self.Qcunline.hide()
        self.Qcunline.textChanged.connect(self.on_text_changed)
        
        self.Qcunline2=QLineEdit(self)
        self.Qcunline2.setGeometry(150, 240, 350, 41)
        self.Qcunline2.setFont(QFont("MV Boli", 15))
        self.Qcunline2.setStyleSheet('background-color: rgb(64, 64, 64);')
        self.Qcunline2.hide()


    # functions
    def hide_and_show_button(self):
        self.btn_start.hide()
        self.Qcunline.show()
        self.btn_next.show()
        self.label_text.show()
        self.label.setPixmap(QPixmap('back2.jpg'))
        self.label.setGeometry(-50, -150, 771, 511)
        self.setGeometry(0, 0,630, 350)
        self.label_text2.hide()
        self.label_text3.hide()


    def next_btn(self):
        
            self.Qcunline.setText('')
            self.label_text.setText("Enter your game?")
            self.label_text.setGeometry(190, 150, 300, 50)
            self.label_text.setFont(QFont("MV Boli", 17))
            self.btn_next.hide()
            self.btn_generate.show()
        
    def next_btn2(self):
        self.label_text.setText("Your ipv4 DNS👽")
        self.label_text.setGeometry(220, 150, 300, 50)
        self.label_text.setFont(QFont("MV Boli", 20))
        self.btn_generate.hide()
        self.Qcunline2.setText("10.202.10.10")
        self.Qcunline2.show()

    def generate_button(self):
         
              self.Qcunline.setText(self.generate_ipv4())
      
    def generate_ipv4(self):
    
            return ".".join(f"{random.randint (0, 255)}" for _ in range(4)) 
    
    def on_text_changed(self):
        list=['!','@','#','$','%','^','&','*','()','(',')','-','_','=','+',']','}','[]','[',']','/','?','<','>','"','',',','.']
        if self.Qcunline.text():
            self.btn_next.setDisabled(False)
            if self.Qcunline.text().isdigit() or self.Qcunline.text() in list:
                self.btn_next.setDisabled(True)
        else:
            self.btn_next.setDisabled(True)
        

app=QApplication(sys.argv)
oron=Oron()

oron.show()
sys.exit(app.exec())