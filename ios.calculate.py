import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox,QLabel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget

class oyna(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui()
        
    def ui(self):
        
        self.setStyleSheet("background-color: #0d1a26")
        self.setWindowTitle("CALCULATOR")
        self.setGeometry(700,250,410,750)
        self.setFixedSize(410,750)
        
        self.view=QLabel("",self)
        self.view.setGeometry(15,5,395,230)
        self.view.setAlignment(Qt.AlignRight|Qt.AlignBottom)
        self.view.setFont(QFont("San Francisco",30))
        
        self.c=QPushButton("C",self)
        self.c.setGeometry(10,250,90,90)
        self.c.setFont(QFont("San Francisco",25))
        self.c.setStyleSheet("background-color : #b3b3b3; border-radius : 45px;")
    
        self.percent=QPushButton("%",self)
        self.percent.setGeometry(110,250,90,90)
        self.percent.setFont(QFont("San Francisco",25))
        self.percent.setStyleSheet("background-color : #b3b3b3; border-radius : 45px;")
        
        self.back=QPushButton("B",self)
        self.back.setGeometry(210,250,90,90)
        self.back.setFont(QFont("San Francisco",25))
        self.back.setStyleSheet("background-color : #b3b3b3; border-radius : 45px;")
        
        self.devide=QPushButton("/",self)
        self.devide.setGeometry(310,250,90,90)
        self.devide.setFont(QFont("San Francisco",30))
        self.devide.setStyleSheet("background-color : #ffa31a; border-radius : 45px;color: white")
        
        self.b7=QPushButton("7",self)
        self.b7.setGeometry(10,350,90,90)
        self.b7.setFont(QFont("San Francisco",30))
        self.b7.setStyleSheet("background-color : #404040;border-radius : 45px;color: white")
        
        self.b8=QPushButton("8",self)
        self.b8.setGeometry(110,350,90,90)
        self.b8.setFont(QFont("San Francisco",30))
        self.b8.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.b9=QPushButton("9",self)
        self.b9.setGeometry(210,350,90,90)
        self.b9.setFont(QFont("San Francisco",30))
        self.b9.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.mult=QPushButton("*",self)
        self.mult.setGeometry(310,350,90,90)
        self.mult.setFont(QFont("San Francisco",30))
        self.mult.setStyleSheet("background-color : #ffaa00; border-radius : 45px;color: white")
        
        self.b4=QPushButton("4",self)
        self.b4.setGeometry(10,450,90,90)
        self.b4.setFont(QFont("San Francisco",30))
        self.b4.setStyleSheet("background-color : #404040;border-radius : 45px;color: white")
        
        self.b5=QPushButton("5",self)
        self.b5.setGeometry(110,450,90,90)
        self.b5.setFont(QFont("San Francisco",30))
        self.b5.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.b6=QPushButton("6",self)
        self.b6.setGeometry(210,450,90,90)
        self.b6.setFont(QFont("San Franciscoes",30))
        self.b6.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.minus=QPushButton("-",self)
        self.minus.setGeometry(310,450,90,90)
        self.minus.setFont(QFont("San Francisco",30))
        self.minus.setStyleSheet("background-color : #ffa31a; border-radius : 45px;color: white")
        
        self.b1=QPushButton("1",self)
        self.b1.setGeometry(10,550,90,90)
        self.b1.setFont(QFont("San Francisco",30))
        self.b1.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.b2=QPushButton("2",self)
        self.b2.setGeometry(110,550,90,90)
        self.b2.setFont(QFont("San Francisco",30))
        self.b2.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.b3=QPushButton("3",self)
        self.b3.setGeometry(210,550,90,90)
        self.b3.setFont(QFont("San Francisco",30))
        self.b3.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.plus=QPushButton("+",self)
        self.plus.setGeometry(310,550,90,90)
        self.plus.setFont(QFont("San Francisco",30))
        self.plus.setStyleSheet("background-color : #ffa31a; border-radius : 45px;color: white;")
        
        self.b0=QPushButton("0",self)
        self.b0.setGeometry(10,650,190,90)
        self.b0.setFont(QFont("San Francisco",30))
        self.b0.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.coma=QPushButton(".",self)
        self.coma.setGeometry(210,650,90,90)
        self.coma.setFont(QFont("San Francisco",30))
        self.coma.setStyleSheet("background-color : #404040; border-radius : 45px;color: white")
        
        self.equal=QPushButton("=",self)
        self.equal.setGeometry(310,650,90,90)
        self.equal.setFont(QFont("San Francisco",30))
        self.equal.setStyleSheet("background-color : #ffa31a; border-radius : 45px;color: white;")
                
        self.a=[]
        
        self.b1.clicked.connect(lambda: self.print1(self.b1.text()))
        self.b2.clicked.connect(lambda: self.print1(self.b2.text()))
        self.b3.clicked.connect(lambda: self.print1(self.b3.text()))
        self.b4.clicked.connect(lambda: self.print1(self.b4.text()))
        self.b5.clicked.connect(lambda: self.print1(self.b5.text()))
        self.b6.clicked.connect(lambda: self.print1(self.b6.text()))
        self.b7.clicked.connect(lambda: self.print1(self.b7.text()))
        self.b8.clicked.connect(lambda: self.print1(self.b8.text()))
        self.b9.clicked.connect(lambda: self.print1(self.b9.text()))
        self.plus.clicked.connect(lambda: self.print1(self.plus.text()))
        self.minus.clicked.connect(lambda: self.print1(self.minus.text()))
        self.mult.clicked.connect(lambda: self.print1(self.mult.text()))
        self.devide.clicked.connect(lambda: self.print1(self.devide.text()))
        self.b0.clicked.connect(lambda: self.print1(self.b0.text()))
        self.equal.clicked.connect(self.calculate)
        self.back.clicked.connect(self.left)
        self.coma.clicked.connect(lambda: self.print1(self.coma.text()))
        self.percent.clicked.connect(lambda: self.print1("%"))
        self.c.clicked.connect(self.clear1)
        
    def print1(self,element):
            
        self.a.append(element)
        self.view.setText(self.view.text()+element)
        self.view.setStyleSheet("color: white;")
        self.view.setFont(QFont("Liberation Mono Bold",50))
        
    def calculate(self):
            
        b=["+","-","*","/","",'.']
        
        for i in self.a:
            if i=='%':
                self.cal_per()
            
        if self.a[0] in b or len(self.a)==0:
            m_box=QMessageBox(self)
            m_box.setStyleSheet("background-color: black;color : white")
            m_box.setWindowTitle("####")
            m_box.setText("1- bo'lib son kiritilishi kerak")
            m_box.setIcon(QMessageBox.Critical)
            m_box.setStandardButtons(QMessageBox.Ok)
            m_box.buttonClicked.connect(self.clear1)
            m_box.exec_()
                
        try:
            b = eval(self.view.text())
            if int(b)==b:
                self.view.setText("{}".format(b))
            else:
                self.view.setText("{:.6}".format(b))
        except:
            m_box=QMessageBox(self)
            m_box.setStyleSheet("background-color: black;color : white")
            m_box.setWindowTitle("####")
            m_box.setText("Xatolik")
            m_box.setIcon(QMessageBox.Critical)
            m_box.setStandardButtons(Ok)
            m_box.buttonClicked.connect(self.clear1)
            m_box.exec_()
        
    def left(self):
          
          self.view.clear()
          if len(self.a)>0:
              self.a.pop(len(self.a)-1)
              for i in self.a:
                  self.view.setText(self.view.text()+i)
          else:
              self.view.setText("")
    
    def clear1(self):
        
        self.a.clear()
        self.view.setText("")
       
    def cal_per(self):
        
        pass
                
app=QApplication(sys.argv)
window=oyna()
window.show()
sys.exit(app.exec_())



#%%          EVAL SIZ KALKULATOR BACKEND


































