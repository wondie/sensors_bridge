# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensorsbridge.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SensorsBridge(object):
    def setupUi(self, SensorsBridge):
        SensorsBridge.setObjectName("SensorsBridge")
        SensorsBridge.resize(878, 557)
        self.verticalLayout = QtWidgets.QVBoxLayout(SensorsBridge)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(SensorsBridge)
        self.toolBox.setObjectName("toolBox")
        self.options_tbx = QtWidgets.QWidget()
        self.options_tbx.setGeometry(QtCore.QRect(0, 0, 860, 421))
        self.options_tbx.setObjectName("options_tbx")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.options_tbx)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.options_tbx)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.data_folder_lne = QtWidgets.QLineEdit(self.groupBox)
        self.data_folder_lne.setObjectName("data_folder_lne")
        self.gridLayout_2.addWidget(self.data_folder_lne, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.data_folder_btn = QtWidgets.QPushButton(self.groupBox)
        self.data_folder_btn.setObjectName("data_folder_btn")
        self.gridLayout_4.addWidget(self.data_folder_btn, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 2, 1, 1)
        self.udp_port_sb = QtWidgets.QSpinBox(self.groupBox)
        self.udp_port_sb.setMaximum(1000000)
        self.udp_port_sb.setProperty("value", 50000)
        self.udp_port_sb.setObjectName("udp_port_sb")
        self.gridLayout_4.addWidget(self.udp_port_sb, 3, 1, 1, 2)
        self.file_keep_limit_sb = QtWidgets.QSpinBox(self.groupBox)
        self.file_keep_limit_sb.setProperty("value", 3)
        self.file_keep_limit_sb.setObjectName("file_keep_limit_sb")
        self.gridLayout_4.addWidget(self.file_keep_limit_sb, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.server_gb = QtWidgets.QGroupBox(self.options_tbx)
        self.server_gb.setCheckable(True)
        self.server_gb.setObjectName("server_gb")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.server_gb)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.server_le = QtWidgets.QLineEdit(self.server_gb)
        self.server_le.setObjectName("server_le")
        self.gridLayout_3.addWidget(self.server_le, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.server_gb)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.server_login_le = QtWidgets.QLineEdit(self.server_gb)
        self.server_login_le.setObjectName("server_login_le")
        self.gridLayout_3.addWidget(self.server_login_le, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.server_gb)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.username_le = QtWidgets.QLineEdit(self.server_gb)
        self.username_le.setObjectName("username_le")
        self.gridLayout_3.addWidget(self.username_le, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.server_gb)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.password_le = QtWidgets.QLineEdit(self.server_gb)
        self.password_le.setObjectName("password_le")
        self.gridLayout_3.addWidget(self.password_le, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.server_gb)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.server_gb)
        self.toolBox.addItem(self.options_tbx, "")
        self.sensors_config_tbx = QtWidgets.QWidget()
        self.sensors_config_tbx.setGeometry(QtCore.QRect(0, 0, 860, 421))
        self.sensors_config_tbx.setObjectName("sensors_config_tbx")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sensors_config_tbx)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QToolButton(self.sensors_config_tbx)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.remove_btn = QtWidgets.QToolButton(self.sensors_config_tbx)
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout.addWidget(self.remove_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.sensors_config_tw = QtWidgets.QTableWidget(self.sensors_config_tbx)
        self.sensors_config_tw.setDragEnabled(False)
        self.sensors_config_tw.setAlternatingRowColors(True)
        self.sensors_config_tw.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.sensors_config_tw.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sensors_config_tw.setShowGrid(True)
        self.sensors_config_tw.setGridStyle(QtCore.Qt.SolidLine)
        self.sensors_config_tw.setWordWrap(True)
        self.sensors_config_tw.setObjectName("sensors_config_tw")
        self.sensors_config_tw.setColumnCount(5)
        self.sensors_config_tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sensors_config_tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sensors_config_tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sensors_config_tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sensors_config_tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sensors_config_tw.setHorizontalHeaderItem(4, item)
        self.sensors_config_tw.horizontalHeader().setVisible(False)
        self.sensors_config_tw.horizontalHeader().setCascadingSectionResizes(True)
        self.sensors_config_tw.horizontalHeader().setSortIndicatorShown(False)
        self.sensors_config_tw.horizontalHeader().setStretchLastSection(False)
        self.sensors_config_tw.verticalHeader().setVisible(False)
        self.sensors_config_tw.verticalHeader().setCascadingSectionResizes(False)
        self.sensors_config_tw.verticalHeader().setHighlightSections(True)
        self.sensors_config_tw.verticalHeader().setSortIndicatorShown(False)
        self.sensors_config_tw.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.sensors_config_tw)
        self.toolBox.addItem(self.sensors_config_tbx, "")
        self.log_tbx = QtWidgets.QWidget()
        self.log_tbx.setGeometry(QtCore.QRect(0, 0, 860, 421))
        self.log_tbx.setObjectName("log_tbx")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.log_tbx)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.log_tab = QtWidgets.QTabWidget(self.log_tbx)
        self.log_tab.setObjectName("log_tab")
        self.verticalLayout_4.addWidget(self.log_tab)
        self.toolBox.addItem(self.log_tbx, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SensorsBridge)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SensorsBridge)
        self.toolBox.setCurrentIndex(0)
        self.buttonBox.accepted.connect(SensorsBridge.accept)
        self.buttonBox.rejected.connect(SensorsBridge.reject)
        QtCore.QMetaObject.connectSlotsByName(SensorsBridge)

    def retranslateUi(self, SensorsBridge):
        _translate = QtCore.QCoreApplication.translate
        SensorsBridge.setWindowTitle(_translate("SensorsBridge", "Mississippi State University Water Quality Sensors Bridge"))
        self.groupBox.setTitle(_translate("SensorsBridge", "Basic Options"))
        self.label.setText(_translate("SensorsBridge", "Output data folder"))
        self.data_folder_btn.setText(_translate("SensorsBridge", "Browse"))
        self.label_4.setText(_translate("SensorsBridge", "days"))
        self.label_2.setText(_translate("SensorsBridge", "Remove files older than"))
        self.label_3.setText(_translate("SensorsBridge", "UDP Port"))
        self.server_gb.setTitle(_translate("SensorsBridge", "Server Options"))
        self.label_6.setText(_translate("SensorsBridge", "Server login URL"))
        self.label_7.setText(_translate("SensorsBridge", "Username"))
        self.label_8.setText(_translate("SensorsBridge", "Password"))
        self.label_5.setText(_translate("SensorsBridge", "Server URL"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.options_tbx), _translate("SensorsBridge", "Options"))
        self.add_btn.setText(_translate("SensorsBridge", "+ Add"))
        self.remove_btn.setText(_translate("SensorsBridge", "- Remove"))
        self.sensors_config_tw.setSortingEnabled(False)
        item = self.sensors_config_tw.horizontalHeaderItem(0)
        item.setText(_translate("SensorsBridge", "Label"))
        item = self.sensors_config_tw.horizontalHeaderItem(1)
        item.setText(_translate("SensorsBridge", "Type"))
        item = self.sensors_config_tw.horizontalHeaderItem(2)
        item.setText(_translate("SensorsBridge", "Code"))
        item = self.sensors_config_tw.horizontalHeaderItem(3)
        item.setText(_translate("SensorsBridge", "Header"))
        item = self.sensors_config_tw.horizontalHeaderItem(4)
        item.setText(_translate("SensorsBridge", "Exclude"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.sensors_config_tbx), _translate("SensorsBridge", "Sensors Configuration"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.log_tbx), _translate("SensorsBridge", "Log"))