from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtCore import Qt


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.dlg = uic.loadUi("main_window.ui", self)
        self.show()
        self.tableWidget.setColumnWidth(0, 180)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.addButton.clicked.connect(self.add_item)
        self.removeButton.clicked.connect(self.remove_item)
        self.countButton.clicked.connect(self.count_all)

    def count_all(self):
        print('Count...')
        count_cols = self.tableWidget.columnCount()
        count_rows = self.tableWidget.rowCount()
        print(count_cols, count_rows)

    def add_item(self):
        items_list = {1: "Maslo", 2: "Chleb", 3: "Mleko", 4: "Olej"}
        current_row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(current_row)
        add_that = self.lineEdit.text()
        self.tableWidget.setItem(current_row, 0, QTableWidgetItem(items_list[int(add_that)]))

    def remove_item(self):
        remove_that = self.dlg.tableWidget.currentRow()
        self.dlg.tableWidget.removeRow(remove_that)


def main():
    app = QApplication([])
    window = MainWindows()
    app.exec_()


if __name__ == '__main__':
    main()