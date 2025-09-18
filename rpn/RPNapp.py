from RPNcalc import *
from PySide6.QtWidgets import *
import sys

class MyWidget(QWidget):

    def __init__(self):
        super(MyWidget, self).__init__()
        self.rpn = RPNcalc()

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Calculadora RPN")
        self.numbersList = QListWidget()
        self.hbox = QHBoxLayout()
        self.leftContainer = QVBoxLayout()
        self.rightContainer = QVBoxLayout()

        self.calcNumbers = QGridLayout()

        for i in range(0, 10):
            num = QPushButton(str(i))
            num.setFixedSize(30, 30) 
            num.clicked.connect(self.addEntry)
            if i == 0:
                self.calcNumbers.addWidget(num, 3, 1)
            else:
                self.calcNumbers.addWidget(num, (i-1)//3, (i-1)%3)

        opp = QPushButton('+')
        opp.setFixedSize(30, 30)
        opp.clicked.connect(self.addEntry)
        self.calcNumbers.addWidget(opp, 0, 3)

        opp = QPushButton('-')
        opp.setFixedSize(30, 30)
        opp.clicked.connect(self.addEntry)
        self.calcNumbers.addWidget(opp, 1, 3)

        opp = QPushButton('*')
        opp.setFixedSize(30, 30)
        opp.clicked.connect(self.addEntry)
        self.calcNumbers.addWidget(opp, 2, 3)

        opp = QPushButton('/')
        opp.setFixedSize(30, 30)
        opp.clicked.connect(self.addEntry)
        self.calcNumbers.addWidget(opp, 3, 3)

        opp = QPushButton('C')
        opp.setFixedSize(30, 30)
        opp.clicked.connect(self.addEntry)
        self.calcNumbers.addWidget(opp, 3, 0)

        opp = QPushButton('<-')
        opp.setFixedSize(30, 30)
        opp.clicked.connect(self.addEntry)
        self.calcNumbers.addWidget(opp, 3, 2)

        opp = QPushButton('Enter')
        opp.clicked.connect(self.addEntry)
        self.calcNumbers.addWidget(opp, 4, 0, 1, 4)

        self.inputLineEdit = QLineEdit()
        self.inputLineEdit.setReadOnly(True)
        self.outputLineEdit = QLineEdit()
        self.outputLineEdit.setReadOnly(True)
            
        self.leftContainer.addLayout(self.calcNumbers)

        self.rightContainer.addWidget(self.inputLineEdit)
        self.rightContainer.addWidget(self.numbersList)
        self.rightContainer.addWidget(self.outputLineEdit)
        
        self.hbox.addLayout(self.leftContainer)
        self.hbox.addLayout(self.rightContainer)
        self.setLayout(self.hbox)

    def addEntry(self):
        botaoNum = self.sender()
        string = botaoNum.text()
        self.outputLineEdit.clear()
        try:
            n = int(string)
            self.inputLineEdit.setText(self.inputLineEdit.text() + string)
        except:
            match string:
                case 'Enter':
                    if self.inputLineEdit.text() != '':
                        n = int(self.inputLineEdit.text())
                        self.rpn.enterNumber(n)
                        self.numbersList.addItem(QListWidgetItem(str(n), None, 0))
                        self.numbersList.scrollToBottom()
                        self.inputLineEdit.setText('')
                case '<-':
                    self.inputLineEdit.setText(self.inputLineEdit.text()[:-1])
                case 'C':
                    self.rpn.clearStack()
                    self.numbersList.clear()
                case '+':
                    try:
                        ans = self.rpn.selectOp_sum()
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.addItem(QListWidgetItem(str(ans), None, 0))
                        self.numbersList.scrollToBottom()
                    except Exception as e:
                        self.outputLineEdit.setText(str(e))
                case '-':
                    try:
                        ans = self.rpn.selectOp_diff()
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.addItem(QListWidgetItem(str(ans), None, 0))
                        self.numbersList.scrollToBottom()
                    except Exception as e:
                        self.outputLineEdit.setText(str(e))
                case '*':
                    try:
                        ans = self.rpn.selectOp_prod()
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.addItem(QListWidgetItem(str(ans), None, 0))
                        self.numbersList.scrollToBottom()
                    except Exception as e:
                        self.outputLineEdit.setText(str(e))
                case '/':
                    try:
                        ans, r = self.rpn.selectOp_div()
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.addItem(QListWidgetItem(str(ans), None, 0))
                        self.numbersList.scrollToBottom()
                        self.outputLineEdit.setText(f"Resto: {str(r)}")
                    except ValueError as ve:
                        self.outputLineEdit.setText(str(ve))
                        self.numbersList.takeItem(self.numbersList.count()-1)
                        self.numbersList.takeItem(self.numbersList.count()-1)
                    except Exception as e:
                        self.outputLineEdit.setText(str(e))
                case default:
                    raise ValueError("Operação inválida")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())