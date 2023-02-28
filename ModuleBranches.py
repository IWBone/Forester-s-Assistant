import sqlite3
from PyQt6.QtWidgets import QListWidgetItem

class branches:
    def __init__(self, ui):
        self.ui = ui
        self.ui.branch_lineEdit_1.setPlaceholderText('Филиал')
        self.ui.branch_lineEdit_2.setPlaceholderText('Код филиала')

        # Вставка пустых строк
        db_branch = sqlite3.connect('Database/branches.db')
        cursor_branch = db_branch.cursor()
        cursor_branch.execute("SELECT * FROM branches WHERE branch = ? AND code_branch = ?", ['', ''])
        if cursor_branch.fetchone() is None:
            cursor_branch.execute("INSERT INTO branches(branch, code_branch) VALUES (?, ?)", ['', ''])
            db_branch.commit()
        cursor_branch.close()
        db_branch.close()

    # Филиалы
    # Вывод списков
    def branch_initData_1(self):
        # Интеграция в вкладку Приемка
        self.ui.acceptance_branch.clear()
        # Интеграция в вкладку Заказы
        self.ui.orders_comboBox_1.clear()
        self.ui.orders_comboBox_2.clear()
        self.ui.orders_comboBox_3.clear()
        self.ui.orders_comboBox_4.clear()
        self.ui.orders_archive_comboBox_1.clear()
        # Интеграция в вкладку Филиалы и приемка
        self.ui.branch_listWidget_1.clear()
        self.ui.branch_listWidget_2.clear()
        self.ui.acceptance_archive_comboBox_2.clear()

        db_branch = sqlite3.connect('Database/branches.db')
        cursor_branch = db_branch.cursor()
        cursor_branch.execute("SELECT branch FROM branches ORDER BY branch")
        items = cursor_branch.fetchall()
        for elements in items:
            QListWidgetItem(format(elements[0]), self.ui.branch_listWidget_1)
            # Интеграция в вкладку заказы
            self.ui.orders_comboBox_1.addItem(elements[0])
            self.ui.orders_comboBox_2.addItem(elements[0])
            self.ui.orders_comboBox_3.addItem(elements[0])
            self.ui.orders_comboBox_4.addItem(elements[0])

        cursor_branch.execute("SELECT code_branch FROM branches ORDER BY branch")
        items = cursor_branch.fetchall()
        for elements in items:
            QListWidgetItem(format(elements[0]), self.ui.branch_listWidget_2)
            # Интеграция в вкладку Приемка
            self.ui.acceptance_branch.addItem(elements[0])
            # Интеграция в вкладку Филиалы и приемка
            self.ui.acceptance_archive_comboBox_2.addItem(elements[0])
            # Интеграция в вкладку Заказы
            self.ui.orders_archive_comboBox_1.addItem(elements[0])
        
        cursor_branch.close()
        db_branch.close()

    # Запись новых данных
    def branch_write_1(self):
        if self.ui.branch_lineEdit_1.text() != '' and self.ui.branch_lineEdit_2.text() != '':
            db_branch = sqlite3.connect('Database/branches.db')
            cursor_branch = db_branch.cursor()
            cursor_branch.execute("SELECT * FROM branches WHERE branch = ? AND code_branch = ?", [self.ui.branch_lineEdit_1.text(), self.ui.branch_lineEdit_2.text()])
            if cursor_branch.fetchone() is None:
                cursor_branch.execute("INSERT INTO branches(branch, code_branch) VALUES (?, ?)", [self.ui.branch_lineEdit_1.text(), self.ui.branch_lineEdit_2.text()])
                db_branch.commit()
            cursor_branch.close()
            db_branch.close()
            self.ui.branch_lineEdit_1.setText('')
            self.ui.branch_lineEdit_2.setText('')
            self.branch_initData_1()

    # Удаление данных
    def branches_delete_item_1(self, item):
        db_branch = sqlite3.connect('Database/branches.db')
        cursor_branch = db_branch.cursor()
        if item.text() != '':
            cursor_branch.execute("DELETE FROM branches WHERE branch = ?", [item.text()])
            db_branch.commit()
            cursor_branch.close()
            db_branch.close()
            self.branch_initData_1()

    def branches_delete_item_2(self, item):
        db_branch = sqlite3.connect('Database/branches.db')
        cursor_branch = db_branch.cursor()
        if item.text() != '':
            cursor_branch.execute("DELETE FROM branches WHERE code_branch = ?", [item.text()])
            db_branch.commit()
            cursor_branch.close()
            db_branch.close()
            self.branch_initData_1()

    # Архив приемок
    # Инициализация списка тем архива приемок
    def init_archive_acceptance(self):
        self.ui.acceptance_archive_listWidget_1.clear()
        db_archive_acceptance = sqlite3.connect('Database/archive_acceptance.db')
        cursor_archive_acceptance = db_archive_acceptance.cursor()
        cursor_archive_acceptance.execute("SELECT theme_acceptance, rowid FROM archive_acceptance ORDER BY rowid DESC")
        items = cursor_archive_acceptance.fetchall()
        for elements in items:
            QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
        cursor_archive_acceptance.close()
        db_archive_acceptance.close()

    # Вывод содержимого приемки по теме
    def load_body_acceptance(self, item):
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        db_archive_acceptance = sqlite3.connect('Database/archive_acceptance.db')
        cursor_archive_acceptance = db_archive_acceptance.cursor()
        cursor_archive_acceptance.execute("SELECT provider_acceptance FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [item.text()[:21], item.text()[23:]])
        provider = cursor_archive_acceptance.fetchone()
        cursor_archive_acceptance.execute("SELECT body_acceptance FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [item.text()[:21], item.text()[23:]])
        body = cursor_archive_acceptance.fetchone()
        s = f'{provider[0]}\n{"".join(str(x) for x in body[0])}'
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText(s)
        cursor_archive_acceptance.close()
        db_archive_acceptance.close()
        self.ui.acceptance_archive_label_1.setText(item.text())

    # Удаление данных
    def acceptance_archive_delete_item(self):
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        db_archive_acceptance = sqlite3.connect('Database/archive_acceptance.db')
        cursor_archive_acceptance = db_archive_acceptance.cursor()
        cursor_archive_acceptance.execute("DELETE FROM archive_acceptance WHERE theme_acceptance = ? AND rowid = ?", [self.ui.acceptance_archive_label_1.text()[:21], self.ui.acceptance_archive_label_1.text()[23:]])
        db_archive_acceptance.commit()
        cursor_archive_acceptance.close()
        db_archive_acceptance.close()
        self.acceptance_archive_selection()

    # Отбор данных
    def acceptance_archive_selection(self):
        self.ui.acceptance_archive_plainTextEdit_2.setPlainText('')
        db_archive_acceptance = sqlite3.connect('Database/archive_acceptance.db')
        cursor_archive_acceptance = db_archive_acceptance.cursor()
        if self.ui.acceptance_archive_comboBox_2.currentText() != '' and self.ui.acceptance_archive_comboBox_1.currentText() != '':
            self.ui.acceptance_archive_listWidget_1.clear()
            cursor_archive_acceptance.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE branch_acceptance = ? AND provider_acceptance = ? ORDER BY rowid DESC", 
                                               [self.ui.acceptance_archive_comboBox_2.currentText(), self.ui.acceptance_archive_comboBox_1.currentText()])
            items = cursor_archive_acceptance.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
        elif self.ui.acceptance_archive_comboBox_2.currentText() == '' and self.ui.acceptance_archive_comboBox_1.currentText() != '':
            self.ui.acceptance_archive_listWidget_1.clear()
            cursor_archive_acceptance.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE provider_acceptance = ? ORDER BY rowid DESC",
                                               [self.ui.acceptance_archive_comboBox_1.currentText()])
            items = cursor_archive_acceptance.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
        elif self.ui.acceptance_archive_comboBox_2.currentText() != '' and self.ui.acceptance_archive_comboBox_1.currentText() == '':
            self.ui.acceptance_archive_listWidget_1.clear()
            cursor_archive_acceptance.execute("SELECT theme_acceptance, rowid FROM archive_acceptance WHERE branch_acceptance = ? ORDER BY rowid DESC",
                                               [self.ui.acceptance_archive_comboBox_2.currentText()])
            items = cursor_archive_acceptance.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.acceptance_archive_listWidget_1)
        else:
            self.init_archive_acceptance()
        cursor_archive_acceptance.close()
        db_archive_acceptance.close()