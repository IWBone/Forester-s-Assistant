from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtWidgets import QApplication
from ModuleProviders import Providers
from ModuleBranches import Branches
from ModuleDB import get_db

class Orders:
    def __init__(self, ui):
        self.ui = ui
        self.providers = Providers(ui)
        self.branches = Branches(ui)
        self.clipboard = QApplication.clipboard()

    # Видимость строк
    def _order_change_visibility(self, index):
        visible = getattr(self.ui, f'orders_checkBox_{index}').isChecked()
        for widget_name in (
            f'orders_comboBox_{index + 1}',
            f'orders_comboBox_{index + 5}',
            f'orders_comboBox_{index + 9}',
            f'orders_spinBox_{index + 1}',
        ):
            getattr(self.ui, widget_name).setVisible(visible)

    def order_changeVisibility_1(self):
        self._order_change_visibility(1)

    def order_changeVisibility_2(self):
        self._order_change_visibility(2)

    def order_changeVisibility_3(self):
        self._order_change_visibility(3)

    # Генерация заказа
    def order(self):
        if self.ui.orders_comboBox_13.currentText() != '' and (self.ui.orders_comboBox_1.currentText() != '' or (self.ui.orders_comboBox_2.currentText() != '' or (self.ui.orders_comboBox_3.currentText() != '' or self.ui.orders_comboBox_4.currentText() != ''))):
            with get_db() as db:
                cursor = db.cursor()
                # Заполнение темы
                code_branches = []
                for i in range(1, 5):
                    cursor.execute(
                        "SELECT code_branch FROM branches WHERE branch = ?",
                        [getattr(self.ui, f'orders_comboBox_{i}').currentText()]
                    )
                    code_branches.append(cursor.fetchone()[0])

                branch_suffixes = ['']
                for code in code_branches[1:]:
                    branch_suffixes.append(f' + {code}' if code != '' else '')

                for i in range(1, 4):
                    for j in range(i):
                        if code_branches[i] == code_branches[j]:
                            branch_suffixes[i] = ''
                            break

                code_branch_for_archive = ", ".join([code_branches[0], *branch_suffixes[1:]])
                date_str = self.ui.orders_calendarWidget.selectedDate().toString('dd.MM.yyyy')
                self.ui.orders_pushButton_2.setText(
                    f"Заказ лес {code_branches[0]}{''.join(branch_suffixes[1:])} на {date_str}"
                )

                # Заполнение тела
                bodies = []
                for i in range(1, 5):
                    if code_branches[i - 1] != '':
                        bodies.append(
                            f'{getattr(self.ui, f"orders_comboBox_{i}").currentText()} - '
                            f'{getattr(self.ui, f"orders_comboBox_{i + 4}").currentText()} '
                            f'{getattr(self.ui, f"orders_comboBox_{i + 8}").currentText()}м '
                            f'{getattr(self.ui, f"orders_spinBox_{i}").text()}м3, на {date_str}\n'
                        )
                    else:
                        bodies.append('')
                body = ''.join(bodies)
                self.ui.orders_pushButton_3.setText(f'Добрый день\n{body}\n')

                # Занесение заказа в архив
                cursor.execute("SELECT * FROM archive_orders WHERE theme_order = ? AND body_order = ? AND provider_order = ?",
                                            [self.ui.orders_pushButton_2.text(), self.ui.orders_pushButton_3.text(), self.ui.orders_comboBox_13.currentText()])
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO archive_orders(theme_order, body_order, provider_order, branch_order, date_order) VALUES (?, ?, ?, ?, ?)",
                                                [self.ui.orders_pushButton_2.text(), self.ui.orders_pushButton_3.text(), self.ui.orders_comboBox_13.currentText(), code_branch_for_archive, date_str])
                    db.commit()
            self.order_archive_selection()

    # Копирование темы в буфер обмена
    def order_copytheme(self):
        self.clipboard.setText(self.ui.orders_pushButton_2.text())
    # Копирование тела в буфер обмена
    def order_copybody(self):
        self.clipboard.setText(self.ui.orders_pushButton_3.text())

    # Очистка полей
    def order_clear(self):
        self.branches.branch_initData_1()
        self.providers.init_data_providers_2()
        self.ui.orders_spinBox_1.setValue(0)
        self.ui.orders_spinBox_2.setValue(0)
        self.ui.orders_spinBox_3.setValue(0)
        self.ui.orders_spinBox_4.setValue(0)
        self.ui.orders_pushButton_2.setText('')
        self.ui.orders_pushButton_3.setText('')

    # Архив заказов
    # Инициализация списка тем архива приемок
    def init_archive_order(self):
        self.ui.orders_archive_listWidget_1.clear()
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("SELECT theme_order, rowid FROM archive_orders ORDER BY rowid DESC")
            items = cursor.fetchall()
            for elements in items:
                QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.orders_archive_listWidget_1)

    # Вывод содержимого приемки по теме
    def load_body_order_achive(self, item):
        if ', ' not in item.text():
            return
        self.ui.orders_archive_plainTextEdit_1.setPlainText('')
        with get_db() as db:
            cursor = db.cursor()
            substring = item.text().split(', ')[1]
            cursor.execute("SELECT provider_order FROM archive_orders WHERE rowid = ?", [substring])
            provider = cursor.fetchone()
            cursor.execute("SELECT body_order FROM archive_orders WHERE rowid = ?", [substring])
            themes = cursor.fetchone()
            s = f'{provider[0]}\n{"".join(str(x) for x in themes[0])}'
            self.ui.orders_archive_plainTextEdit_1.setPlainText(s)
        self.ui.orders_archive_label_1.setText(substring)

    # Удаление данных
    def order_archive_delete_item(self):
        if self.ui.orders_archive_label_1.text() == '':
            return
        self.ui.orders_archive_plainTextEdit_1.setPlainText('')
        with get_db() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM archive_orders WHERE rowid = ?", [self.ui.orders_archive_label_1.text()])
            db.commit()
        self.ui.orders_archive_label_1.setText('')
        self.order_archive_selection()

    # Отбор данных
    def order_archive_selection(self):
        self.ui.orders_archive_plainTextEdit_1.setPlainText('')
        with get_db() as db:
            cursor = db.cursor()
            if self.ui.orders_archive_comboBox_1.currentText() != '' and self.ui.orders_archive_comboBox_2.currentText() != '':
                self.ui.orders_archive_listWidget_1.clear()
                cursor.execute("SELECT theme_order, rowid FROM archive_orders WHERE theme_order LIKE ? AND provider_order = ? ORDER BY rowid DESC", ['%' + self.ui.orders_archive_comboBox_1.currentText() + '%', self.ui.orders_archive_comboBox_2.currentText()])
                items = cursor.fetchall()
                for elements in items:
                    QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.orders_archive_listWidget_1)
            elif self.ui.orders_archive_comboBox_1.currentText() == '' and self.ui.orders_archive_comboBox_2.currentText() != '':
                self.ui.orders_archive_listWidget_1.clear()
                cursor.execute("SELECT theme_order, rowid FROM archive_orders WHERE provider_order = ? ORDER BY rowid DESC", [self.ui.orders_archive_comboBox_2.currentText()])
                items = cursor.fetchall()
                for elements in items:
                    QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.orders_archive_listWidget_1)
            elif self.ui.orders_archive_comboBox_1.currentText() != '' and self.ui.orders_archive_comboBox_2.currentText() == '':
                self.ui.orders_archive_listWidget_1.clear()
                cursor.execute("SELECT theme_order, rowid FROM archive_orders WHERE theme_order LIKE ? ORDER BY rowid DESC", ['%' + self.ui.orders_archive_comboBox_1.currentText() + '%'])
                items = cursor.fetchall()
                for elements in items:
                    QListWidgetItem(format(f'{elements[0]}, {elements[1]}'), self.ui.orders_archive_listWidget_1)
            else:
                self.init_archive_order()
