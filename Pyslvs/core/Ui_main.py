# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs/core/main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 599)
        MainWindow.setMinimumSize(QtCore.QSize(777, 599))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 190, 101, 21))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.X_coordinate = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.X_coordinate.setGeometry(QtCore.QRect(60, 210, 81, 26))
        self.X_coordinate.setProperty("showGroupSeparator", False)
        self.X_coordinate.setMinimum(-10000.0)
        self.X_coordinate.setMaximum(10000.0)
        self.X_coordinate.setObjectName("X_coordinate")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(160, 190, 91, 21))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.Point_add_button = QtWidgets.QPushButton(self.centralWidget)
        self.Point_add_button.setGeometry(QtCore.QRect(250, 210, 85, 25))
        self.Point_add_button.setObjectName("Point_add_button")
        self.Entiteis_Point = QtWidgets.QTableWidget(self.centralWidget)
        self.Entiteis_Point.setGeometry(QtCore.QRect(10, 10, 331, 171))
        self.Entiteis_Point.setMinimumSize(QtCore.QSize(331, 0))
        self.Entiteis_Point.setToolTipDuration(-1)
        self.Entiteis_Point.setAutoFillBackground(True)
        self.Entiteis_Point.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Entiteis_Point.setRowCount(1)
        self.Entiteis_Point.setColumnCount(4)
        self.Entiteis_Point.setObjectName("Entiteis_Point")
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/point.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.Entiteis_Point.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.Entiteis_Point.setItem(0, 3, item)
        self.Entiteis_Point.horizontalHeader().setDefaultSectionSize(65)
        self.Entiteis_Point.horizontalHeader().setMinimumSectionSize(50)
        self.Y_coordinate = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.Y_coordinate.setGeometry(QtCore.QRect(160, 210, 81, 26))
        self.Y_coordinate.setProperty("showGroupSeparator", False)
        self.Y_coordinate.setMinimum(-10000.0)
        self.Y_coordinate.setMaximum(10000.0)
        self.Y_coordinate.setObjectName("Y_coordinate")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 51, 41))
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/point.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 240, 331, 311))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Entites = QtWidgets.QWidget()
        self.Entites.setObjectName("Entites")
        self.Entiteis_Link = QtWidgets.QTableWidget(self.Entites)
        self.Entiteis_Link.setGeometry(QtCore.QRect(10, 10, 301, 141))
        self.Entiteis_Link.setAcceptDrops(False)
        self.Entiteis_Link.setAutoFillBackground(True)
        self.Entiteis_Link.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Entiteis_Link.setRowCount(0)
        self.Entiteis_Link.setColumnCount(4)
        self.Entiteis_Link.setObjectName("Entiteis_Link")
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.Entiteis_Link.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Link.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Link.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Link.setHorizontalHeaderItem(3, item)
        self.Entiteis_Link.horizontalHeader().setDefaultSectionSize(70)
        self.Entiteis_Link.horizontalHeader().setMinimumSectionSize(50)
        self.Entiteis_Stay_Chain = QtWidgets.QTableWidget(self.Entites)
        self.Entiteis_Stay_Chain.setGeometry(QtCore.QRect(10, 160, 301, 111))
        self.Entiteis_Stay_Chain.setAutoFillBackground(True)
        self.Entiteis_Stay_Chain.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Entiteis_Stay_Chain.setRowCount(0)
        self.Entiteis_Stay_Chain.setColumnCount(7)
        self.Entiteis_Stay_Chain.setObjectName("Entiteis_Stay_Chain")
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/equal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.Entiteis_Stay_Chain.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Stay_Chain.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Stay_Chain.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Stay_Chain.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Stay_Chain.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Stay_Chain.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Stay_Chain.setHorizontalHeaderItem(6, item)
        self.Entiteis_Stay_Chain.horizontalHeader().setDefaultSectionSize(65)
        self.Entiteis_Stay_Chain.horizontalHeader().setMinimumSectionSize(65)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/trim.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Entites, icon4, "")
        self.Simulate = QtWidgets.QWidget()
        self.Simulate.setObjectName("Simulate")
        self.tableWidget = QtWidgets.QTableWidget(self.Simulate)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 301, 111))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(70)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/arc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Simulate, icon6, "")
        self.Style = QtWidgets.QWidget()
        self.Style.setObjectName("Style")
        self.Entiteis_Point_Style = QtWidgets.QTableWidget(self.Style)
        self.Entiteis_Point_Style.setGeometry(QtCore.QRect(10, 10, 301, 151))
        self.Entiteis_Point_Style.setColumnCount(4)
        self.Entiteis_Point_Style.setObjectName("Entiteis_Point_Style")
        self.Entiteis_Point_Style.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point_Style.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon1)
        self.Entiteis_Point_Style.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point_Style.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point_Style.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point_Style.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.Entiteis_Point_Style.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point_Style.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point_Style.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Entiteis_Point_Style.setItem(0, 3, item)
        self.Entiteis_Point_Style.horizontalHeader().setDefaultSectionSize(65)
        self.Entiteis_Point_Style.horizontalHeader().setMinimumSectionSize(50)
        self.label_4 = QtWidgets.QLabel(self.Style)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 301, 31))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.Color_set = QtWidgets.QPushButton(self.Style)
        self.Color_set.setGeometry(QtCore.QRect(10, 200, 141, 41))
        self.Color_set.setObjectName("Color_set")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/char-3-radio-true.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Style, icon7, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 777, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setStatusTip("")
        self.menuFile.setObjectName("menuFile")
        self.menu_Draw = QtWidgets.QMenu(self.menuBar)
        self.menu_Draw.setObjectName("menu_Draw")
        self.menu_Options = QtWidgets.QMenu(self.menuBar)
        self.menu_Options.setObjectName("menu_Options")
        self.menu_Help = QtWidgets.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Simulation = QtWidgets.QMenu(self.menuBar)
        self.menu_Simulation.setObjectName("menu_Simulation")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_New_Workbook = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/step-rotate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_New_Workbook.setIcon(icon8)
        self.action_New_Workbook.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_New_Workbook.setObjectName("action_New_Workbook")
        self.action_Load_Workbook = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/step-translate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Load_Workbook.setIcon(icon9)
        self.action_Load_Workbook.setObjectName("action_Load_Workbook")
        self.action_New_Point = QtWidgets.QAction(MainWindow)
        self.action_New_Point.setIcon(icon1)
        self.action_New_Point.setObjectName("action_New_Point")
        self.action_New_Line = QtWidgets.QAction(MainWindow)
        self.action_New_Line.setIcon(icon2)
        self.action_New_Line.setObjectName("action_New_Line")
        self.action_Output_to_Script = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/edges.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Output_to_Script.setIcon(icon10)
        self.action_Output_to_Script.setObjectName("action_Output_to_Script")
        self.actionE_xit = QtWidgets.QAction(MainWindow)
        self.actionE_xit.setCheckable(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionE_xit.setIcon(icon11)
        self.actionE_xit.setObjectName("actionE_xit")
        self.action_Get_Help = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/kmol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Get_Help.setIcon(icon12)
        self.action_Get_Help.setObjectName("action_Get_Help")
        self.action_Prefenece = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/shaded.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Prefenece.setIcon(icon13)
        self.action_Prefenece.setObjectName("action_Prefenece")
        self.actionGit_hub_Site = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/github-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGit_hub_Site.setIcon(icon14)
        self.actionGit_hub_Site.setObjectName("actionGit_hub_Site")
        self.action_About_Pyslvs = QtWidgets.QAction(MainWindow)
        self.action_About_Pyslvs.setIcon(icon)
        self.action_About_Pyslvs.setObjectName("action_About_Pyslvs")
        self.action_Set_Drive_Shaft = QtWidgets.QAction(MainWindow)
        self.action_Set_Drive_Shaft.setIcon(icon5)
        self.action_Set_Drive_Shaft.setObjectName("action_Set_Drive_Shaft")
        self.actionGithub_Wiki = QtWidgets.QAction(MainWindow)
        self.actionGithub_Wiki.setIcon(icon14)
        self.actionGithub_Wiki.setObjectName("actionGithub_Wiki")
        self.action_Highlight_Drive_Shaft_Point = QtWidgets.QAction(MainWindow)
        self.action_Highlight_Drive_Shaft_Point.setCheckable(True)
        self.action_Highlight_Drive_Shaft_Point.setChecked(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/char-1-check-true.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon15.addPixmap(QtGui.QPixmap(":/icons/char-0-check-false.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Highlight_Drive_Shaft_Point.setIcon(icon15)
        self.action_Highlight_Drive_Shaft_Point.setObjectName("action_Highlight_Drive_Shaft_Point")
        self.actionMi_nimized = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/minmized.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMi_nimized.setIcon(icon16)
        self.actionMi_nimized.setObjectName("actionMi_nimized")
        self.actionM_axmized = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/maxmized.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionM_axmized.setIcon(icon17)
        self.actionM_axmized.setObjectName("actionM_axmized")
        self.action_Full_Screen = QtWidgets.QAction(MainWindow)
        self.action_Full_Screen.setCheckable(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Full_Screen.setIcon(icon18)
        self.action_Full_Screen.setObjectName("action_Full_Screen")
        self.actionNormalmized = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/normalsized.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNormalmized.setIcon(icon19)
        self.actionNormalmized.setObjectName("actionNormalmized")
        self.action_Output_to_Picture = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/faces.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Output_to_Picture.setIcon(icon20)
        self.action_Output_to_Picture.setObjectName("action_Output_to_Picture")
        self.action_Output_Coordinate_to_Text_File = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/hidden-lines.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Output_Coordinate_to_Text_File.setIcon(icon21)
        self.action_Output_Coordinate_to_Text_File.setObjectName("action_Output_Coordinate_to_Text_File")
        self.action_Angle_Simulation = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/angle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Angle_Simulation.setIcon(icon22)
        self.action_Angle_Simulation.setObjectName("action_Angle_Simulation")
        self.actionSimulation_Options = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/other-supp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSimulation_Options.setIcon(icon23)
        self.actionSimulation_Options.setObjectName("actionSimulation_Options")
        self.action_See_Error_Logs = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icons/ref.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_See_Error_Logs.setIcon(icon24)
        self.action_See_Error_Logs.setObjectName("action_See_Error_Logs")
        self.action_Triangle = QtWidgets.QAction(MainWindow)
        self.action_Triangle.setObjectName("action_Triangle")
        self.action_Quadrilateral = QtWidgets.QAction(MainWindow)
        self.action_Quadrilateral.setObjectName("action_Quadrilateral")
        self.action_Pentagon = QtWidgets.QAction(MainWindow)
        self.action_Pentagon.setObjectName("action_Pentagon")
        self.action_Hexagon = QtWidgets.QAction(MainWindow)
        self.action_Hexagon.setObjectName("action_Hexagon")
        self.actionH_eptagon = QtWidgets.QAction(MainWindow)
        self.actionH_eptagon.setObjectName("actionH_eptagon")
        self.action_Octagon = QtWidgets.QAction(MainWindow)
        self.action_Octagon.setObjectName("action_Octagon")
        self.action_Custom = QtWidgets.QAction(MainWindow)
        self.action_Custom.setObjectName("action_Custom")
        self.action_New_Stay_Chain = QtWidgets.QAction(MainWindow)
        self.action_New_Stay_Chain.setIcon(icon3)
        self.action_New_Stay_Chain.setObjectName("action_New_Stay_Chain")
        self.action_Appearance = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/icons/mesh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Appearance.setIcon(icon25)
        self.action_Appearance.setObjectName("action_Appearance")
        self.action_See_Python_Scripts = QtWidgets.QAction(MainWindow)
        self.action_See_Python_Scripts.setIcon(icon10)
        self.action_See_Python_Scripts.setObjectName("action_See_Python_Scripts")
        self.action_About_Python_Solvspace = QtWidgets.QAction(MainWindow)
        self.action_About_Python_Solvspace.setIcon(icon)
        self.action_About_Python_Solvspace.setObjectName("action_About_Python_Solvspace")
        self.actionDelete_Point = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Point.setIcon(icon26)
        self.actionDelete_Point.setObjectName("actionDelete_Point")
        self.actionDelete_Linkage = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/icons/deleteline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Linkage.setIcon(icon27)
        self.actionDelete_Linkage.setObjectName("actionDelete_Linkage")
        self.actionDelete_Stay_Chain = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/icons/deletechain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Stay_Chain.setIcon(icon28)
        self.actionDelete_Stay_Chain.setObjectName("actionDelete_Stay_Chain")
        self.actionEdit_Point = QtWidgets.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/icons/editpoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Point.setIcon(icon29)
        self.actionEdit_Point.setObjectName("actionEdit_Point")
        self.actionEdit_Linkage = QtWidgets.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/icons/length.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Linkage.setIcon(icon30)
        self.actionEdit_Linkage.setObjectName("actionEdit_Linkage")
        self.actionEdit_Stay_Chain = QtWidgets.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/icons/editchain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Stay_Chain.setIcon(icon31)
        self.actionEdit_Stay_Chain.setObjectName("actionEdit_Stay_Chain")
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/icons/assemble.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHow_to_use.setIcon(icon32)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionSet_Slider = QtWidgets.QAction(MainWindow)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/icons/pointonx.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSet_Slider.setIcon(icon33)
        self.actionSet_Slider.setObjectName("actionSet_Slider")
        self.actionColor_Settings = QtWidgets.QAction(MainWindow)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/icons/in3d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColor_Settings.setIcon(icon34)
        self.actionColor_Settings.setObjectName("actionColor_Settings")
        self.menuFile.addAction(self.action_New_Workbook)
        self.menuFile.addAction(self.action_Load_Workbook)
        self.menuFile.addAction(self.action_Output_to_Picture)
        self.menuFile.addAction(self.action_Output_to_Script)
        self.menuFile.addAction(self.action_Output_Coordinate_to_Text_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMi_nimized)
        self.menuFile.addAction(self.actionM_axmized)
        self.menuFile.addAction(self.actionNormalmized)
        self.menuFile.addAction(self.action_Full_Screen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionE_xit)
        self.menu_Draw.addAction(self.action_New_Point)
        self.menu_Draw.addAction(self.action_New_Line)
        self.menu_Draw.addAction(self.action_New_Stay_Chain)
        self.menu_Draw.addSeparator()
        self.menu_Draw.addAction(self.actionEdit_Point)
        self.menu_Draw.addAction(self.actionEdit_Linkage)
        self.menu_Draw.addAction(self.actionEdit_Stay_Chain)
        self.menu_Draw.addSeparator()
        self.menu_Draw.addAction(self.actionDelete_Point)
        self.menu_Draw.addAction(self.actionDelete_Linkage)
        self.menu_Draw.addAction(self.actionDelete_Stay_Chain)
        self.menu_Draw.addSeparator()
        self.menu_Draw.addAction(self.action_Set_Drive_Shaft)
        self.menu_Draw.addAction(self.actionSet_Slider)
        self.menu_Options.addAction(self.action_Highlight_Drive_Shaft_Point)
        self.menu_Options.addAction(self.action_See_Python_Scripts)
        self.menu_Options.addSeparator()
        self.menu_Options.addAction(self.action_Appearance)
        self.menu_Options.addAction(self.action_Prefenece)
        self.menu_Help.addAction(self.actionHow_to_use)
        self.menu_Help.addAction(self.actionColor_Settings)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_Get_Help)
        self.menu_Help.addAction(self.actionGit_hub_Site)
        self.menu_Help.addAction(self.actionGithub_Wiki)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_About_Pyslvs)
        self.menu_Help.addAction(self.action_About_Python_Solvspace)
        self.menu_Simulation.addAction(self.action_Angle_Simulation)
        self.menu_Simulation.addAction(self.action_See_Error_Logs)
        self.menu_Simulation.addSeparator()
        self.menu_Simulation.addAction(self.actionSimulation_Options)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menu_Draw.menuAction())
        self.menuBar.addAction(self.menu_Simulation.menuAction())
        self.menuBar.addAction(self.menu_Options.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.actionM_axmized.triggered.connect(MainWindow.showMaximized)
        self.actionMi_nimized.triggered.connect(MainWindow.showMinimized)
        self.action_Full_Screen.triggered.connect(MainWindow.showFullScreen)
        self.actionNormalmized.triggered.connect(MainWindow.showNormal)
        self.actionE_xit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Entiteis_Point, self.Entiteis_Link)
        MainWindow.setTabOrder(self.Entiteis_Link, self.Entiteis_Stay_Chain)
        MainWindow.setTabOrder(self.Entiteis_Stay_Chain, self.X_coordinate)
        MainWindow.setTabOrder(self.X_coordinate, self.Y_coordinate)
        MainWindow.setTabOrder(self.Y_coordinate, self.Point_add_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyslvs"))
        self.label.setText(_translate("MainWindow", "x coordinate"))
        self.X_coordinate.setStatusTip(_translate("MainWindow", "X coordinate of Next Point."))
        self.label_2.setText(_translate("MainWindow", "y coordinate"))
        self.Point_add_button.setStatusTip(_translate("MainWindow", "Quick insert a joint point."))
        self.Point_add_button.setText(_translate("MainWindow", "Add a Point"))
        self.Entiteis_Point.setStatusTip(_translate("MainWindow", "All Points in this workbook."))
        item = self.Entiteis_Point.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Origin"))
        item = self.Entiteis_Point.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.Entiteis_Point.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "X"))
        item = self.Entiteis_Point.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Y"))
        item = self.Entiteis_Point.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fixed"))
        __sortingEnabled = self.Entiteis_Point.isSortingEnabled()
        self.Entiteis_Point.setSortingEnabled(False)
        item = self.Entiteis_Point.item(0, 0)
        item.setText(_translate("MainWindow", "Point0"))
        item = self.Entiteis_Point.item(0, 1)
        item.setText(_translate("MainWindow", "0.00"))
        item = self.Entiteis_Point.item(0, 2)
        item.setText(_translate("MainWindow", "0.00"))
        self.Entiteis_Point.setSortingEnabled(__sortingEnabled)
        self.Y_coordinate.setStatusTip(_translate("MainWindow", "X coordinate of Next Point."))
        self.Entiteis_Link.setStatusTip(_translate("MainWindow", "All Links in this workbook."))
        item = self.Entiteis_Link.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.Entiteis_Link.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Start Side"))
        item = self.Entiteis_Link.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "End Side"))
        item = self.Entiteis_Link.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Length"))
        self.Entiteis_Stay_Chain.setStatusTip(_translate("MainWindow", "All Stay Chains in this workbook."))
        item = self.Entiteis_Stay_Chain.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.Entiteis_Stay_Chain.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Point[1]"))
        item = self.Entiteis_Stay_Chain.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Point[2]"))
        item = self.Entiteis_Stay_Chain.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Point[3]"))
        item = self.Entiteis_Stay_Chain.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "[1]-[2]"))
        item = self.Entiteis_Stay_Chain.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "[2]-[3]"))
        item = self.Entiteis_Stay_Chain.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "[1]-[3]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Entites), _translate("MainWindow", "Entites"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Shaft Center"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "References"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Simulate), _translate("MainWindow", "Simulate"))
        item = self.Entiteis_Point_Style.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Origin"))
        item = self.Entiteis_Point_Style.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.Entiteis_Point_Style.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Color"))
        item = self.Entiteis_Point_Style.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ring Size"))
        item = self.Entiteis_Point_Style.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ring Color"))
        __sortingEnabled = self.Entiteis_Point_Style.isSortingEnabled()
        self.Entiteis_Point_Style.setSortingEnabled(False)
        item = self.Entiteis_Point_Style.item(0, 0)
        item.setText(_translate("MainWindow", "Point0"))
        item = self.Entiteis_Point_Style.item(0, 1)
        item.setText(_translate("MainWindow", "RED"))
        item = self.Entiteis_Point_Style.item(0, 2)
        item.setText(_translate("MainWindow", "3"))
        item = self.Entiteis_Point_Style.item(0, 3)
        item.setText(_translate("MainWindow", "RED"))
        self.Entiteis_Point_Style.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Double-click to edit the form.</span></p></body></html>"))
        self.Color_set.setText(_translate("MainWindow", "Color Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Style), _translate("MainWindow", "Point Style"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menu_Draw.setTitle(_translate("MainWindow", "&Draw"))
        self.menu_Options.setTitle(_translate("MainWindow", "&Options"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menu_Simulation.setTitle(_translate("MainWindow", "&Simulation"))
        self.action_New_Workbook.setText(_translate("MainWindow", "&New Workbook"))
        self.action_New_Workbook.setStatusTip(_translate("MainWindow", "Reset to a new wrokbook."))
        self.action_New_Workbook.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Load_Workbook.setText(_translate("MainWindow", "&Load Workbook (*.py)"))
        self.action_Load_Workbook.setStatusTip(_translate("MainWindow", "Load workbook by exist file."))
        self.action_Load_Workbook.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_New_Point.setText(_translate("MainWindow", "New Joint &Point"))
        self.action_New_Point.setStatusTip(_translate("MainWindow", "Add a new point representative of a node on a machine."))
        self.action_New_Line.setText(_translate("MainWindow", "New &Linkage"))
        self.action_New_Line.setStatusTip(_translate("MainWindow", "Add  a link between two points."))
        self.action_Output_to_Script.setText(_translate("MainWindow", "Output to &Script"))
        self.action_Output_to_Script.setStatusTip(_translate("MainWindow", "Output to a Python 3 slvs module script."))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit"))
        self.actionE_xit.setStatusTip(_translate("MainWindow", "Exit Pyslvs."))
        self.action_Get_Help.setText(_translate("MainWindow", "&Get Help on Kmolab"))
        self.action_Get_Help.setStatusTip(_translate("MainWindow", "Goto Kmolab learn about more."))
        self.action_Prefenece.setText(_translate("MainWindow", "&Preferences..."))
        self.action_Prefenece.setStatusTip(_translate("MainWindow", "Some options in this program."))
        self.actionGit_hub_Site.setText(_translate("MainWindow", "Git&hub Site"))
        self.actionGit_hub_Site.setStatusTip(_translate("MainWindow", "Goto Github storage of Pyslvs."))
        self.action_About_Pyslvs.setText(_translate("MainWindow", "About &Pyslvs"))
        self.action_About_Pyslvs.setStatusTip(_translate("MainWindow", "Version and introduction of Pyslvs."))
        self.action_Set_Drive_Shaft.setText(_translate("MainWindow", "Set &Drive Shaft"))
        self.action_Set_Drive_Shaft.setStatusTip(_translate("MainWindow", "Set a point as a Drive Shaft"))
        self.actionGithub_Wiki.setText(_translate("MainWindow", "Github &Wiki"))
        self.actionGithub_Wiki.setStatusTip(_translate("MainWindow", "See our Wiki on Github."))
        self.action_Highlight_Drive_Shaft_Point.setText(_translate("MainWindow", "High&light Drive Shaft Point"))
        self.action_Highlight_Drive_Shaft_Point.setStatusTip(_translate("MainWindow", "Highlight Drive Shaft Point."))
        self.actionMi_nimized.setText(_translate("MainWindow", "M&inimized"))
        self.actionMi_nimized.setStatusTip(_translate("MainWindow", "Minimized the window."))
        self.actionM_axmized.setText(_translate("MainWindow", "M&axmized"))
        self.actionM_axmized.setStatusTip(_translate("MainWindow", "Maxmized the window."))
        self.action_Full_Screen.setText(_translate("MainWindow", "&Full Screen"))
        self.action_Full_Screen.setStatusTip(_translate("MainWindow", "Let the window truns to full screen."))
        self.actionNormalmized.setText(_translate("MainWindow", "&Normal"))
        self.actionNormalmized.setStatusTip(_translate("MainWindow", "Let the window back to normal."))
        self.action_Output_to_Picture.setText(_translate("MainWindow", "Output to &Picture"))
        self.action_Output_Coordinate_to_Text_File.setText(_translate("MainWindow", "Output Coordinate to &Text File"))
        self.action_Angle_Simulation.setText(_translate("MainWindow", "Start &Angle Simulation"))
        self.action_Angle_Simulation.setStatusTip(_translate("MainWindow", "Start a simulation by your settings."))
        self.actionSimulation_Options.setText(_translate("MainWindow", "Simulation &Options..."))
        self.actionSimulation_Options.setStatusTip(_translate("MainWindow", "Simulation options."))
        self.action_See_Error_Logs.setText(_translate("MainWindow", "See Error &Logs"))
        self.action_See_Error_Logs.setStatusTip(_translate("MainWindow", "See error logs in dialog box."))
        self.action_Triangle.setText(_translate("MainWindow", "&Triangle (3)"))
        self.action_Quadrilateral.setText(_translate("MainWindow", "&Quadrilateral (4)"))
        self.action_Pentagon.setText(_translate("MainWindow", "&Pentagon (5)"))
        self.action_Hexagon.setText(_translate("MainWindow", "&Hexagon (6)"))
        self.actionH_eptagon.setText(_translate("MainWindow", "H&eptagon (7)"))
        self.action_Octagon.setText(_translate("MainWindow", "&Octagon (8)"))
        self.action_Custom.setText(_translate("MainWindow", "&Custom..."))
        self.action_New_Stay_Chain.setText(_translate("MainWindow", "New Stay &Chain"))
        self.action_New_Stay_Chain.setStatusTip(_translate("MainWindow", "Add a stay chain by exist points."))
        self.action_Appearance.setText(_translate("MainWindow", "&Appearance..."))
        self.action_Appearance.setStatusTip(_translate("MainWindow", "Change appearance for all Points."))
        self.action_See_Python_Scripts.setText(_translate("MainWindow", "See &Python Scripts"))
        self.action_See_Python_Scripts.setStatusTip(_translate("MainWindow", "See Python scripts in this status."))
        self.action_About_Python_Solvspace.setText(_translate("MainWindow", "About Python &Solvspace"))
        self.actionDelete_Point.setText(_translate("MainWindow", "Delet Point"))
        self.actionDelete_Linkage.setText(_translate("MainWindow", "Delet Linkage"))
        self.actionDelete_Stay_Chain.setText(_translate("MainWindow", "Delete Stay Chain"))
        self.actionEdit_Point.setText(_translate("MainWindow", "Edit Point"))
        self.actionEdit_Linkage.setText(_translate("MainWindow", "Edit Linkage"))
        self.actionEdit_Stay_Chain.setText(_translate("MainWindow", "Edit Stay Chain"))
        self.actionHow_to_use.setText(_translate("MainWindow", "&How to use?"))
        self.actionSet_Slider.setText(_translate("MainWindow", "Set &Slider"))
        self.actionColor_Settings.setText(_translate("MainWindow", "&Color Settings"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

