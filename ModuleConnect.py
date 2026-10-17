from PyQt6.QtGui import QIcon
import asyncio
from PyQt6.QtWidgets import QApplication
from ModuleAcceptance import Acceptance
from ModuleProviders import Providers
from ModuleBranches import Branches
from ModuleOrders import Orders
from ModuleOutlook import Outlook
from ModuleConverter import Converter
from ModuleDB import init_db

# Создание таблиц в единой БД forester.db
init_db()

class Connect:
    def __init__(self, ui):
        self.ui = ui
        self.providers = Providers(ui)
        self.branches = Branches(ui)
        self.acceptance = Acceptance(ui)
        self.clipboard = QApplication.clipboard()
        self.providers = Providers(ui)
        self.branches = Branches(ui)
        self.orders = Orders(ui)
        self.outlook = Outlook(ui)
        self.converter = Converter(ui)

        # # Кастомизация
        version = 'v4.2'
        title = "Ассистент лесника" + ' ' + version
        self.ui.setWindowTitle(title)
        #self.ui.setWindowIcon(QIcon("icon.ico"))

        # # Связи
        # # Приемка с браком
        self.ui.reject_calculate_button.clicked.connect(self.acceptance.calculate)
        self.ui.reject_clean_button.clicked.connect(self.acceptance.cleaner)
        self.ui.reject_radioButton1.toggled.connect(self.acceptance.radiobtn_perc1)
        self.ui.reject_radioButton2.toggled.connect(self.acceptance.radiobtn_perc2)
        self.ui.reject_radioButton2.setChecked(True)
        self.ui.reject_radioButton3.toggled.connect(self.acceptance.radiobtn_perc3)
        self.ui.reject_result_1.clicked.connect(self.acceptance.copy_result_1)
        self.ui.reject_result_2.clicked.connect(self.acceptance.copy_result_2)
        self.ui.reject_result_3.clicked.connect(self.acceptance.copy_result_3)
        self.ui.reject_result_4.clicked.connect(self.acceptance.copy_result_4)

        # # Подбор В и Ш
        # self.radioButton_lenght.toggled.connect(self.radioBtn_lenght)
        # self.radioButton_lenght.setChecked(True)
        # self.radioButton_lenght_2.toggled.connect(self.radioBtn_lenght)

        # # Генератор приемки
        self.ui.acceptance_Lenght_3.setVisible(False)
        self.ui.acceptance_pieces_3.setVisible(False)
        self.ui.acceptance_value_3.setVisible(False)
        self.ui.acceptance_Lenght_4.setVisible(False)
        self.ui.acceptance_pieces_4.setVisible(False)
        self.ui.acceptance_value_4.setVisible(False)
        self.ui.acceptance_Lenght_5.setVisible(False)
        self.ui.acceptance_pieces_5.setVisible(False)
        self.ui.acceptance_value_5.setVisible(False)
        self.ui.acceptance_Lenght_6.setVisible(False)
        self.ui.acceptance_pieces_6.setVisible(False)
        self.ui.acceptance_value_6.setVisible(False)
        self.ui.acceptance_Lenght_7.setVisible(False)
        self.ui.acceptance_pieces_7.setVisible(False)
        self.ui.acceptance_value_7.setVisible(False)
        self.ui.acceptance_Lenght_8.setVisible(False)
        self.ui.acceptance_pieces_8.setVisible(False)
        self.ui.acceptance_value_8.setVisible(False)
        self.ui.acceptance_btn_generate.clicked.connect(self.acceptance.acceptance_generate)
        self.ui.acceptance_btn_copy_1.clicked.connect(self.acceptance.copytheme)
        self.ui.acceptance_btn_copy_2.clicked.connect(self.acceptance.copybody)
        self.ui.reject_clean_button.clicked.connect(self.acceptance.acceptance_clr)
        self.ui.acceptance_checkBox_2.stateChanged.connect(self.acceptance.changeVisibility_1)
        self.ui.acceptance_checkBox_3.stateChanged.connect(self.acceptance.changeVisibility_2)
        self.ui.acceptance_checkBox_4.stateChanged.connect(self.acceptance.changeVisibility_3)
        self.ui.acceptance_branch_perc_1.toggled.connect(self.acceptance.acceptance_branch_perc_1)
        self.ui.acceptance_branch_perc_1.setChecked(True)
        self.ui.acceptance_branch_perc_2.toggled.connect(self.acceptance.acceptance_branch_perc_2)
        self.ui.acceptance_branch_perc_3.toggled.connect(self.acceptance.acceptance_branch_perc_3)
        self.ui.acceptance_branch_perc_4.toggled.connect(self.acceptance.acceptance_branch_perc_4)

        # # Поставщики
        self.ui.info_listWidget_1.itemClicked.connect(self.providers.load_providers)
        self.ui.info_listWidget_2.itemClicked.connect(self.providers.delete_item)
        self.ui.info_pushButton_1.clicked.connect(self.providers.write_data_providers)
        self.ui.info_pushButton_2.clicked.connect(self.providers.write_data_providers_2)
        self.ui.info_listWidget_3.itemClicked.connect(self.providers.delete_item_2)
        self.providers.init_data_providers()
        self.providers.init_data_providers_2()

        # # Филиалы
        self.ui.branch_pushButton_1.clicked.connect(self.branches.branch_write_1)
        self.ui.branch_listWidget_1.itemClicked.connect(self.branches.branches_delete_item_1)
        self.ui.branch_listWidget_2.itemClicked.connect(self.branches.branches_delete_item_2)
        self.branches.branch_initData_1()

        # # Архив приемок
        self.branches.init_archive_acceptance()
        self.ui.acceptance_archive_listWidget_1.itemClicked.connect(self.branches.load_body_acceptance)
        self.ui.acceptance_archive_pushButton_1.clicked.connect(self.branches.acceptance_archive_delete_item)
        self.ui.acceptance_archive_pushButton_2.clicked.connect(self.branches.acceptance_archive_selection)

        # # Заказ
        self.ui.orders_comboBox_2.setVisible(False)
        self.ui.orders_comboBox_6.setVisible(False)
        self.ui.orders_comboBox_10.setVisible(False)
        self.ui.orders_spinBox_2.setVisible(False)
        self.ui.orders_comboBox_3.setVisible(False)
        self.ui.orders_comboBox_7.setVisible(False)
        self.ui.orders_comboBox_11.setVisible(False)
        self.ui.orders_spinBox_3.setVisible(False)
        self.ui.orders_comboBox_4.setVisible(False)
        self.ui.orders_comboBox_8.setVisible(False)
        self.ui.orders_comboBox_12.setVisible(False)
        self.ui.orders_spinBox_4.setVisible(False)
        self.ui.orders_pushButton_1.clicked.connect(self.orders.order)
        self.ui.orders_pushButton_6.clicked.connect(self.orders.order_clear)
        self.ui.orders_pushButton_2.clicked.connect(self.orders.order_copytheme)
        self.ui.orders_pushButton_3.clicked.connect(self.orders.order_copybody)
        self.ui.orders_checkBox_1.stateChanged.connect(self.orders.order_changeVisibility_1)
        self.ui.orders_checkBox_2.stateChanged.connect(self.orders.order_changeVisibility_2)
        self.ui.orders_checkBox_3.stateChanged.connect(self.orders.order_changeVisibility_3)
        self.orders.init_archive_order()

        # Архив заказов
        self.ui.orders_archive_listWidget_1.itemClicked.connect(self.orders.load_body_order_achive)
        self.ui.orders_archive_pushButton_2.clicked.connect(self.orders.order_archive_delete_item)
        self.ui.orders_archive_pushButton_1.clicked.connect(self.orders.order_archive_selection)

        # Outlook
        self.ui.outlook_btn_change_visible.clicked.connect(self.outlook.outlook_change_visible_settings)
        self.outlook.outlook_init_copy_emails()
        self.ui.outlook_btn_save_email_c.clicked.connect(self.outlook.outlook_save_copy_emails)
        self.ui.outlook_list_email_c.itemClicked.connect(self.outlook.outlook_delete_copy_emails)
        self.outlook.outlook_init_ccopy_emails()
        self.ui.outlook_btn_save_email_cc.clicked.connect(self.outlook.outlook_save_ccopy_emails)
        self.ui.outlook_list_email_cc.itemClicked.connect(self.outlook.outlook_delete_ccopy_emails)
        self.outlook.outlook_init_email_signature()
        self.ui.outlook_btn_paste_image_sign.clicked.connect(self.outlook.outlook_paste_signature_image)
        self.ui.outlook_btn_save_signature.clicked.connect(self.outlook.outlook_save_email_signature)
        self.ui.outlook_btn_delete_signature.clicked.connect(self.outlook.outlook_delete_email_signature)
        self.ui.outlook_send_acceptance.clicked.connect(self.outlook.outlook_send_acceptance)
        self.ui.outlook_send_order.clicked.connect(self.outlook.outlook_send_order)

        # Конвертер
        self.ui.other_converter.clicked.connect(self.converter.convert_pdf2img)
        # self.ui.other_converter.clicked.connect(self.converter.as_convert_pdf2img)
        # self.ui.other_converter.clicked.connect(lambda: asyncio.run(self.converter.as_thr_convert_pdf2img()))
        # Подбор ширины и высоты
        self.ui.other_calculate_1.clicked.connect(self.converter.selection)
        self.ui.other_radioButton_lenght_1.toggled.connect(self.converter.lenght_selection_1)
        self.ui.other_radioButton_lenght_2.toggled.connect(self.converter.lenght_selection_2)
        self.ui.other_list_1.itemClicked.connect(self.converter.item_for_copy)
        self.ui.other_copy_1.clicked.connect(self.converter.btn_copy_1)
        self.ui.other_copy_2.clicked.connect(self.converter.btn_copy_2)

    # async def on_converter_clicked(self):
    #     await self.converter.as_convert_pdf2img()
