# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import datetime
from playsound import playsound

class sayacWindow_tyt(QMainWindow):
	def __init__(self):
		super().__init__()
		#self.fl = True
		# setting title
		self.setWindowTitle("Python Stop watch")

		# setting geometry
		self.setGeometry(100, 100, 400, 500)

		# calling method
		self.UiComponents()

		# showing all the widgets
		#self.show()

	# method for widgets
	def UiComponents(self):

		# counter
		self.count_sec = 00
		self.count_min = 15
		self.count_hour = 2

		# creating flag
		self.flag = False

		# creating a label to show the time
		self.label = QLabel(self)

		# setting geometry of label
		self.label.setGeometry(75, 100, 250, 70)

		# adding border to the label
		self.label.setStyleSheet("border : 4px solid black;")

		# setting text to the label
		self.label.setText("{}:{}:{}".format(self.count_hour,self.count_min,self.count_sec))

		# setting font to the label
		self.label.setFont(QFont('Arial', 25))

		# setting alignment to the text of label
		self.label.setAlignment(Qt.AlignCenter)

		# creating start button
		start = QPushButton("Start", self)

		# setting geometry to the button
		start.setGeometry(125, 250, 150, 40)

		# add action to the method
		start.pressed.connect(self.Start)

		# creating pause button
		pause = QPushButton("Pause", self)

		# setting geometry to the button
		pause.setGeometry(125, 300, 150, 40)

		# add action to the method
		pause.pressed.connect(self.Pause)

		# creating reset button
		re_set = QPushButton("Re-set", self)

		# setting geometry to the button
		re_set.setGeometry(125, 350, 150, 40)

		# add action to the method
		re_set.pressed.connect(self.Re_set)

		# creating a timer object
		timer = QTimer(self)

		# adding action to timer
		timer.timeout.connect(self.showTime)

		# update the timer every tenth second
		timer.start(1000)
	def showWid(self):
		self.show()

	# method called by timer
	def showTime(self):

		# checking if flag is true


		if self.flag: #self.flag
			# incrementing the counter
			self.count_sec -= 1
		"""if self.count_sec == 0 and self.count_min == 0 and self.count_hour == 0:
			playsound("dimbillan-dayi.mp3")"""

		# getting text from count
		text = str(datetime.timedelta(seconds=self.count_sec, minutes=self.count_min, hours=self.count_hour))
		if text == "0:00:00":
			playsound("C:/Users/ASUS/Downloads/dimbillan.mp3")
			self.flag = False
			self.count_sec = 00
			self.count_min = 15
			self.count_hour = 2


		# showing text
		self.label.setText(text)


	def Start(self):

		# making flag to true
		self.flag = True

	def Pause(self):

		# making flag to False
		self.flag = False

	def Re_set(self):

		# making flag to false
		self.flag = False
		self.count_sec = 00
		self.count_min = 15
		self.count_hour = 2
		# reseeting the count
		text = str(datetime.timedelta(seconds=self.count_sec, minutes=self.count_min, hours=self.count_hour))

		# setting text to label
		self.label.setText(str(text))

class sayacWindow_ayt(QMainWindow):
	def __init__(self):
		super().__init__()
		#self.fl = True
		# setting title
		self.setWindowTitle("Python Stop watch")

		# setting geometry
		self.setGeometry(100, 100, 400, 500)

		# calling method
		self.UiComponents()

		# showing all the widgets
		#self.show()

	# method for widgets
	def UiComponents(self):

		# counter
		self.count_sec = 00
		self.count_min = 00
		self.count_hour = 3

		# creating flag
		self.flag = False

		# creating a label to show the time
		self.label = QLabel(self)

		# setting geometry of label
		self.label.setGeometry(75, 100, 250, 70)

		# adding border to the label
		self.label.setStyleSheet("border : 4px solid black;")

		# setting text to the label
		self.label.setText("{}:{}:{}".format(self.count_hour,self.count_min,self.count_sec))

		# setting font to the label
		self.label.setFont(QFont('Arial', 25))

		# setting alignment to the text of label
		self.label.setAlignment(Qt.AlignCenter)

		# creating start button
		start = QPushButton("Start", self)

		# setting geometry to the button
		start.setGeometry(125, 250, 150, 40)

		# add action to the method
		start.pressed.connect(self.Start)

		# creating pause button
		pause = QPushButton("Pause", self)

		# setting geometry to the button
		pause.setGeometry(125, 300, 150, 40)

		# add action to the method
		pause.pressed.connect(self.Pause)

		# creating reset button
		re_set = QPushButton("Re-set", self)

		# setting geometry to the button
		re_set.setGeometry(125, 350, 150, 40)

		# add action to the method
		re_set.pressed.connect(self.Re_set)

		# creating a timer object
		timer = QTimer(self)

		# adding action to timer
		timer.timeout.connect(self.showTime)

		# update the timer every tenth second
		timer.start(1000)
	def showWid(self):
		self.show()

	# method called by timer
	def showTime(self):

		# checking if flag is true


		if self.flag: #self.flag
			# incrementing the counter
			self.count_sec -= 1
		"""if self.count_sec == 0 and self.count_min == 0 and self.count_hour == 0:
			playsound("dimbillan-dayi.mp3")"""

		# getting text from count
		text = str(datetime.timedelta(seconds=self.count_sec, minutes=self.count_min, hours=self.count_hour))
		if text == "0:00:00":
			self.flag = False
			playsound("dimbillan-dayi.mp3")


		# showing text
		self.label.setText(text)


	def Start(self):

		# making flag to true
		self.flag = True

	def Pause(self):

		# making flag to False
		self.flag = False

	def Re_set(self):

		# making flag to false
		self.flag = False
		self.count_sec = 00
		self.count_min = 00
		self.count_hour = 3
		# reseeting the count
		text = str(datetime.timedelta(seconds=self.count_sec, minutes=self.count_min, hours=self.count_hour))

		# setting text to label
		self.label.setText(str(text))


# create pyqt5 app
