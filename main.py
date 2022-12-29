import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import plot


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Connect to the database
        self.conn = sqlite3.connect('Financials.db')
        self.cursor = self.conn.cursor()

        # Create the main widget and set it as the central widget
        self.main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.main_widget)

        # Create a layout for the main widget
        self.layout = QtWidgets.QVBoxLayout(self.main_widget)

        # Create a combobox to select the table
        self.table_combobox = QtWidgets.QComboBox()
        self.table_combobox.addItems(
            ['Company Allocation', 'Income Statement', 'Balance Sheet', 'P&L', 'Cost of Goods Sold',
             'Government Policies'])
        self.table_combobox.currentIndexChanged.connect(self.refresh_data)
        self.layout.addWidget(self.table_combobox)

        # Create a table view and model for the data
        self.table_view = QtWidgets.QTableView()
        self.table_model = QtGui.QStandardItemModel(self.table_view)
        self.table_view.setModel(self.table_model)
        self.layout.addWidget(self.table_view)

        # Load the data into the table model
        self.refresh_data()

    def refresh_data(self):
        # Get the selected table name from the combobox
        table_name = self.table_combobox.currentText()

        # Clear the table model
        self.table_model.clear()

        # Set the column headers based on the selected table
        if table_name == 'Company Allocation':
            self.table_model.setHorizontalHeaderLabels(['ID', 'Country', 'Industry', 'Product'])
            self.cursor.execute('''SELECT * FROM Company_Allocation''')
        elif table_name == 'Income Statement':
            self.table_model.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Revenue', 'Cost of Goods Sold', 'Gross Profit', 'Selling and Administrative Expenses',
                 'Operating Income', 'Other Income/Expense', 'Net Income'])
            self.cursor.execute('''SELECT * FROM income_statement''')
        elif table_name == 'Balance Sheet':
            self.table_model.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Cash and Cash Equivalents', 'Accounts Receivable', 'Inventories', 'Investments',
                 'Property, Plant and Equipment', 'Intangible Assets', 'Accounts Payable', 'Notes Payable',
                 'Accrued Expenses', 'Common Stock', 'Retained Earnings', 'Total Assets',
                 'Total Liabilities and Equity'])
            self.cursor.execute('''SELECT * FROM balance_sheet''')
        elif table_name == 'P&L':
            self.table_model.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Revenue', 'Cost of Goods Sold', 'Gross Profit', 'Selling and Administrative Expenses',
                 'Operating Income', 'Other Income/Expense', 'Net Income'])
            self.cursor.execute('''SELECT * FROM pnl''')
        elif table_name == 'Cost of Goods Sold':
            self.table_model.setHorizontalHeaderLabels(
                ['ID', 'Date', 'Product Name', 'Quantity', 'Unit Cost', 'Total Cost'])
            self.cursor.execute('''SELECT * FROM cost_of_goods_sold''')
        elif table_name == 'Government Policies':
            self.table_model.setHorizontalHeaderLabels(
                ['Macro', 'Tax Rate', 'Interest Rates', 'Risk Free Rate', 'Date'])
            self.cursor.execute('''SELECT * FROM Goverment_Policies''')
            # Iterate over the rows of data and add them to the table model
        for row in self.cursor:
            items = [QtGui.QStandardItem(str(cell)) for cell in row]
            self.table_model.appendRow(items)
            # Create the plot

            # Create a subplot containing both the table view and the plot


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()