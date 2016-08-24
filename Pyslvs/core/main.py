# -*- coding: utf-8 -*-
import csv
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
#UI Ports
from core.Ui_main import Ui_MainWindow
import webbrowser
#Dialog Ports
from .info.version import version_show
from .info.color import color_show
from .info.info import Info_show
from .info.help import Help_info_show
#Warning Dialog Ports
from .warning.reset_workbook import reset_show
from .warning.zero_value import zero_show
from .warning.repeated_value import same_show
#Drawing Dialog Ports
from .draw.draw_point import New_point
from .draw.draw_link import New_link
from .draw.draw_stay_chain import chain_show
from .draw.draw_delete_point import delete_point_show
from .draw.draw_delete_linkage import delete_linkage_show
#from .python_solve import Solve

Environment_variables = '../'

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?\nAny Changes won't be saved.",
            QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("Exit.")
            event.accept()
        else:
            event.ignore()
    
    @pyqtSlot()
    def on_actionMi_nimized_triggered(self):
        print("Minmized Windows.")
    
    @pyqtSlot()
    def on_actionM_axmized_triggered(self):
        print("Maxmized Windows.")
    
    @pyqtSlot()
    def on_action_Full_Screen_triggered(self):
        print("Full Screen.")
    
    @pyqtSlot()
    def on_actionNormalmized_triggered(self):
        print("Normal Screen.")
    
    @pyqtSlot()
    def on_actionHow_to_use_triggered(self):
        dlg_help = Help_info_show()
        dlg_help.show()
        if dlg_help.exec_():
            pass
    
    @pyqtSlot()
    def on_actionColor_Settings_triggered(self):
        dlg_color = color_show()
        dlg_color.show()
        if dlg_color.exec_():
            pass
    
    @pyqtSlot()
    def on_action_Get_Help_triggered(self):
        print("Open http://project.mde.tw/blog/slvs-library-functions.html")
        webbrowser.open("http://project.mde.tw/blog/slvs-library-functions.html")
    
    @pyqtSlot()
    def on_actionGit_hub_Site_triggered(self):
        print("Open https://github.com/40323230/python-solvespace")
        webbrowser.open("https://github.com/40323230/python-solvespace")
    
    @pyqtSlot()
    def on_actionGithub_Wiki_triggered(self):
        print("Open https://github.com/40323230/python-solvespace/wiki")
        webbrowser.open("https://github.com/40323230/python-solvespace/wiki")
    
    @pyqtSlot()
    def on_action_About_Pyslvs_triggered(self):
        dlg_version  = version_show()
        dlg_version.show()
        if dlg_version.exec_():
            pass
    
    @pyqtSlot()
    def on_action_About_Python_Solvspace_triggered(self):
        dlg_info  = Info_show()
        dlg_info.show()
        if dlg_info.exec_():
            pass
    
    @pyqtSlot()
    def on_action_New_Workbook_triggered(self):
        dlg  = reset_show()
        dlg.show()
        if dlg.exec_():
            table1 = self.Entiteis_Point
            table2 = self.Entiteis_Link
            table3 = self.Entiteis_Stay_Chain
            for i in reversed(range(1, table1.rowCount())):
                table1.removeRow(i)
            for i in reversed(range(table2.rowCount())):
                table2.removeRow(i)
            for i in reversed(range(table3.rowCount())):
                table3.removeRow(i)
            print("Reset workbook.")
    
    @pyqtSlot()
    def on_action_Load_Workbook_triggered(self):
        warning_reset  = reset_show()
        warning_reset.show()
        if warning_reset.exec_():
            table1 = self.Entiteis_Point
            table2 = self.Entiteis_Link
            table3 = self.Entiteis_Stay_Chain
            for i in reversed(range(1, table1.rowCount())):
                table1.removeRow(i)
            for i in reversed(range(table2.rowCount())):
                table2.removeRow(i)
            for i in reversed(range(table3.rowCount())):
                table3.removeRow(i)
            print("Reset workbook.")
            print("Loading workbook...")
            fileName, _ = QFileDialog.getOpenFileName(self, 'Open file...', Environment_variables, 'Python Script(*.py)')
            print("Get:"+str(fileName))
            #TODO: Load Workbook
    
    @pyqtSlot()
    def on_action_Output_to_Script_triggered(self):
        print("Saving to script...")
        fileName, sub = QFileDialog.getSaveFileName(self, 'Save file...', Environment_variables, 'Python Script(*.py)')
        if sub == "Python Script(*.py)":
            fileName += ".py"
        print("Saved to:"+str(fileName))
        # TODO: Output_to_Script
    
    @pyqtSlot()
    def on_action_Output_to_Picture_triggered(self):
        print("Saving to script...")
        fileName, sub = QFileDialog.getSaveFileName(self, 'Save file...', Environment_variables, 'PNG file(*.png)')
        if sub == "PNG file(*.png)":
            fileName += ".png"
        print("Saved to:"+str(fileName))
        # TODO: Output_to_Picture
    
    @pyqtSlot()
    def on_action_Output_Coordinate_to_Text_File_triggered(self):
        table = self.Entiteis_Point
        print("Saving to script...")
        fileName, sub = QFileDialog.getSaveFileName(self, 'Save file...', Environment_variables, 'Text File(*.txt);;CSV File(*.csv)')
        if fileName:
            fileName = fileName.replace(".txt", "")
            fileName = fileName.replace(".csv", "")
            if sub == "Text File(*.txt)":
                fileName += ".txt"
            if sub == "CSV File(*.csv)":
                fileName += ".csv"
            stream = open(fileName, 'w', newline="\n")
            writer = csv.writer(stream)
            csv.register_dialect(
                'mydialect',
                delimiter = ',',
                quotechar = '\"',
                doublequote = True,
                skipinitialspace = True,
                lineterminator = '\r\n',
                quoting = csv.QUOTE_MINIMAL)
            for row in range(table.rowCount()):
                rowdata = []
                for column in range(table.columnCount()):
                    print(row, column)
                    item = table.item(row, column)
                    if item is not None:
                        rowdata += [item.text()+'\t']
                    else:
                        rowdata += ['\n']
                writer.writerow(rowdata)
    
    @pyqtSlot()
    def on_action_New_Point_triggered(self):
        table1 = self.Entiteis_Point
        table2 = self.Entiteis_Point_Style
        draw_point  = New_point()
        draw_point.Point_num.insertPlainText("Point"+str(table1.rowCount()))
        draw_point.show()
        if draw_point.exec_():
            Points_list_add(table1, draw_point.Point_num.toPlainText(),
                draw_point.X_coordinate.text(), draw_point.Y_coordinate.text(),
                draw_point.Fix_Point.checkState())
            Points_style_add(table2, draw_point.Point_num.toPlainText(), "GREEN", "1", "GREEN")
    
    @pyqtSlot()
    def on_Point_add_button_clicked(self):
        table1 = self.Entiteis_Point
        table2 = self.Entiteis_Point_Style
        x = self.X_coordinate.text()
        y = self.Y_coordinate.text()
        Points_list_add(table1, "Point"+str(table1.rowCount()), x, y, False)
        Points_style_add(table2, "Point"+str(table2.rowCount()), "GREEN", "1", "GREEN")
    
    @pyqtSlot()
    def on_action_New_Line_triggered(self):
        table1 = self.Entiteis_Point
        if (table1.rowCount() <= 1):
            dlg = zero_show()
            dlg.show()
            if dlg.exec_():
                pass
        else:
            icon = QIcon()
            icon.addPixmap(QPixmap(":/icons/point.png"), QIcon.Normal, QIcon.Off)
            draw_link  = New_link()
            for i in range(table1.rowCount()):
                point_select = "Point"+str(i)
                draw_link.Start_Point.insertItem(i, icon, point_select)
                draw_link.End_Point.insertItem(i, icon, point_select)
            table2 = self.Entiteis_Link
            draw_link.Link_num.insertPlainText("Line"+str(table2.rowCount()))
            draw_link.show()
            if draw_link.exec_():
                a = draw_link.Start_Point.currentText()
                b = draw_link.End_Point.currentText()
                if a == b:
                    dlg = same_show()
                    dlg.show()
                    if dlg.exec_():
                        pass
                else:
                    start = draw_link.Start_Point.currentText()
                    end = draw_link.End_Point.currentText()
                    Links_list_add(table2, draw_link.Link_num.toPlainText(),
                        start, end,
                        draw_link.Length.text())
    
    @pyqtSlot()
    def on_action_New_Stay_Chain_triggered(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/point.png"), QIcon.Normal, QIcon.Off)
        table1 = self.Entiteis_Point
        if (table1.rowCount() <= 2):
            dlg = zero_show()
            dlg.show()
            if dlg.exec_():
                pass
        else:
            New_stay_chain = chain_show()
            table2 = self.Entiteis_Stay_Chain
            for i in range(table1.rowCount()):
                New_stay_chain.Point1.insertItem(i, icon, table1.item(i, 0).text())
                New_stay_chain.Point2.insertItem(i, icon, table1.item(i, 0).text())
                New_stay_chain.Point3.insertItem(i, icon, table1.item(i, 0).text())
            New_stay_chain.Chain_num.insertPlainText("Chain"+str(table2.rowCount()))
            New_stay_chain.show()
            if New_stay_chain.exec_():
                p1 = New_stay_chain.Point1.currentText()
                p2 = New_stay_chain.Point2.currentText()
                p3 = New_stay_chain.Point3.currentText()
                if (p1 == p2) | (p2 == p3) | (p1 == p3):
                    dlg = same_show()
                    dlg.show()
                    if dlg.exec_():
                        pass
                else:
                    Chain_list_add(table2, New_stay_chain.Chain_num.toPlainText(),
                        p1, p2, p3,
                        New_stay_chain.p1_p2.text(),
                        New_stay_chain.p2_p3.text(),
                        New_stay_chain.p1_p3.text())
    
    @pyqtSlot()
    def on_actionDelete_Point_triggered(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/point.png"), QIcon.Normal, QIcon.Off)
        table1 = self.Entiteis_Point
        table2 = self.Entiteis_Point_Style
        if table1.rowCount() <= 1:
            dlg = zero_show()
            dlg.show()
            if dlg.exec_():
                pass
        else:
            dlg = delete_point_show()
            for i in range(1, table1.rowCount()):
                dlg.Point.insertItem(i, icon, table1.item(i, 0).text())
            dlg.show()
            if dlg.exec_():
                Point_list_delete(table1, table2, dlg)
    
    @pyqtSlot()
    def on_actionDelete_Linkage_triggered(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/line.png"), QIcon.Normal, QIcon.Off)
        table = self.Entiteis_Link
        if table.rowCount() <= 0:
            dlg = zero_show()
            dlg.show()
            if dlg.exec_():
                pass
        else:
            dlg = delete_linkage_show()
            for i in range(table.rowCount()):
                dlg.Linkage.insertItem(i, icon, table.item(i, 0).text())
            dlg.show()
            if dlg.exec_():
                One_list_delete(table, "Line", dlg)

def Points_list_add(table, name, x, y, fixed):
    rowPosition = table.rowCount()
    table.insertRow(rowPosition)
    table.setItem(rowPosition , 0, QTableWidgetItem(name))
    table.setItem(rowPosition , 1, QTableWidgetItem(x))
    table.setItem(rowPosition , 2, QTableWidgetItem(y))
    checkbox = QTableWidgetItem("")
    checkbox.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    if fixed:
        checkbox.setCheckState(Qt.Checked)
    else:
        checkbox.setCheckState(Qt.Unchecked)
    table.setItem(rowPosition , 3, checkbox)
    print("Add Point"+str(rowPosition)+".")

def Links_list_add(table, name, start, end, l):
    rowPosition = table.rowCount()
    table.insertRow(rowPosition)
    table.setItem(rowPosition , 0, QTableWidgetItem(name))
    table.setItem(rowPosition , 1, QTableWidgetItem(start))
    table.setItem(rowPosition , 2, QTableWidgetItem(end))
    table.setItem(rowPosition , 3, QTableWidgetItem(l))
    print("Add a link, Line "+str(rowPosition)+".")

def Chain_list_add(table, name, p1, p2, p3, a, b, c):
    rowPosition = table.rowCount()
    table.insertRow(rowPosition)
    table.setItem(rowPosition , 0, QTableWidgetItem(name))
    table.setItem(rowPosition , 1, QTableWidgetItem(p1))
    table.setItem(rowPosition , 2, QTableWidgetItem(p2))
    table.setItem(rowPosition , 3, QTableWidgetItem(p3))
    table.setItem(rowPosition , 4, QTableWidgetItem(a))
    table.setItem(rowPosition , 5, QTableWidgetItem(b))
    table.setItem(rowPosition , 6, QTableWidgetItem(c))
    print("Add a Triangle Chain, Line "+str(rowPosition)+".")

def Points_style_add(table, name, color, ringsize, ringcolor):
    rowPosition = table.rowCount()
    table.insertRow(rowPosition)
    table.setItem(rowPosition , 0, QTableWidgetItem(name))
    table.setItem(rowPosition , 1, QTableWidgetItem(color))
    table.setItem(rowPosition , 2, QTableWidgetItem(ringsize))
    table.setItem(rowPosition , 3, QTableWidgetItem(ringcolor))
    print("Add Point Style for Point"+str(rowPosition)+".")

def Point_list_delete(table1, table2, dlg):
    for i in range(1, table1.rowCount()):
                    if (dlg.Point.currentText() == table1.item(i, 0).text()):
                        table1.removeRow(i)
                        table2.removeRow(i)
                        for y in range(i, table1.rowCount()):
                            table1.setItem(y , 0, QTableWidgetItem("Point"+str(y)))
                        break
                        for y in range(i, table2.rowCount()):
                            table2.setItem(y , 0, QTableWidgetItem("Point"+str(y)))
                        break

def One_list_delete(table, name, dlg):
    for i in range(table.rowCount()):
                    if (dlg.Linkage.currentText() == table.item(i, 0).text()):
                        table.removeRow(i)
                        for y in range(i, table.rowCount()):
                            table.setItem(y , 0, QTableWidgetItem(name+str(y)))
                        break
