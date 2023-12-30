from  PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QSpinBox, QHBoxLayout, QRadioButton, QButtonGroup,QGroupBox 
 
menu_btn = QPushButton("Меню") 
rest_btn = QPushButton("Відпочити") 
 
time_spin = QSpinBox() 
time_spin.setValue(3) 
 
time_lb = QLabel("Хвилини") 
 
row1 = QHBoxLayout() 
row1.addWidget(menu_btn) 
row1.addStretch(1) 
row1.addWidget(rest_btn) 
row1.addWidget(time_spin) 
row1.addWidget(time_lb) 
 
main_line = QVBoxLayout() 
main_line.addLayout(row1) 
 
que_lb = QLabel("Питання") 
 
ans1 = QRadioButton("А") 
ans2 = QRadioButton("Б") 
ans3 = QRadioButton("В") 
ans4 = QRadioButton("Г") 
 
row2 = QHBoxLayout() 
row2.addWidget(ans1) 
row2.addWidget(ans2) 
row2.addWidget(ans3) 
row2.addWidget(ans4) 
 
main_line.addWidget(que_lb) 
 
radio_group = QButtonGroup() 
 
radio_group.addButton(ans1) 
radio_group.addButton(ans2) 
radio_group.addButton(ans3) 
radio_group.addButton(ans4) 
 
main_line.addLayout(row2)

group = QGroupBox("Варіанти відповідей")

cal1 = QVBoxLayout()
cal2 = QVBoxLayout()

cal1.addWidget(ans1)
cal1.addWidget(ans2)
cal2.addWidget(ans3)
cal2.addWidget(ans4)

row1.addLayout(cal1)
row1.addLayout(cal2)

group.setLayout(row2)

#main_line = QVBoxLayout()
main_line.addLayout(row1)
main_line.addWidget(que_lb)
main_line.addWidget(group)
main_line.addWidget(ans)