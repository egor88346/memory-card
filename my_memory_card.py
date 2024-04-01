#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout,QRadioButton,QGroupBox,QButtonGroup,QMessageBox
import random

class Question:
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3


questions = list()
questions.append(Question('Какой сегодня год?','2023','2134','2002','1999'))
questions.append(Question('Сколько месяцев в году?','12','23','32','499'))
questions.append(Question('Сколько дней в году?','32','365','123','465'))
questions.append(Question('В каком месяце 28 дней?','февраль','март','апрель','август'))
questions.append(Question('Сколько хромосом у человека?','46','48','23','32'))
questions.append(Question('Сколько лап у собаки?','3','2','6','4'))
questions.append(Question('Минимальная оценка в школе?','2','3','4','5'))

def next_question():
    if win.q_index == len(questions):
        win.q_index = 0 
        show_score()
        win.score = 0

    if win.q_index == 0:
        random.shuffle(questions)
        
    ask(questions[win.q_index])
    win.q_index += 1

def show_score():
    percent = win.score / win.total * 100
    percent = round(percent,1)

    text = 'Уважаемый пользователь!\n'
    text += 'Ваш результат составил ' + str(percent) + '%\n'
    text += 'Вы ответили правильно на '+ str(win.score) + 'из' + str(win.total) + 'вопросов\n'
    text += 'После закрытия данного окна - тест начнётся заново.Удачи!'

    msg_box = QMessageBox()
    msg_box.setWindowTitle('Результат тестирования')
    msg_box.setText(text)
    msg_box.exec()

def ask(q):
    question_text.setText(q.question)
    random.shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

def check_answer():
    for rbtn in answers:
        if rbtn.isChecked():
            if rbtn.text() == answers[0].text():
                right_text.setText('Правильно')
                right_answer.setText('Поздравляем!')
                win.score += 1
            else:
                right_text.setText('Неправильно')
                right_answer.setText('Правильный ответ:'+answers[0].text())





def show_result():
    grp_box.hide()
    grp_box_result.show()
    btn.setText('Следующий вопрос')
    check_answer()

def show_question():
    next_question()
    grp_box.show()
    grp_box_result.hide()
    btn.setText('Ответить')
    radio_group.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    radio_group.setExclusive(True)


def start_test():
    if btn.text()== 'Ответить':
        show_result()
    else:
        show_question()


        


app = QApplication([])
win = QWidget()
win.setWindowTitle('MemoryCard')
win.resize(400,300)
win.q_index = 0
win.score = 0
win.total = len(questions)


question_text = QLabel('Тут будет вопрос')
grp_box = QGroupBox('Варианты ответа')
radio1 = QRadioButton('1 вариант')
radio2 = QRadioButton('2 вариант')
radio3 = QRadioButton('3 вариант')
radio4 = QRadioButton('4 вариант')
btn = QPushButton('Ответить')
grp_box_result = QGroupBox('Результат')
right_text = QLabel('Правильно/Неправильно')
right_answer = QLabel('Правильный ответ')

radio_group = QButtonGroup()
radio_group.addButton(radio1)
radio_group.addButton(radio2)
radio_group.addButton(radio3)
radio_group.addButton(radio4)
answers = [radio1,radio2,radio3,radio4]




main_layout = QVBoxLayout()
h_main1 = QHBoxLayout()
h_main2 = QHBoxLayout()
h_main3 = QHBoxLayout()
grp_box_layout = QHBoxLayout()
grp_box_v1 = QVBoxLayout()
grp_box_v2 = QVBoxLayout()
grp_box_result_layout = QVBoxLayout()

grp_box_result_layout.addWidget(right_text)
grp_box_result_layout.addWidget(right_answer,alignment=Qt.AlignCenter)
grp_box_result.setLayout(grp_box_result_layout)


grp_box_v1.addWidget(radio1)
grp_box_v1.addWidget(radio2)
grp_box_v2.addWidget(radio3)
grp_box_v2.addWidget(radio4)
grp_box_layout.addLayout(grp_box_v1)
grp_box_layout.addLayout(grp_box_v2)
grp_box.setLayout(grp_box_layout)

h_main1.addWidget(question_text,alignment=Qt.AlignCenter)
h_main2.addWidget(grp_box)
h_main2.addWidget(grp_box_result)
h_main3.addStretch(1)
h_main3.addWidget(btn,stretch=2)
h_main3.addStretch(1)

main_layout.addLayout(h_main1)
main_layout.addLayout(h_main2)
main_layout.addLayout(h_main3)

win.setLayout(main_layout)
win.show()
btn.clicked.connect(start_test)

next_question()
grp_box_result.hide()
app.exec()

