import os
import time
import sys
from PyQt4 import QtCore, QtGui, Qt
class Window(QtGui.QWidget):
    def __init__(self, parent=None):
	super(Window, self).__init__(parent)
        self.setWindowTitle("Locker!")
        self.setWindowIcon(QtGui.QIcon('locker.png'))
        self.show()
	self.setStyleSheet("background-color: white;")
	
        self.path_label = QtGui.QLabel("File Path:", self)
	self.path_label.setStyleSheet("color: rgb(0, 0, 205);")

	self.myTextBox = QtGui.QLineEdit()
	self.myTextBox.setStyleSheet("color: rgb(0, 0, 205);")
	
	self.button = QtGui.QPushButton('Choose File', self)
	self.button.setStyleSheet("background-color: rgb(219, 141, 10);")
        self.button.clicked.connect(self.open)
        	
        self.passwd_label = QtGui.QLabel("Password:", self)
	self.passwd_label.setStyleSheet("color: rgb(0, 0, 205);")
		   
	self.le = QtGui.QLineEdit()
	self.le.setStyleSheet("color: rgb(0, 0, 205);")
	self.le.setEchoMode(QtGui.QLineEdit.Password)
	self.le.show()
	
	self.btn1 = QtGui.QPushButton("Get set, Go!!")
	self.btn1.setStyleSheet("background-color: rgb(34,139,34);")
	self.btn1.clicked.connect(self.go)
		
	self.leo = QtGui.QLineEdit()
	self.leo.setStyleSheet("color: rgb(0,100,0);")
	self.leo.setReadOnly(True)

	self.exit = QtGui.QPushButton('Exit', self)
	self.exit.setStyleSheet("background-color: rgb(128,0,0);")
	self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
	
	layout = QtGui.QGridLayout(self)

	layout.addWidget(self.path_label, 0, 0)
	layout.addWidget(self.myTextBox, 0, 1)
        layout.addWidget(self.button, 0, 2)
	layout.addWidget(self.passwd_label, 1, 0)
	layout.addWidget(self.le, 1, 1)
	layout.addWidget(self.btn1, 2, 1)
	layout.addWidget(self.leo, 3, 1)
	layout.addWidget(self.exit, 4, 1)

	self.setLayout(layout)
    
    def open(self):
	global m
	m = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
	self.myTextBox.setText(m)
    def go(self):
	global k, text
	k = str(self.le.text())
	
	l=''.join(format(ord(x)) for x in k)
	start_time = time.time()
	y=int(l)
	v=y%101110100970
	s=0
	u=[]
	for d in l:
	 p=int(d)
	 s=s+p
	 if s>245:
	  break
	with open(m, "rb") as binary_file:
	 data = binary_file.read()
	 binary_file.seek(0)
	 for couple_bytes in binary_file.read(2):
	  c=' '.join(map(bin,bytearray(couple_bytes)))
	  d=int(c,2)
	  u.append(chr(d))
	 g=''.join(u)
	 if g=="xc":
	  for couple_bytes in binary_file.read(1):
	   c=' '.join(map(bin,bytearray(couple_bytes)))
	   d=int(c,2)
	   e=d^s
	  if v==e:
	   os.remove(m)
	   ff=open(m, "wb")
	   for couple_bytes in binary_file.read():
	    c=' '.join(map(bin,bytearray(couple_bytes)))
	    d=int(c,2)
	    e=d^s
	    ff.write(chr(e))
	   text=("Decryption Successful..")
	  else:
	   text=("WrOng PasswOrd..!!")
	 else:
	  os.remove(m)
	  ff=open(m, "wb")
	  q=v^s
	  i=chr(q)
	  ff.write("x")
	  ff.write("c")
	  ff.write(i)
	  binary_file.seek(0)
	  for couple_bytes in binary_file.read():
	   c=' '.join(map(bin,bytearray(couple_bytes)))
	   d=int(c,2)
	   e=d^s
	   ff.write(chr(e))
	  text=("Encryption Successful..")
	  ff.close()
	print("--- %s seconds ---" % (time.time() - start_time))
	self.leo.setText(text)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

