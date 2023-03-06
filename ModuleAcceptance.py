import sqlite3
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QApplication
from ModuleProviders import providers
from ModuleBranches import branches

class acceptance:
    def __init__(self, ui):
        self.ui = ui
        self.providers = providers(ui)
        self.branches = branches(ui)
        self.clipboard = QApplication.clipboard()

        # Ограничение на ввод по типу данных
        self.ui.acceptance_Lenght_1.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_Lenght_2.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_Lenght_3.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_Lenght_4.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_Lenght_5.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_Lenght_6.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_Lenght_7.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_Lenght_8.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_pieces_1.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_pieces_2.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_pieces_3.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_pieces_4.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_pieces_5.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_pieces_6.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_pieces_7.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_pieces_8.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_value_1.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_value_2.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_value_3.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_value_4.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_value_5.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_value_6.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_value_7.setValidator(QDoubleValidator(self.ui))
        self.ui.acceptance_value_8.setValidator(QDoubleValidator(self.ui))
        self.ui.reject_input_value_1.setValidator(QDoubleValidator(self.ui))
        self.ui.reject_input_value_2.setValidator(QDoubleValidator(self.ui))
        self.ui.reject_reject_1.setValidator(QDoubleValidator(self.ui))
        self.ui.reject_reject_2.setValidator(QDoubleValidator(self.ui))
        self.ui.reject_percent.setValidator(QDoubleValidator(self.ui))

        # Наименования строк
        self.ui.reject_input_value_1.setPlaceholderText('Принимаемый объем')
        self.ui.reject_input_value_2.setPlaceholderText('Принимаемый объем')
        self.ui.reject_reject_1.setPlaceholderText('Брак')
        self.ui.reject_reject_2.setPlaceholderText('Брак')
        self.ui.reject_percent.setPlaceholderText('Процент брака')
        self.ui.reject_result_1.setText('Объем с браком')
        self.ui.reject_result_2.setText('Объем с браком')
        self.ui.reject_input_value_3.setPlaceholderText('Принимаемый объем')
        self.ui.reject_input_value_4.setPlaceholderText('Принимаемый объем')
        self.ui.reject_reject_3.setPlaceholderText('Брак')
        self.ui.reject_reject_4.setPlaceholderText('Брак')
        self.ui.reject_result_3.setText('Объем с браком')
        self.ui.reject_result_4.setText('Объем с браком')
        self.ui.acceptance_Lenght_1.setPlaceholderText('Длина')
        self.ui.acceptance_Lenght_2.setPlaceholderText('Длина')
        self.ui.acceptance_Lenght_3.setPlaceholderText('Длина')
        self.ui.acceptance_Lenght_4.setPlaceholderText('Длина')
        self.ui.acceptance_Lenght_5.setPlaceholderText('Длина')
        self.ui.acceptance_Lenght_6.setPlaceholderText('Длина')
        self.ui.acceptance_Lenght_7.setPlaceholderText('Длина')
        self.ui.acceptance_Lenght_8.setPlaceholderText('Длина')
        self.ui.acceptance_pieces_1.setPlaceholderText('ШТ')
        self.ui.acceptance_pieces_2.setPlaceholderText('ШТ')
        self.ui.acceptance_pieces_3.setPlaceholderText('ШТ')
        self.ui.acceptance_pieces_4.setPlaceholderText('ШТ')
        self.ui.acceptance_pieces_5.setPlaceholderText('ШТ')
        self.ui.acceptance_pieces_6.setPlaceholderText('ШТ')
        self.ui.acceptance_pieces_7.setPlaceholderText('ШТ')
        self.ui.acceptance_pieces_8.setPlaceholderText('ШТ')
        self.ui.acceptance_value_1.setPlaceholderText('Объем')
        self.ui.acceptance_value_2.setPlaceholderText('Объем')
        self.ui.acceptance_value_3.setPlaceholderText('Объем')
        self.ui.acceptance_value_4.setPlaceholderText('Объем')
        self.ui.acceptance_value_5.setPlaceholderText('Объем')
        self.ui.acceptance_value_6.setPlaceholderText('Объем')
        self.ui.acceptance_value_7.setPlaceholderText('Объем')
        self.ui.acceptance_value_8.setPlaceholderText('Объем')
        self.ui.outlook_input_email_c.setPlaceholderText('email в копию')
        self.ui.outlook_input_email_cc.setPlaceholderText('email в скрытую копию')

# # Переключатель процентов брака
    def radiobtn_perc1(self):
        if self.ui.reject_radioButton1.isChecked():
            self.ui.reject_percent.setText('30')
    def radiobtn_perc2(self):
        if self.ui.reject_radioButton2.isChecked():
            self.ui.reject_percent.setText('50')
    def radiobtn_perc3(self):
        if self.ui.reject_radioButton3.isChecked():
            self.ui.reject_percent.setText('')
            self.ui.reject_percent.setFocus()

# # Переключатель процентов брака для приемки
    def acceptance_branch_perc_1(self):
        if self.ui.acceptance_branch_perc_1.isChecked():
            self.ui.acceptance_branch_perc_box.setValue(0)
    def acceptance_branch_perc_2(self):
        if self.ui.acceptance_branch_perc_2.isChecked():
            self.ui.acceptance_branch_perc_box.setValue(30)
    def acceptance_branch_perc_3(self):
        if self.ui.acceptance_branch_perc_3.isChecked():
            self.ui.acceptance_branch_perc_box.setValue(50)
    def acceptance_branch_perc_4(self):
        if self.ui.acceptance_branch_perc_4.isChecked():
            self.ui.acceptance_branch_perc_box.setValue(0)
            self.ui.acceptance_branch_perc_box.setFocus()

