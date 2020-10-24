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
        SensorsBridge.resize(961, 633)
        self.verticalLayout = QtWidgets.QVBoxLayout(SensorsBridge)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(SensorsBridge)
        self.toolBox.setObjectName("toolBox")
        self.options_tbx = QtWidgets.QWidget()
        self.options_tbx.setGeometry(QtCore.QRect(0, 0, 939, 421))
        self.options_tbx.setObjectName("options_tbx")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.options_tbx)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.options_tbx)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)
        self.sys_msg_log_ck = QtWidgets.QCheckBox(self.groupBox)
        self.sys_msg_log_ck.setObjectName("sys_msg_log_ck")
        self.gridLayout_2.addWidget(self.sys_msg_log_ck, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.udp_port_sb = QtWidgets.QSpinBox(self.groupBox)
        self.udp_port_sb.setMaximum(1000000)
        self.udp_port_sb.setProperty("value", 50000)
        self.udp_port_sb.setObjectName("udp_port_sb")
        self.gridLayout_2.addWidget(self.udp_port_sb, 5, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 3, 1, 1)
        self.data_folder_btn = QtWidgets.QPushButton(self.groupBox)
        self.data_folder_btn.setObjectName("data_folder_btn")
        self.gridLayout_2.addWidget(self.data_folder_btn, 2, 3, 1, 1)
        self.data_log_ck = QtWidgets.QCheckBox(self.groupBox)
        self.data_log_ck.setObjectName("data_log_ck")
        self.gridLayout_2.addWidget(self.data_log_ck, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.file_keep_limit_sb = QtWidgets.QSpinBox(self.groupBox)
        self.file_keep_limit_sb.setProperty("value", 3)
        self.file_keep_limit_sb.setObjectName("file_keep_limit_sb")
        self.gridLayout_2.addWidget(self.file_keep_limit_sb, 3, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.config_folder_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.config_folder_btn.sizePolicy().hasHeightForWidth())
        self.config_folder_btn.setSizePolicy(sizePolicy)
        self.config_folder_btn.setObjectName("config_folder_btn")
        self.gridLayout_2.addWidget(self.config_folder_btn, 0, 3, 1, 1)
        self.data_folder_lne = QtWidgets.QLineEdit(self.groupBox)
        self.data_folder_lne.setObjectName("data_folder_lne")
        self.gridLayout_2.addWidget(self.data_folder_lne, 2, 1, 1, 2)
        self.config_folder_le = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.config_folder_le.sizePolicy().hasHeightForWidth())
        self.config_folder_le.setSizePolicy(sizePolicy)
        self.config_folder_le.setObjectName("config_folder_le")
        self.gridLayout_2.addWidget(self.config_folder_le, 0, 1, 1, 2)
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
        self.sensors_config_tbx.setGeometry(QtCore.QRect(0, 0, 939, 421))
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
        self.log_tbx.setGeometry(QtCore.QRect(0, 0, 939, 421))
        self.log_tbx.setObjectName("log_tbx")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.log_tbx)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.log_tab = QtWidgets.QTabWidget(self.log_tbx)
        self.log_tab.setObjectName("log_tab")
        self.verticalLayout_4.addWidget(self.log_tab)
        self.toolBox.addItem(self.log_tbx, "")
        self.help = QtWidgets.QWidget()
        self.help.setGeometry(QtCore.QRect(0, 0, 939, 421))
        self.help.setObjectName("help")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.help)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.help_box = QtWidgets.QTextEdit(self.help)
        self.help_box.setReadOnly(True)
        self.help_box.setObjectName("help_box")
        self.verticalLayout_5.addWidget(self.help_box)
        self.toolBox.addItem(self.help, "")
        self.about = QtWidgets.QWidget()
        self.about.setGeometry(QtCore.QRect(0, 0, 939, 421))
        self.about.setObjectName("about")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.about)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.about_2 = QtWidgets.QTextEdit(self.about)
        self.about_2.setReadOnly(True)
        self.about_2.setObjectName("about_2")
        self.verticalLayout_6.addWidget(self.about_2)
        self.toolBox.addItem(self.about, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(SensorsBridge)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Save)
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
        self.label_3.setText(_translate("SensorsBridge", "UDP Port"))
        self.sys_msg_log_ck.setText(_translate("SensorsBridge", "System messages"))
        self.label_2.setText(_translate("SensorsBridge", "Remove files older than"))
        self.label_9.setText(_translate("SensorsBridge", "Log display"))
        self.label_4.setText(_translate("SensorsBridge", "days"))
        self.data_folder_btn.setText(_translate("SensorsBridge", "Browse..."))
        self.data_log_ck.setText(_translate("SensorsBridge", "Data"))
        self.label.setText(_translate("SensorsBridge", "Output data folder"))
        self.label_10.setText(_translate("SensorsBridge", "Configuration folder"))
        self.config_folder_btn.setText(_translate("SensorsBridge", "Browse..."))
        self.server_gb.setTitle(_translate("SensorsBridge", "Server Options"))
        self.label_6.setText(_translate("SensorsBridge", "Server login URL"))
        self.label_7.setText(_translate("SensorsBridge", "Username"))
        self.label_8.setText(_translate("SensorsBridge", "Password"))
        self.label_5.setText(_translate("SensorsBridge", "Server URL"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.options_tbx), _translate("SensorsBridge", "Options"))
        self.add_btn.setText(_translate("SensorsBridge", "Add"))
        self.remove_btn.setText(_translate("SensorsBridge", "Remove"))
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
        self.help_box.setHtml(_translate("SensorsBridge", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Sensors Bridge Documentation</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Sensors Bridge receives data from water quality sensors. It currently supports Ecotriplets 1, 2, and 3, dissolved oxygen, and co2procv and any sensor sent via UDP such as GPS and water quality sensors. It saves data to a folder and sends it to a server.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Options</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Basic Options</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Configuration Folder</span>: By default Sensors Bridge uses its installation folder to store configuration. However, you can change it to any folder in your computer. The default configuration needs to be modified based on the sensors you have and to which COM ports they are connected.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Output</span> <span style=\" font-weight:600;\">Data Folder</span>: is where the data and log files are stored. The data and logs are organized by data followed by the sensor name (generated from sensor label). The data is raw data that directly come from the sensors. You will need to convert it using your server or other software like Microsoft Excel. The output data is CSV file comma delimited that you can open using Spreadsheet software. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Remove Files Older Than</span>: <span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:8pt;\">determines</span> the maximum days data will be stored. Data and logs older that the specified days will be removed.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">UDP Port</span>: the UDP port number to be connected. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Log Display</span>: can be shown in the Log tab if checked. You can see system messages and/or data being saved. Note, this will add extra resources on the computer so it is only recommended for debugging purposes.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Server Options</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to send data to a server, you can check the checkbox to enable it. If you don\'t have a server, make sure to uncheck it. The receiving server must accept Post data. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Server</span>: the URL of the server</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Server Login</span>: the login URL of the server.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Username</span>: the username to have access to the server if any.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Password</span>: the password of the user if any</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Sensors Configuration</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The Sensors Configuration is where you add sensors details. The default configuration comes will all the sensors. You can modify the header fields and the exclude fields. You can add or remove based on the sensors you have and want to capture data from.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Label</span><span style=\" font-size:8pt;\">: The name of the sensor. The sensor name is auto generated by removing the label. The sensor name is used to send data to the server. So, make sure to type it the same way as the server expects the same name. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Type</span><span style=\" font-size:8pt;\">: The communication interface type</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Code</span><span style=\" font-size:8pt;\">: The code of data. The code for COM ports is determined by the port number your computer gives to currently connected ports. Make sure the sensor and the COM port number you choose match. This default configuration will need to be changed here. For UDP,  the code should be the first word before a dollar sign. The UDP expects the following format CODE$[data comma separated]*checksum.  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Header</span><span style=\" font-size:8pt;\">: This is the field name for comma or tab separated data that comes from the sensors. All fields must be included here. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Exclude</span><span style=\" font-size:8pt;\">: If you don\'t want to save some columns, you can exclude them here. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Log</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is the tab that shows the system messages and data on realtime bases when you start capturing data. Each sensor has its on Log tab. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Support and Bug Report</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Contact us at </span><a href=\"mailto:wtb175@msstate.edu\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">wtb175@msstate.edu</span></a><span style=\" font-size:8pt;\"> for support. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create an issue on our </span><a href=\"https://github.com/wondie/sensors_bridge\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">GitHub Repository</span></a><span style=\" font-size:8pt;\">.</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.help), _translate("SensorsBridge", "Help"))
        self.about_2.setHtml(_translate("SensorsBridge", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Sensors Bridge</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Version 1.0.0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Sensors Bridge receives data from water quality sensors. It currently support Ecotriplets 1, 2, and 3, dissolved oxygen, and co2procv and any sensor sent via UDP such as GPS and water quality sensors. It saves data to a folder and sends it to a server.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Sensors Bridge is developed under </span><a href=\"https://www.erdc.usace.army.mil/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">the U.S. Army Engineer Research and Development Center (ERDC)</span></a><span style=\" font-size:8pt;\"> funded project coordinated by </span><a href=\"https://www.gri.msstate.edu/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Mississippi State University Geosystems Research Institute</span></a><span style=\" font-size:8pt;\">. It is initially designed to read water quality sensor and ancillary data from MSU SeaTrac Autonomous Boat and send it to a receiving server and the </span><a href=\"https://water.geosci.msstate.edu/monitor/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Water Monitor</span></a><span style=\" font-size:8pt;\"> web application. It is customizable to use for other sensors but this feature is not yet added. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Authors</span><span style=\" font-size:8pt;\">: Wondimagegn Tesfaye Beshah (Mississippi State University - Department of Geosciences), Jane Moorhead  (Mississippi State University - Department Electrical and Computer Engineering), and Dr. Padmanava Dash  (Mississippi State University - Department of Geosciences).  </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">It is a free software under GNU General Public License 3.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Product Home</span><span style=\" font-size:8pt;\">: </span><a href=\"https://github.com/wondie/sensors_bridge\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://github.com/wondie/sensors_bridge</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Copyright © 2020 </span><a href=\"https://www.msstate.edu/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Mississippi State University</span></a><span style=\" font-size:8pt;\">. All rights reserved.</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.about), _translate("SensorsBridge", "About"))
