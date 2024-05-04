#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import*
from random import randint
#создание элементов интерфейса
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Розыгрыш')
my_win.move(100,100)
my_win.resize(400,200)
#привязка элементов к вертикальной линии
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
rnum = QLabel('?')
rnum.setFont(QFont('Arial', 50))

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(rnum, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)
#обработка событий
def show_winner():
    x = randint(1, 100)
    rnum.setText(str(x))
    text.setText('ПОБЕДИТЕЛЬ!')
button.clicked.connect(show_winner)

#запуск приложения
my_win.show()
app.exec_()