# # Вычисление принимаемого брака
    def calculate(self):
        if (self.ui.reject_input_value_1.text() != '' and self.ui.reject_reject_1.text != '') and self.ui.reject_percent.text() != '':
            input_value_1 = float(self.ui.reject_input_value_1.text().replace(',', '.'))
            reject_reject_1 = float(self.ui.reject_reject_1.text().replace(',', '.'))
            reject_percent = float(self.ui.reject_percent.text().replace(',', '.'))
            self.ui.reject_result_1.setText(str(round(input_value_1 + (reject_reject_1 * (reject_percent / 100)), 2)))
        if (self.ui.reject_input_value_2.text() != '' and self.ui.reject_reject_2.text() != '') and self.ui.reject_percent.text() != '':
            input_value_2 = float(self.ui.reject_input_value_2.text().replace(',', '.'))
            reject_reject_2 = float(self.ui.reject_reject_2.text().replace(',', '.'))
            reject_percent = float(self.ui.reject_percent.text().replace(',', '.'))
            self.ui.reject_result_2.setText(str(round(input_value_2 + (reject_reject_2 * (reject_percent / 100)), 2)))
        if (self.ui.reject_input_value_3.text() != '' and self.ui.reject_reject_3.text() != '') and self.ui.reject_percent.text() != '':
            input_value_3 = float(self.ui.reject_input_value_3.text().replace(',', '.'))
            reject_reject_3 = float(self.ui.reject_reject_3.text().replace(',', '.'))
            reject_percent = float(self.ui.reject_percent.text().replace(',', '.'))
            self.ui.reject_result_3.setText(str(round(input_value_3 + (reject_reject_3 * (reject_percent / 100)), 2)))
        if (self.ui.reject_input_value_4.text() != '' and self.ui.reject_reject_4.text() != '') and self.ui.reject_percent.text() != '':
            input_value_4 = float(self.ui.reject_input_value_4.text().replace(',', '.'))
            reject_reject_4 = float(self.ui.reject_reject_4.text().replace(',', '.'))
            reject_percent = float(self.ui.reject_percent.text().replace(',', '.'))
            self.ui.reject_result_4.setText(str(round(input_value_4 + (reject_reject_4 * (reject_percent / 100)), 2)))

# # Очистка приемки с браком
    def cleaner(self):
        self.ui.reject_input_value_1.setText('')
        self.ui.reject_input_value_2.setText('')
        self.ui.reject_input_value_3.setText('')
        self.ui.reject_input_value_4.setText('')
        self.ui.reject_reject_1.setText('')
        self.ui.reject_reject_2.setText('')
        self.ui.reject_reject_3.setText('')
        self.ui.reject_reject_4.setText('')
        self.ui.reject_result_1.setText('Объем с браком')
        self.ui.reject_result_2.setText('Объем с браком')
        self.ui.reject_result_3.setText('Объем с браком')
        self.ui.reject_result_4.setText('Объем с браком')
        self.providers.init_data_providers()

# # Копирование результата вычисления принимаего брака в буфер обмена
    def copy_result_1(self):
        self.clipboard.setText(self.ui.reject_result_1.text())
    def copy_result_2(self):
        self.clipboard.setText(self.ui.reject_result_2.text())
    def copy_result_3(self):
        self.clipboard.setText(self.ui.reject_result_3.text())
    def copy_result_4(self):
        self.clipboard.setText(self.ui.reject_result_4.text())
                
# # Видимость строк
    def changeVisibility_1(self):
        if self.ui.acceptance_checkBox_2.isChecked() == True:
            self.ui.acceptance_Lenght_3.setVisible(True)
            self.ui.acceptance_pieces_3.setVisible(True)
            self.ui.acceptance_value_3.setVisible(True)
            self.ui.acceptance_Lenght_4.setVisible(True)
            self.ui.acceptance_pieces_4.setVisible(True)
            self.ui.acceptance_value_4.setVisible(True)
        else:
            self.ui.acceptance_Lenght_3.setVisible(False)
            self.ui.acceptance_pieces_3.setVisible(False)
            self.ui.acceptance_value_3.setVisible(False)
            self.ui.acceptance_Lenght_4.setVisible(False)
            self.ui.acceptance_pieces_4.setVisible(False)
            self.ui.acceptance_value_4.setVisible(False)
    def changeVisibility_2(self):
        if self.ui.acceptance_checkBox_3.isChecked() == True:
            self.ui.acceptance_Lenght_5.setVisible(True)
            self.ui.acceptance_pieces_5.setVisible(True)
            self.ui.acceptance_value_5.setVisible(True)
            self.ui.acceptance_Lenght_6.setVisible(True)
            self.ui.acceptance_pieces_6.setVisible(True)
            self.ui.acceptance_value_6.setVisible(True)
        else:
            self.ui.acceptance_Lenght_5.setVisible(False)
            self.ui.acceptance_pieces_5.setVisible(False)
            self.ui.acceptance_value_5.setVisible(False)
            self.ui.acceptance_Lenght_6.setVisible(False)
            self.ui.acceptance_pieces_6.setVisible(False)
            self.ui.acceptance_value_6.setVisible(False)
    def changeVisibility_3(self):
        if self.ui.acceptance_checkBox_4.isChecked() == True:
            self.ui.acceptance_Lenght_7.setVisible(True)
            self.ui.acceptance_pieces_7.setVisible(True)
            self.ui.acceptance_value_7.setVisible(True)
            self.ui.acceptance_Lenght_8.setVisible(True)
            self.ui.acceptance_pieces_8.setVisible(True)
            self.ui.acceptance_value_8.setVisible(True)
        else:
            self.ui.acceptance_Lenght_7.setVisible(False)
            self.ui.acceptance_pieces_7.setVisible(False)
            self.ui.acceptance_value_7.setVisible(False)
            self.ui.acceptance_Lenght_8.setVisible(False)
            self.ui.acceptance_pieces_8.setVisible(False)
            self.ui.acceptance_value_8.setVisible(False)

