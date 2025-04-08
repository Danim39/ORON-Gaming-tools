import sys
import random
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*
import random
import os
from wireguard import generate_key,generate_config


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
        self.btn_next.setDisabled(True)

        self.btn_next2=QPushButton("Next",self)
        self.btn_next2.setGeometry(270, 250, 100, 20)
        self.btn_next2.hide()
        self.btn_next2.clicked.connect(self.next_btn2)

        self.btn_save=QPushButton("Save",self)
        self.btn_save.setGeometry(270, 250, 100, 20)
        self.btn_save.hide()
        self.btn_save.clicked.connect(self.save_btn)

        self.btn_generate=QPushButton('Gengenerate',self)
        self.btn_generate.setGeometry(270, 250, 100, 20)
        self.btn_generate.clicked.connect(self.generate_dns)
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


        #check box
        self.chbox_ipv4 = QCheckBox('Ipv4',self)
        self.chbox_ipv4.setGeometry(150, 190, 350, 41)
        self.chbox_ipv4.hide()
        self.chbox_ipv4.clicked.connect(self.checkBox_ipv4)

        self.chbox_ipv6 = QCheckBox('Ipv6',self)
        self.chbox_ipv6.setGeometry(280, 190, 350, 41)
        self.chbox_ipv6.hide()
        self.chbox_ipv6.clicked.connect(self.checkBox_ipv6)

        self.chbox_wireguard = QCheckBox('Wireguard',self)
        self.chbox_wireguard.setGeometry(400, 190, 350, 41)
        self.chbox_wireguard.hide()
        self.chbox_wireguard.clicked.connect(self.main)
        

    # function
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
            self.btn_next2.show()

    def next_btn2(self):
        self.Qcunline.hide()
        self.label_text.setText("chose your dns version")
        self.chbox_ipv4.show()
        self.chbox_ipv6.show()
        self.chbox_wireguard.show()
        self.btn_next2.hide()
        self.btn_generate.show()
        
    def checkBox_ipv4(self):
        if self.chbox_ipv4.checkState() == Qt.CheckState.Checked:
             self.chbox_wireguard.setDisabled(True)
             self.chbox_ipv6.setDisabled(True)
        else:
             self.chbox_wireguard.setDisabled(False)
             self.chbox_ipv6.setDisabled(False)

    def checkBox_ipv6(self):
         if self.chbox_ipv6.checkState() == Qt.CheckState.Checked:
             self.chbox_wireguard.setDisabled(True)
             self.chbox_ipv4.setDisabled(True)

         else:
            self.chbox_wireguard.setDisabled(False)
            self.chbox_ipv4.setDisabled(False)

    def checkBox_wireguard(self):
         if self.chbox_wireguard.checkState() == Qt.CheckState.Checked:
             self.chbox_ipv6.setDisabled(True)
             self.chbox_ipv4.setDisabled(True)

         else:
             self.chbox_ipv6.setDisabled(False)
             self.chbox_ipv4.setDisabled(False)

    def generate_dns(self):
        if self.chbox_ipv4.checkState()==Qt.CheckState.Checked:
            self.label_text.setText("Your ipv4 DNS👽")
            self.label_text.setGeometry(220, 150, 300, 50)
            self.label_text.setFont(QFont("MV Boli", 20))
            self.btn_generate.hide()
            self.Qcunline2.setText("10.202.10.10")
            self.Qcunline2.show()
            self.Qcunline.show()
            self.Qcunline.setText(self.generate_ipv4())
            self.chbox_ipv4.hide()
            self.chbox_ipv6.hide()
            self.chbox_wireguard.hide()
        
        if self.chbox_ipv6.checkState()==Qt.CheckState.Checked:
            self.label_text.setText("Your ipv6 DNS👽")
            self.label_text.setGeometry(220, 150, 300, 50)
            self.label_text.setFont(QFont("MV Boli", 20))
            self.btn_generate.hide()
            self.Qcunline2.setText(self.generate_ipv6())
            self.Qcunline2.show()
            self.Qcunline.show()
            self.Qcunline.setText(self.generate_ipv6())
            self.chbox_ipv4.hide()
            self.chbox_ipv6.hide()
            self.chbox_wireguard.hide()

    def main(self):
        if self.chbox_wireguard.checkState()==Qt.CheckState.Checked:
            self.chbox_ipv4.hide()
            self.chbox_ipv6.hide()
            self.chbox_wireguard.hide()
            self.label_text.setText("Name for save👽")
            self.label_text.setGeometry(220, 150, 300, 50)
            self.label_text.setFont(QFont("MV Boli", 20))
            self.btn_generate.hide()
            self.btn_save.show()
            self.Qcunline.show()
    
    def save_btn(self):
            private_key = generate_key()
            public_key = os.popen(f'echo {private_key} | wg pubkey').read().strip()
            address = f"10.0.0.{random.randint(2, 254)}/24"
            port = random.randint(51820, 65535)
            dns = f'10.202.10.10,{self.generate_ipv4()}'
            config = generate_config(private_key, public_key, address, port, dns)
            with open(f'{self.Qcunline.text()}.conf', 'w') as f:
                f.write(config)
            msg=QMessageBox()
            msg.setText('Your wireguard config was sucsfuly created')
            msg.exec()
                                        
    def generate_ipv4(self):
    
            return ".".join(f"{random.randint (0, 255)}" for _ in range(4)) 

    def generate_ipv6(self):
    
            return ":".join(f"{random.randint(0, 65535):x}" for _ in range(8))
    

    def on_text_changed(self):
        list=['!','@','#','$','%','^','&','*','()','(',')','-','_','=','+',']','}','[]','[',']','/','?','<','>','"','',',','.']
        if self.Qcunline.text():
            self.btn_next.setDisabled(False)
            if self.Qcunline.text().isdigit() or self.Qcunline.text() in list:
                self.btn_next.setDisabled(True)
        else:
            self.btn_next.setDisabled(True)
        

app = QApplication(sys.argv)
window = Oron()
window.show()
sys.exit(app.exec())