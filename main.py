import sqlite3
import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication


class Coffee(QWidget):
    def __init__(self):
        super().__init__()
        database = sqlite3.connect('coffee.sqlite')
        cursor = database.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS coffee (id INTEGER, kind_name STRING, roasting_degree STRING,
                       ground_or_in_grains STRING, taste_description STRING, 
                       price INTEGER, packaging_volume INTEGER)
                       """)
        database.commit()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        view.setModel(model)
        view.resize(800, 300)

        self.setGeometry(300, 100, 800, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee = Coffee()
    coffee.show()
    sys.exit(app.exec())