# # Чистка
    def acceptance_clr(self):
        self.ui.acceptance_Lenght_1.setText('')
        self.ui.acceptance_Lenght_2.setText('')
        self.ui.acceptance_Lenght_3.setText('')
        self.ui.acceptance_Lenght_4.setText('')
        self.ui.acceptance_Lenght_5.setText('')
        self.ui.acceptance_Lenght_6.setText('')
        self.ui.acceptance_Lenght_7.setText('')
        self.ui.acceptance_Lenght_8.setText('')
        self.ui.acceptance_pieces_1.setText('')
        self.ui.acceptance_pieces_2.setText('')
        self.ui.acceptance_pieces_3.setText('')
        self.ui.acceptance_pieces_4.setText('')
        self.ui.acceptance_pieces_5.setText('')
        self.ui.acceptance_pieces_6.setText('')
        self.ui.acceptance_pieces_7.setText('')
        self.ui.acceptance_pieces_8.setText('')
        self.ui.acceptance_value_1.setText('')
        self.ui.acceptance_value_2.setText('')
        self.ui.acceptance_value_3.setText('')
        self.ui.acceptance_value_4.setText('')
        self.ui.acceptance_value_5.setText('')
        self.ui.acceptance_value_6.setText('')
        self.ui.acceptance_value_7.setText('')
        self.ui.acceptance_value_8.setText('')
        self.ui.acceptance_btn_copy_1.setText('')
        self.ui.acceptance_btn_copy_2.setText('')
        self.ui.acceptance_branch_perc_1.setChecked(True)
        self.ui.acceptance_checkBox_2.setChecked(False)
        self.ui.acceptance_checkBox_3.setChecked(False)
        self.ui.acceptance_checkBox_4.setChecked(False)
        self.providers.init_data_providers()
        self.providers.init_data_providers_2()
        self.branches.branch_initData_1()

