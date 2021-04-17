from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QButtonGroup
from random import shuffle, randint

class Qu():
    def __init__(self, que, right_ans, w1, w2, w3):
        self.que = que
        self.right_ans = right_ans
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

qlist = []
qlist.append(Qu('P это', 'мощность', 'сила', 'работа', 'время'))
qlist.append(Qu('самый угнетённый класс', 'черные люди', 'украинцы', 'женщины', 'геи'))
qlist.append(Qu('когда было образовано ссср', '31.12.1922', '31.12.2020', '01.01.1922', '01.01.1923'))
qlist.append(Qu('столица нигерии', 'абуджа', 'нигер', 'москва', 'канберра'))
qlist.append(Qu('пиглины используют', 'меч либо арбалет', 'топор либо арбалет', 'меч либо топор', 'только топор'))
qlist.append(Qu('столица нигера', 'ниамей', 'нигерия', 'негр', 'лондон'))
qlist.append(Qu('научное название чешуйницы', 'Lepisma saccharina', 'Araneus', 'Oniscidea', 'Niggers'))
qlist.append(Qu('второй закон ньютона', 'F = ma', 'F(тяж.) = mg', 'F(1) = -F(2)', 'ΔU = Q + A'))
qlist.append(Qu('буква пси', 'ψ', 'α', 'λ', 'σ'))
qlist.append(Qu('формула фтороводорода', 'HF', 'HCl', 'HBr', 'HI'))

app = QApplication([])

ok = QPushButton('Ответить')
que = QLabel('question')

rgb = QGroupBox('Варианты ответа')
a1 = QRadioButton('1')
a2 = QRadioButton('2')
a3 = QRadioButton('3')
a4 = QRadioButton('4')

lo1 = QHBoxLayout()
lo2 = QVBoxLayout()
lo3 = QVBoxLayout()
lo2.addWidget(a1)
lo2.addWidget(a2)
lo3.addWidget(a3)
lo3.addWidget(a4)

lo1.addLayout(lo2)
lo1.addLayout(lo3)

rgb.setLayout(lo1)

agb = QGroupBox('Результат теста')
result = QLabel('nigga')
cor = QLabel('ответ')

rgroup = QButtonGroup()
rgroup.addButton(a1)
rgroup.addButton(a2)
rgroup.addButton(a3)
rgroup.addButton(a4)

lr = QVBoxLayout()
lr.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
lr.addWidget(cor, alignment = Qt.AlignHCenter, stretch = 2)
agb.setLayout(lr)

lline1 = QHBoxLayout()
lline2 = QHBoxLayout()
lline3 = QHBoxLayout()

lline1.addWidget(que, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
lline2.addWidget(rgb)
lline2.addWidget(agb)

lline3.addStretch(1)
lline3.addWidget(ok, stretch = 2)
lline3.addStretch(1)

lcard = QVBoxLayout()

lcard.addLayout(lline1, stretch = 2)
lcard.addLayout(lline2, stretch = 8)
lcard.addStretch(1)
lcard.addLayout(lline3, stretch = 5)
lcard.addStretch(1)
lcard.setSpacing(5)

def show_result():
    rgb.hide()
    agb.show()
    ok.setText('следующий')

def show_q():
    agb.hide()
    rgb.show()
    ok.setText('Ответить')
    rgroup.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    rgroup.setExclusive(True)

answers = [a1, a2, a3, a4]

def ask(q: Qu):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    que.setText(q.que)
    cor.setText(q.right_ans)
    show_q()

def show_correct(res):
    result.setText(res)
    show_result()

def next_q():
    mc.t += 1
    print('Статистика\n- Всего вопросов: ', mc.t, '\n- Правильных ответов: ', mc.sc, '\n- Процент правильных ответов: ', mc.perc, '%')
    cur_q = randint(0, len(qlist) -1)
    q = qlist[cur_q]
    ask(q)

def cok():
    if ok.text() == 'Ответить':
        check()
    else:
        next_q()

def check():
    if answers[0].isChecked():
        show_correct('верно')
        mc.sc += 1
        mc.perc = (mc.sc/mc.t) * 100
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('нет')
            mc.perc = (mc.sc/mc.t) * 100




agb.hide()
mc = QWidget()
mc.setLayout(lcard)
mc.setWindowTitle('memory card')
ok.clicked.connect(cok)
mc.sc = 0
mc.t = 0
mc.perc = 0
next_q()
mc.resize(400, 300)
mc.show()
app.exec()