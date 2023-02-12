import sys
import sqlite3
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from ModuleAcceptance import acceptance
from ModuleProviders import providers
from ModuleBranches import branches
from ModuleOrders import orders
from ModuleOutlook import outlook
# import PyInstaller.__main__

# PyInstaller.__main__.run([
#     '--onefile',
#     '--add-data=Calc_wood.ui;.',
#     '--add-data=icon.ico;.',
#     '--add-data=ModuleAcceptance.py;.',
#     '--add-data=ModuleBranches.py;.',
#     '--add-data=ModuleOrders.py;.',
#     '--add-data=ModuleOutlook.py;.',
#     '--add-data=ModuleProviders.py;.',
#     'main.py'
# ])

with sqlite3.connect("database.db") as db:
    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS base_nubers(
        number_car VARCHAR,
        provider VARCHAR
    );
    CREATE TABLE IF NOT EXISTS providers(
        providers VARCHAR,
        providers_email_acceptances VARCHAR,
        providers_email_orders VARCHAR
    );
    CREATE TABLE IF NOT EXISTS branches(
        branches VARCHAR,
        code_branches VARCHAR
    );
    CREATE TABLE IF NOT EXISTS archive_acceptance(
        provider_acceptance VARCHAR,
        branch_acceptance VARCHAR,
        theme_acceptance VARCHAR,
        body_acceptance TEXT
    );
    CREATE TABLE IF NOT EXISTS archive_order(
        provider_order VARCHAR,
        branch_order VARCHAR,
        theme_order VARCHAR,
        body_order TEXT
    );
    CREATE TABLE IF NOT EXISTS outlook_copy_emails(
        outlook_copy_emails VARCHAR
    );
    CREATE TABLE IF NOT EXISTS outlook_ccopy_emails(
        outlook_ccopy_emails VARCHAR
    )
    """
    cursor.executescript(query)

class CalcWood(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = uic.loadUi("Calc_wood.ui", self)
        self.acceptance = acceptance(ui)
        self.clipboard = QApplication.clipboard()
        self.providers = providers(ui)
        self.branches = branches(ui)
        self.orders = orders(ui)
        self.outlook = outlook(ui)
        self.show()

        # # Кастомизация
        version = 'v2.0'
        title = "Ассистент лесника" + ' ' + version
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("icon.ico"))

        # # Связи
        # # Приемка с браком
        self.reject_calculate_button.clicked.connect(self.acceptance.calculate)
        self.reject_clean_button.clicked.connect(self.acceptance.cleaner)
        self.reject_radioButton1.toggled.connect(self.acceptance.radiobtn_perc1)
        self.reject_radioButton2.toggled.connect(self.acceptance.radiobtn_perc2)
        self.reject_radioButton2.setChecked(True)
        self.reject_radioButton3.toggled.connect(self.acceptance.radiobtn_perc3)
        self.reject_result_1.clicked.connect(self.acceptance.copy_result_1)
        self.reject_result_2.clicked.connect(self.acceptance.copy_result_2)

        # # Подбор В и Ш
        # self.radioButton_lenght.toggled.connect(self.radioBtn_lenght)
        # self.radioButton_lenght.setChecked(True)
        # self.radioButton_lenght_2.toggled.connect(self.radioBtn_lenght)

        # # Генератор приемки
        self.acceptance_Lenght_3.setVisible(False)
        self.acceptance_pieces_3.setVisible(False)
        self.acceptance_value_3.setVisible(False)
        self.acceptance_Lenght_4.setVisible(False)
        self.acceptance_pieces_4.setVisible(False)
        self.acceptance_value_4.setVisible(False)
        self.acceptance_Lenght_5.setVisible(False)
        self.acceptance_pieces_5.setVisible(False)
        self.acceptance_value_5.setVisible(False)
        self.acceptance_Lenght_6.setVisible(False)
        self.acceptance_pieces_6.setVisible(False)
        self.acceptance_value_6.setVisible(False)
        self.acceptance_Lenght_7.setVisible(False)
        self.acceptance_pieces_7.setVisible(False)
        self.acceptance_value_7.setVisible(False)
        self.acceptance_Lenght_8.setVisible(False)
        self.acceptance_pieces_8.setVisible(False)
        self.acceptance_value_8.setVisible(False)
        self.acceptance_btn_generate.clicked.connect(self.acceptance.acceptance_generate)
        self.acceptance_btn_copy_1.clicked.connect(self.acceptance.copytheme)
        self.acceptance_btn_copy_2.clicked.connect(self.acceptance.copybody)
        self.reject_clean_button.clicked.connect(self.acceptance.acceptance_clr)
        self.acceptance_checkBox_2.stateChanged.connect(self.acceptance.changeVisibility_1)
        self.acceptance_checkBox_3.stateChanged.connect(self.acceptance.changeVisibility_2)
        self.acceptance_checkBox_4.stateChanged.connect(self.acceptance.changeVisibility_3)
        self.acceptance_branch_perc_1.toggled.connect(self.acceptance.acceptance_branch_perc_1)
        self.acceptance_branch_perc_1.setChecked(True)
        self.acceptance_branch_perc_2.toggled.connect(self.acceptance.acceptance_branch_perc_2)
        self.acceptance_branch_perc_3.toggled.connect(self.acceptance.acceptance_branch_perc_3)
        self.acceptance_branch_perc_4.toggled.connect(self.acceptance.acceptance_branch_perc_4)

        # # Поставщики
        self.info_listWidget_1.itemClicked.connect(self.providers.load_providers)
        self.info_listWidget_2.itemClicked.connect(self.providers.delete_item)
        self.info_pushButton_1.clicked.connect(self.providers.write_data_providers)
        self.info_pushButton_2.clicked.connect(self.providers.write_data_providers_2)
        self.info_listWidget_3.itemClicked.connect(self.providers.delete_item_2)
        self.providers.init_data_providers()
        self.providers.init_data_providers_2()

        # # Филиалы
        self.branch_pushButton_1.clicked.connect(self.branches.branch_write_1)
        self.branch_listWidget_1.itemClicked.connect(self.branches.branches_delete_item_1)
        self.branch_listWidget_2.itemClicked.connect(self.branches.branches_delete_item_2)
        self.branches.branch_initData_1()
        
        # # Архив приемок
        self.branches.init_archive_acceptance()
        self.acceptance_archive_listWidget_1.itemClicked.connect(self.branches.load_body_acceptance)
        self.acceptance_archive_pushButton_1.clicked.connect(self.branches.acceptance_archive_delete_item)
        self.acceptance_archive_pushButton_2.clicked.connect(self.branches.acceptance_archive_selection)

        # # Заказ
        self.orders_comboBox_2.setVisible(False)
        self.orders_comboBox_6.setVisible(False)
        self.orders_comboBox_10.setVisible(False)
        self.orders_spinBox_2.setVisible(False)
        self.orders_comboBox_3.setVisible(False)
        self.orders_comboBox_7.setVisible(False)
        self.orders_comboBox_11.setVisible(False)
        self.orders_spinBox_3.setVisible(False)
        self.orders_comboBox_4.setVisible(False)
        self.orders_comboBox_8.setVisible(False)
        self.orders_comboBox_12.setVisible(False)
        self.orders_spinBox_4.setVisible(False)
        self.orders_pushButton_1.clicked.connect(self.orders.order)
        self.orders_pushButton_6.clicked.connect(self.orders.order_clear)
        self.orders_pushButton_2.clicked.connect(self.orders.order_copytheme)
        self.orders_pushButton_3.clicked.connect(self.orders.order_copybody)
        self.orders_checkBox_1.stateChanged.connect(self.orders.order_changeVisibility_1)
        self.orders_checkBox_2.stateChanged.connect(self.orders.order_changeVisibility_2)
        self.orders_checkBox_3.stateChanged.connect(self.orders.order_changeVisibility_3)
        self.orders.init_archive_order()

        # Архив заказов
        self.orders_archive_listWidget_1.itemClicked.connect(self.orders.load_body_order_achive)
        self.orders_archive_pushButton_2.clicked.connect(self.orders.order_archive_delete_item)
        self.orders_archive_pushButton_1.clicked.connect(self.orders.order_archive_selection)

        # Outlook
        self.outlook_btn_change_visible.clicked.connect(self.outlook.outlook_change_visible_settings)
        self.outlook.outlook_init_copy_emails()
        self.outlook_btn_save_email_c.clicked.connect(self.outlook.outlook_save_copy_emails)
        self.outlook_list_email_c.itemClicked.connect(self.outlook.outlook_delete_copy_emails)
        self.outlook.outlook_init_ccopy_emails()
        self.outlook_btn_save_email_cc.clicked.connect(self.outlook.outlook_save_ccopy_emails)
        self.outlook_list_email_cc.itemClicked.connect(self.outlook.outlook_delete_ccopy_emails)
        self.outlook.outlook_init_email_signature()
        self.outlook_btn_paste_image_sign.clicked.connect(self.outlook.outlook_paste_signature_image)
        self.outlook_btn_save_signature.clicked.connect(self.outlook.outlook_save_email_signature)
        self.outlook_btn_delete_signature.clicked.connect(self.outlook.outlook_delete_email_signature)
        self.outlook_send_acceptance.clicked.connect(self.outlook.outlook_send_acceptance)
        self.outlook_send_order.clicked.connect(self.outlook.outlook_send_order)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalcWood()
    sys.exit(app.exec())