# # Генерация приемки
    def acceptance_generate(self):
        # Защита от запятых
        acceptance_Lenght_1 = self.ui.acceptance_Lenght_1.text().replace(',', '.')
        acceptance_Lenght_2 = self.ui.acceptance_Lenght_2.text().replace(',', '.')
        acceptance_Lenght_3 = self.ui.acceptance_Lenght_3.text().replace(',', '.')
        acceptance_Lenght_4 = self.ui.acceptance_Lenght_4.text().replace(',', '.')
        acceptance_Lenght_5 = self.ui.acceptance_Lenght_5.text().replace(',', '.')
        acceptance_Lenght_6 = self.ui.acceptance_Lenght_6.text().replace(',', '.')
        acceptance_Lenght_7 = self.ui.acceptance_Lenght_7.text().replace(',', '.')
        acceptance_Lenght_8 = self.ui.acceptance_Lenght_8.text().replace(',', '.')
        acceptance_pieces_1 = self.ui.acceptance_pieces_1.text().replace(',', '.')
        acceptance_pieces_2 = self.ui.acceptance_pieces_2.text().replace(',', '.')
        acceptance_pieces_3 = self.ui.acceptance_pieces_3.text().replace(',', '.')
        acceptance_pieces_4 = self.ui.acceptance_pieces_4.text().replace(',', '.')
        acceptance_pieces_5 = self.ui.acceptance_pieces_5.text().replace(',', '.')
        acceptance_pieces_6 = self.ui.acceptance_pieces_6.text().replace(',', '.')
        acceptance_pieces_7 = self.ui.acceptance_pieces_7.text().replace(',', '.')
        acceptance_pieces_8 = self.ui.acceptance_pieces_8.text().replace(',', '.')
        acceptance_value_1 = self.ui.acceptance_value_1.text().replace(',', '.')
        acceptance_value_2 = self.ui.acceptance_value_2.text().replace(',', '.')
        acceptance_value_3 = self.ui.acceptance_value_3.text().replace(',', '.')
        acceptance_value_4 = self.ui.acceptance_value_4.text().replace(',', '.')
        acceptance_value_5 = self.ui.acceptance_value_5.text().replace(',', '.')
        acceptance_value_6 = self.ui.acceptance_value_6.text().replace(',', '.')
        acceptance_value_7 = self.ui.acceptance_value_7.text().replace(',', '.')
        acceptance_value_8 = self.ui.acceptance_value_8.text().replace(',', '.')

        if ((self.ui.acceptance_comboBox_2.currentText() != '' and self.ui.acceptance_branch.currentText() != '') and 
            ((((acceptance_Lenght_1 != '' or acceptance_Lenght_2 != '') and (acceptance_Lenght_5 != '' or acceptance_Lenght_6 != '')) or ((acceptance_Lenght_3 != '' or acceptance_Lenght_4 != '') and (acceptance_Lenght_7 != '' or acceptance_Lenght_8 != ''))) or 
            ((((acceptance_Lenght_1 != '' or acceptance_Lenght_2 != '') or (acceptance_Lenght_3 != '' or acceptance_Lenght_4 != '')) and ((acceptance_Lenght_5 == '' and acceptance_Lenght_6 == '') and (acceptance_Lenght_7 == '' and acceptance_Lenght_8 == '')))))):

            # Код филиала
            db_branch = sqlite3.connect('Database/branches.db')
            cursor_branch = db_branch.cursor()
            cursor_branch.execute("SELECT branch FROM branches where code_branch = ?", [self.ui.acceptance_branch.currentText()])
            branch = cursor_branch.fetchone()[0]

            # Заполнение темы
            if (self.ui.acceptance_branch_perc_box.value() != 0 and (acceptance_Lenght_5 != "" or (acceptance_Lenght_6 != "" or (acceptance_Lenght_7 != "" or acceptance_Lenght_8 != "")))) or self.ui.acceptance_branch_perc_box.value() == 0:
                self.ui.acceptance_btn_copy_1.setText(f"""Приемка {self.ui.acceptance_branch.currentText()} {self.ui.acceptance_calendarWidget.selectedDate().toString('dd.MM.yyyy')}""")

            # Константы
            height_board = 0.025
            width_board = 0.1
            if acceptance_Lenght_1 != "":
                v_board_accept_1 = float(acceptance_Lenght_1) * height_board * width_board
            if acceptance_Lenght_2 != "":
                v_board_accept_2 = float(acceptance_Lenght_2) * height_board * width_board
            if acceptance_Lenght_5 != "":
                v_board_reject_1 = float(acceptance_Lenght_5) * height_board * width_board
            if acceptance_Lenght_6 != "":
                v_board_reject_2 = float(acceptance_Lenght_6) * height_board * width_board     
            height_timber = 0.05
            width_timber = 0.1
            if acceptance_Lenght_3 != "":
                v_timber_accept_1 = float(acceptance_Lenght_3) * height_timber * width_timber
            if acceptance_Lenght_4 != "":
                v_timber_accept_2 = float(acceptance_Lenght_4) * height_timber * width_timber
            if acceptance_Lenght_7 != "":    
                v_timber_reject_1 = float(acceptance_Lenght_7) * height_timber * width_timber
            if acceptance_Lenght_8 != "":
                v_timber_reject_2 = float(acceptance_Lenght_8) * height_timber * width_timber

            # Математика
            # Вычисления первой строки доски
            if acceptance_Lenght_1 != "":
                if acceptance_pieces_1 != "" and acceptance_value_1 != "":
                    None
                elif acceptance_pieces_1 != "":
                    total_v_board_accept_1 = float(acceptance_pieces_1) * v_board_accept_1
                    self.ui.acceptance_value_1.setText(str(round(total_v_board_accept_1, 2)))
                    acceptance_value_1 = str(round(total_v_board_accept_1, 2))
                elif acceptance_value_1 != "":
                    total_pieces_board_accept_1 = float(acceptance_value_1) / v_board_accept_1
                    self.ui.acceptance_pieces_1.setText(str(round(total_pieces_board_accept_1)))
                    acceptance_pieces_1 = str(round(total_pieces_board_accept_1))

            # Вычисление второй строки доски
            if acceptance_Lenght_2 != "":
                if acceptance_pieces_2 != "" and acceptance_value_2 != "":
                    None
                elif acceptance_pieces_2 != "":
                    total_v_board_accept_2 = float(acceptance_pieces_2) * v_board_accept_2
                    self.ui.acceptance_value_2.setText(str(round(total_v_board_accept_2, 2)))
                    acceptance_value_2 = str(round(total_v_board_accept_2, 2))
                elif acceptance_value_2 != "":
                    total_pieces_board_accept_2 = float(acceptance_value_2) / v_board_accept_2
                    self.ui.acceptance_pieces_2.setText(str(round(total_pieces_board_accept_2)))
                    acceptance_pieces_2 = str(round(total_pieces_board_accept_2))

            # Вычисления первой строки бруса
            if acceptance_Lenght_3 != "":
                if acceptance_pieces_3 != "" and acceptance_value_3 != "":
                    None
                elif acceptance_pieces_3 != "":
                    total_v_board_accept_3 = float(acceptance_pieces_3) * v_timber_accept_1
                    self.ui.acceptance_value_3.setText(str(round(total_v_board_accept_3, 2)))
                    acceptance_value_3 = str(round(total_v_board_accept_3, 2))
                elif acceptance_value_3 != "":
                    total_pieces_board_accept_3 = float(acceptance_value_3) / v_timber_accept_1
                    self.ui.acceptance_pieces_3.setText(str(round(total_pieces_board_accept_3)))
                    acceptance_pieces_3 = str(round(total_pieces_board_accept_3))

            # Вычисление второй строки бруса
            if acceptance_Lenght_4 != "":
                if acceptance_pieces_4 != "" and acceptance_value_4 != "":
                    None
                elif acceptance_pieces_4 != "":
                    total_v_board_accept_4 = float(acceptance_pieces_4) * v_timber_accept_2
                    self.ui.acceptance_value_4.setText(str(round(total_v_board_accept_4, 2)))
                    acceptance_value_4 = str(round(total_v_board_accept_4, 2))
                elif acceptance_value_4 != "":
                    total_pieces_board_accept_4 = float(acceptance_value_4) / v_timber_accept_2
                    self.ui.acceptance_pieces_4.setText(str(round(total_pieces_board_accept_4)))
                    acceptance_pieces_4 = str(round(total_pieces_board_accept_4))
            
            # Вычисления первой строки брака доски
            if acceptance_Lenght_5 != "":
                if acceptance_pieces_5 != "" and acceptance_value_5 != "":
                    None
                elif acceptance_pieces_5 != "":
                    total_v_board_reject_5 = float(acceptance_pieces_5) * v_board_reject_1
                    self.ui.acceptance_value_5.setText(str(round(total_v_board_reject_5, 2)))
                    acceptance_value_5 = str(round(total_v_board_reject_5, 2))
                elif acceptance_value_5 != "":
                    total_pieces_board_reject_5 = float(acceptance_value_5) / v_board_reject_1
                    self.ui.acceptance_pieces_5.setText(str(round(total_pieces_board_reject_5)))
                    acceptance_pieces_5 = str(round(total_pieces_board_reject_5))
                # Расчет для процента брака
                if ((acceptance_Lenght_1 != "" and acceptance_Lenght_2 != "") and acceptance_Lenght_6 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_1 = round(float(acceptance_value_1) + (float(acceptance_value_5) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                    acceptance_value_with_reject_2 = acceptance_value_2
                elif ((acceptance_Lenght_1 != "" and acceptance_Lenght_2 != "") and acceptance_Lenght_6 != "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_1 = round(float(acceptance_value_1) + (float(acceptance_value_5) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                elif (acceptance_Lenght_1 != "" and acceptance_Lenght_2 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_1 = round(float(acceptance_value_1) + (float(acceptance_value_5) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                elif ((acceptance_Lenght_1 == "" and acceptance_Lenght_2 != "") and acceptance_Lenght_6 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_2 = round(float(acceptance_value_2) + (float(acceptance_value_5) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                    acceptance_value_with_reject_1 = ''
                else:
                    acceptance_value_with_reject_1 = ''
            else:
                acceptance_value_with_reject_1 = ''

            # Вычисление второй строки брака доски
            if acceptance_Lenght_6 != "":
                if acceptance_pieces_6 != "" and acceptance_value_6 != "":
                    None
                elif acceptance_pieces_6 != "":
                    total_v_board_reject_6 = float(acceptance_pieces_6) * v_board_reject_2
                    self.ui.acceptance_value_6.setText(str(round(total_v_board_reject_6, 2)))
                    acceptance_value_6 = (round(total_v_board_reject_6, 2))
                elif acceptance_value_6 != "":
                    total_pieces_board_reject_6 = float(acceptance_value_6) / v_board_reject_2
                    self.ui.acceptance_pieces_6.setText(str(round(total_pieces_board_reject_6)))
                    acceptance_pieces_6 = str(round(total_pieces_board_reject_6))
                # Расчет для процента брака
                if ((acceptance_Lenght_2 != "" and acceptance_Lenght_1 != "") and acceptance_Lenght_5 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_2 = round(float(acceptance_value_2) + (float(acceptance_value_6) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                    acceptance_value_with_reject_1 = acceptance_value_1
                elif ((acceptance_Lenght_2 != "" and acceptance_Lenght_1 != "") and acceptance_Lenght_5 != "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_2 = round(float(acceptance_value_2) + (float(acceptance_value_6) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                elif (acceptance_Lenght_2 != "" and acceptance_Lenght_1 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_2 = round(float(acceptance_value_2) + (float(acceptance_value_6) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                elif ((acceptance_Lenght_2 == "" and acceptance_Lenght_1 != "") and acceptance_Lenght_5 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_1 = round(float(acceptance_value_1) + (float(acceptance_value_6) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                    acceptance_value_with_reject_2 = ''
                else:
                    acceptance_value_with_reject_2 = ''
            else:
                acceptance_value_with_reject_2 = ''

            # Вычисления первой строки брака бруса
            if acceptance_Lenght_7 != "":
                if acceptance_pieces_7 != "" and acceptance_value_7 != "":
                    None
                elif acceptance_pieces_7 != "":
                    total_v_board_reject_7 = float(acceptance_pieces_7) * v_timber_reject_1
                    self.ui.acceptance_value_7.setText(str(round(total_v_board_reject_7, 2)))
                    acceptance_value_7 = str(round(total_v_board_reject_7, 2))
                elif acceptance_value_7 != "":
                    total_pieces_board_reject_7 = float(acceptance_value_7) / v_timber_reject_1
                    self.ui.acceptance_pieces_7.setText(str(round(total_pieces_board_reject_7)))
                    acceptance_pieces_7 = str(round(total_pieces_board_reject_7))
                # Расчет для процента брака
                if ((acceptance_Lenght_3 != "" and acceptance_Lenght_4 != "") and acceptance_Lenght_8 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_3 = round(float(acceptance_value_3) + (float(acceptance_value_7) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                    acceptance_value_with_reject_4 = acceptance_value_4
                elif ((acceptance_Lenght_3 != "" and acceptance_Lenght_4 != "") and acceptance_Lenght_8 != "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_3 = round(float(acceptance_value_3) + (float(acceptance_value_7) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                elif (acceptance_Lenght_3 != "" and acceptance_Lenght_4 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_3 = round(float(acceptance_value_3) + (float(acceptance_value_7) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                elif ((acceptance_Lenght_3 == "" and acceptance_Lenght_4 != "") and acceptance_Lenght_8 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_4 = round(float(acceptance_value_4) + (float(acceptance_value_7) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                    acceptance_value_with_reject_3 = ''
                else:
                    acceptance_value_with_reject_3 = ''
            else:
                acceptance_value_with_reject_3 = ''

            # Вычисление второй строки брака бруса
            if acceptance_Lenght_8 != "":
                if acceptance_pieces_8 != "" and acceptance_value_8 != "":
                    None
                elif acceptance_pieces_8 != "":
                    total_v_board_reject_8 = float(acceptance_pieces_8) * v_timber_reject_2
                    self.ui.acceptance_value_8.setText(str(round(total_v_board_reject_8, 2)))
                    acceptance_value_8 = str(round(total_v_board_reject_8, 2))
                elif acceptance_value_8 != "":
                    total_pieces_board_reject_8 = float(acceptance_value_8) / v_timber_reject_2
                    self.ui.acceptance_pieces_8.setText(str(round(total_pieces_board_reject_8)))
                    acceptance_pieces_8 = str(round(total_pieces_board_reject_8))
                # Расчет для процента брака
                if ((acceptance_Lenght_4 != "" and acceptance_Lenght_3 != "") and acceptance_Lenght_7 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_4 = round(float(acceptance_value_4) + (float(acceptance_value_8) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                    acceptance_value_with_reject_3 = acceptance_value_3
                elif ((acceptance_Lenght_4 != "" and acceptance_Lenght_3 != "") and acceptance_Lenght_7 != "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_4 = round(float(acceptance_value_4) + (float(acceptance_value_8) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                elif (acceptance_Lenght_4 != "" and acceptance_Lenght_3 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_4 = round(float(acceptance_value_4) + (float(acceptance_value_8) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                elif ((acceptance_Lenght_4 == "" and acceptance_Lenght_3 != "") and acceptance_Lenght_7 == "") and self.ui.acceptance_branch_perc_box.value() != 0:
                    acceptance_value_with_reject_3 = round(float(acceptance_value_3) + (float(acceptance_value_8) * (self.ui.acceptance_branch_perc_box.value() / 100)), 2)
                    acceptance_value_with_reject_4 = ''
                else:
                    acceptance_value_with_reject_4 = ''
            else:
                acceptance_value_with_reject_4 = ''
            #  Заполнение в кнопки для копирования
            self.ui.reject_result_1.setText(str(acceptance_value_with_reject_1))
            self.ui.reject_result_2.setText(str(acceptance_value_with_reject_2))
            self.ui.reject_result_3.setText(str(acceptance_value_with_reject_3))
            self.ui.reject_result_4.setText(str(acceptance_value_with_reject_4))

            # Сложение объема для архива
            if acceptance_value_1 == '':
                acceptance_value_1 = 0
            if acceptance_value_2 == '':
                acceptance_value_2 = 0
            if acceptance_value_3 == '':
                acceptance_value_3 = 0
            if acceptance_value_4 == '':
                acceptance_value_4 = 0
            value_board_for_archive = float(acceptance_value_1) + float(acceptance_value_2)
            value_timber_for_archive = float(acceptance_value_3) + float(acceptance_value_4)
            # Доска
            if acceptance_value_with_reject_1 != '' and acceptance_value_with_reject_2 != '':
                value_board_with_reject_for_archive = acceptance_value_with_reject_1 + acceptance_value_with_reject_2
            elif acceptance_value_with_reject_1 != '' and acceptance_value_with_reject_2 == '':
                if acceptance_value_2 == '':
                    acceptance_value_2 = 0
                value_board_with_reject_for_archive = acceptance_value_with_reject_1 + acceptance_value_2
            elif acceptance_value_with_reject_1 == '' and acceptance_value_with_reject_2 != '':
                if acceptance_value_1 == '':
                    acceptance_value_1 = 0
                value_board_with_reject_for_archive = acceptance_value_1 + acceptance_value_with_reject_2
            else:
                value_board_with_reject_for_archive = value_board_for_archive
            # Брус
            if acceptance_value_with_reject_3 != '' and acceptance_value_with_reject_4 != '':
                value_timber_with_reject_for_archive = acceptance_value_with_reject_3 + acceptance_value_with_reject_4
            elif acceptance_value_with_reject_3 != '' and acceptance_value_with_reject_4 == '':
                if acceptance_value_4 == '':
                    acceptance_value_4 = 0
                value_timber_with_reject_for_archive = acceptance_value_with_reject_3 + acceptance_value_4
            elif acceptance_value_with_reject_3 == '' and acceptance_value_with_reject_4 != '':
                if acceptance_value_3 == '':
                    acceptance_value_3 = 0
                value_timber_with_reject_for_archive = acceptance_value_3 + acceptance_value_with_reject_4
            else:
                value_timber_with_reject_for_archive = value_timber_for_archive

            # Вывод в тело письма
            # Доска
            if acceptance_Lenght_1 != "" and acceptance_Lenght_2 != "":
                body_1 = f'Доска, принято\n{str(acceptance_Lenght_1)}м - {str(acceptance_pieces_1)}шт - {str(acceptance_value_1)}м3\n{str(acceptance_Lenght_2)}м - {str(acceptance_pieces_2)}шт - {str(acceptance_value_2)}м3\n'
                body_1_with_reject = f'Доска, принято\n{str(acceptance_Lenght_1)}м - {str(acceptance_pieces_1)}шт - {str(acceptance_value_1)}м3 (C браком принято - {str(acceptance_value_with_reject_1)}м3)\n{str(acceptance_Lenght_2)}м - {str(acceptance_pieces_2)}шт - {str(acceptance_value_2)}м3 (C браком принято - {str(acceptance_value_with_reject_2)}м3)\n'
            elif acceptance_Lenght_1 != "":
                body_1 = f'Доска, принято\n{str(acceptance_Lenght_1)}м - {str(acceptance_pieces_1)}шт - {str(acceptance_value_1)}м3\n'
                body_1_with_reject = f'Доска, принято\n{str(acceptance_Lenght_1)}м - {str(acceptance_pieces_1)}шт - {str(acceptance_value_1)}м3 (C браком принято - {str(acceptance_value_with_reject_1)}м3)\n'
            elif acceptance_Lenght_2 != "":
                body_1 = f'Доска, принято\n{str(acceptance_Lenght_2)}м - {str(acceptance_pieces_2)}шт - {str(acceptance_value_2)}м3\n'
                body_1_with_reject = f'Доска, принято\n{str(acceptance_Lenght_2)}м - {str(acceptance_pieces_2)}шт - {str(acceptance_value_2)}м3 (C браком принято - {str(acceptance_value_with_reject_2)}м3)\n'
            else:
                body_1 = ""
                body_1_with_reject = ""

            # Брус
            if acceptance_Lenght_3 != "" and acceptance_Lenght_4 != "":
                body_2 = f'Брус, принято\n{str(acceptance_Lenght_3)}м - {str(acceptance_pieces_3)}шт - {str(acceptance_value_3)}м3\n{str(acceptance_Lenght_4)}м - {str(acceptance_pieces_4)}шт - {str(acceptance_value_4)}м3\n'
                body_2_with_reject = f'Брус, принято\n{str(acceptance_Lenght_3)}м - {str(acceptance_pieces_3)}шт - {str(acceptance_value_3)}м3 (C браком принято - {str(acceptance_value_with_reject_3)}м3)\n{str(acceptance_Lenght_4)}м - {str(acceptance_pieces_4)}шт - {str(acceptance_value_4)}м3 (C браком принято - {str(acceptance_value_with_reject_4)}м3)\n'
            elif acceptance_Lenght_3 != "":
                body_2 = f'Брус, принято\n{str(acceptance_Lenght_3)}м - {str(acceptance_pieces_3)}шт - {str(acceptance_value_3)}м3\n'
                body_2_with_reject = f'Брус, принято\n{str(acceptance_Lenght_3)}м - {str(acceptance_pieces_3)}шт - {str(acceptance_value_3)}м3 (C браком принято - {str(acceptance_value_with_reject_3)}м3)\n'
            elif acceptance_Lenght_4 != "":
                body_2 = f'Брус, принято\n{str(acceptance_Lenght_4)}м - {str(acceptance_pieces_4)}шт - {str(acceptance_value_4)}м3\n'
                body_2_with_reject = f'Брус, принято\n{str(acceptance_Lenght_4)}м - {str(acceptance_pieces_4)}шт - {str(acceptance_value_4)}м3 (C браком принято - {str(acceptance_value_with_reject_4)}м3)\n'
            else:
                body_2 = ""
                body_2_with_reject = ""

            # Брак доски
            if acceptance_Lenght_5 != "" and acceptance_Lenght_6 != "":
                body_3 = f'Доска, брак\n{str(acceptance_Lenght_5)}м - {str(acceptance_pieces_5)}шт - {str(acceptance_value_5)}м3\n{str(acceptance_Lenght_6)}м - {str(acceptance_pieces_6)}шт - {str(acceptance_value_6)}м3\n'
            elif acceptance_Lenght_5 != "":
                body_3 = f'Доска, брак\n{str(acceptance_Lenght_5)}м - {str(acceptance_pieces_5)}шт - {str(acceptance_value_5)}м3\n'
            elif acceptance_Lenght_6 != "":
                body_3 = f'Доска, брак\n{str(acceptance_Lenght_6)}м - {str(acceptance_pieces_6)}шт - {str(acceptance_value_6)}м3\n'
            else:
                body_3 = ""

            # Брак бруса
            if acceptance_Lenght_7 != "" and acceptance_Lenght_8 != "":
                body_4 = f'Брус, брак\n{str(acceptance_Lenght_7)}м - {str(acceptance_pieces_7)}шт - {str(acceptance_value_7)}м3\n{str(acceptance_Lenght_8)}м - {str(acceptance_pieces_8)}шт - {str(acceptance_value_8)}м3\n'
            elif acceptance_Lenght_7 != "":
                body_4 = f'Брус, брак\n{str(acceptance_Lenght_7)}м - {str(acceptance_pieces_7)}шт - {str(acceptance_value_7)}м3\n'
            elif acceptance_Lenght_8 != "":
                body_4 = f'Брус, брак\n{str(acceptance_Lenght_8)}м - {str(acceptance_pieces_8)}шт - {str(acceptance_value_8)}м3\n'
            else:
                body_4 = ""

            # Заполнение тела
            if (self.ui.acceptance_branch_perc_box.value() != 0 and (acceptance_Lenght_5 != "" or (acceptance_Lenght_6 != "" or (acceptance_Lenght_7 != "" or acceptance_Lenght_8 != "")))) or self.ui.acceptance_branch_perc_box.value() == 0:
                if acceptance_Lenght_1 != "" or (acceptance_Lenght_2 != "" or (acceptance_Lenght_3 != "" or (acceptance_Lenght_4 != "" or (acceptance_Lenght_5 != "" or (acceptance_Lenght_6 != "" or (acceptance_Lenght_7 != "" or acceptance_Lenght_8 != "")))))):
                    date = self.ui.acceptance_calendarWidget.selectedDate().toString('dd.MM.yyyy')
                    if self.ui.acceptance_number.currentText() != "":
                        car_number = f'{self.ui.acceptance_number.currentText()}\n'
                    else:
                        car_number = ""
                    body = f'{body_1}{body_2}{body_3}{body_4}'
                    self.ui.acceptance_btn_copy_2.setText(f'Добрый день\n\n{date}\n{car_number.upper()}{branch}\n\n{body}\n')
                    body_with_reject = f'Добрый день\n\n{date}\n{car_number.upper()}{branch}\n\n{body_1_with_reject}{body_2_with_reject}{body_3}{body_4}\n'

            # Занесение номера машина в базу
            if self.ui.acceptance_number.currentText() != '':
                db_car_number = sqlite3.connect('Database/car_numbers.db')
                cursor_car_number = db_car_number.cursor()
                cursor_car_number.execute("SELECT car_number, provider FROM car_numbers WHERE car_number = ? AND provider = ?", [self.ui.acceptance_number.currentText().upper(), self.ui.acceptance_comboBox_2.currentText()])
                if cursor_car_number.fetchone() is None:
                    cursor_car_number.execute("INSERT INTO car_numbers(car_number, provider) VALUES (?, ?)", [self.ui.acceptance_number.currentText().upper(), self.ui.acceptance_comboBox_2.currentText()])
                    db_car_number.commit()
                self.providers.init_data_providers()
                cursor_car_number.close()
                db_car_number.close()

            # Занесение приемки в архив
            db_archive_acceptance = sqlite3.connect('Database/archive_acceptance.db')
            cursor_archive_acceptance = db_archive_acceptance.cursor()
            # Без брака
            if self.ui.acceptance_branch_perc_box.value() == 0:
                if self.ui.acceptance_btn_copy_1.text() != '' and self.ui.acceptance_btn_copy_2.text() != '':
                    cursor_archive_acceptance.execute("SELECT * FROM archive_acceptance WHERE theme_acceptance = ? AND body_acceptance = ? AND provider_acceptance = ?", [self.ui.acceptance_btn_copy_1.text(), self.ui.acceptance_btn_copy_2.text(), self.ui.acceptance_comboBox_2.currentText()])
                    if cursor_archive_acceptance.fetchone() is None:
                        cursor_archive_acceptance.execute("INSERT INTO archive_acceptance(theme_acceptance, body_acceptance, provider_acceptance, branch_acceptance, date_acceptance, board_value_acceptance, timber_value_acceptance) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                                           [self.ui.acceptance_btn_copy_1.text(), self.ui.acceptance_btn_copy_2.text(), self.ui.acceptance_comboBox_2.currentText(), self.ui.acceptance_branch.currentText(), date, value_board_for_archive, value_timber_for_archive])
                        db_archive_acceptance.commit()
            # С браком
            elif self.ui.acceptance_branch_perc_box.value() != 0 and (acceptance_value_with_reject_1 != '' or (acceptance_value_with_reject_2 != '' or (acceptance_value_with_reject_3 != '' or acceptance_value_with_reject_4 != ''))):
                if self.ui.acceptance_btn_copy_1.text() != '' and self.ui.acceptance_btn_copy_2.text() != '':
                    cursor_archive_acceptance.execute("SELECT * FROM archive_acceptance WHERE theme_acceptance = ? AND body_acceptance = ? AND provider_acceptance = ?", [self.ui.acceptance_btn_copy_1.text(), self.ui.acceptance_btn_copy_2.text(), self.ui.acceptance_comboBox_2.currentText()])
                    if cursor_archive_acceptance.fetchone() is None:
                        cursor_archive_acceptance.execute("INSERT INTO archive_acceptance(theme_acceptance, body_acceptance, provider_acceptance, branch_acceptance, date_acceptance, board_value_acceptance, timber_value_acceptance) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                                           [self.ui.acceptance_btn_copy_1.text(), body_with_reject, self.ui.acceptance_comboBox_2.currentText(), self.ui.acceptance_branch.currentText(), date, value_board_with_reject_for_archive, value_timber_with_reject_for_archive])
                        db_archive_acceptance.commit()
            self.branches.acceptance_archive_selection()

            cursor_branch.close()
            cursor_archive_acceptance.close()
            db_branch.close()
            db_archive_acceptance.close()

    # Копирование темы в буфер обмена
    def copytheme(self):
        self.clipboard.setText(self.ui.acceptance_btn_copy_1.text())
    # Копирование тела в буфер обмена
    def copybody(self):
        self.clipboard.setText(self.ui.acceptance_btn_copy_2.text())