# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/infoUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_5.addWidget(self.label_title)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_capture = QtWidgets.QLabel(Form)
        self.label_capture.setMinimumSize(QtCore.QSize(500, 400))
        self.label_capture.setMaximumSize(QtCore.QSize(500, 400))
        self.label_capture.setText("")
        self.label_capture.setObjectName("label_capture")
        self.verticalLayout_4.addWidget(self.label_capture)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_start_collect = QtWidgets.QPushButton(Form)
        self.bt_start_collect.setMinimumSize(QtCore.QSize(0, 100))
        self.bt_start_collect.setMaximumSize(QtCore.QSize(16777215, 100))
        self.bt_start_collect.setObjectName("bt_start_collect")
        self.horizontalLayout_3.addWidget(self.bt_start_collect)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_auto_collect = QtWidgets.QCheckBox(Form)
        self.checkBox_auto_collect.setChecked(True)
        self.checkBox_auto_collect.setObjectName("checkBox_auto_collect")
        self.horizontalLayout.addWidget(self.checkBox_auto_collect)
        self.label_collected = QtWidgets.QLabel(Form)
        self.label_collected.setObjectName("label_collected")
        self.horizontalLayout.addWidget(self.label_collected)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_set_num = QtWidgets.QSpinBox(Form)
        self.spinBox_set_num.setMinimumSize(QtCore.QSize(70, 30))
        self.spinBox_set_num.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBox_set_num.setProperty("value", 12)
        self.spinBox_set_num.setObjectName("spinBox_set_num")
        self.horizontalLayout_2.addWidget(self.spinBox_set_num)
        self.lcdNumber_collection_nums = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_collection_nums.setObjectName("lcdNumber_collection_nums")
        self.horizontalLayout_2.addWidget(self.lcdNumber_collection_nums)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.bt_take_photo = QtWidgets.QPushButton(Form)
        self.bt_take_photo.setMinimumSize(QtCore.QSize(149, 40))
        self.bt_take_photo.setMaximumSize(QtCore.QSize(150, 40))
        self.bt_take_photo.setObjectName("bt_take_photo")
        self.verticalLayout_2.addWidget(self.bt_take_photo)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_check_info = QtWidgets.QPushButton(Form)
        self.bt_check_info.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_check_info.setObjectName("bt_check_info")
        self.verticalLayout_3.addWidget(self.bt_check_info)
        self.bt_change_info = QtWidgets.QPushButton(Form)
        self.bt_change_info.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_change_info.setObjectName("bt_change_info")
        self.verticalLayout_3.addWidget(self.bt_change_info)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_id = QtWidgets.QLabel(Form)
        self.label_id.setObjectName("label_id")
        self.verticalLayout.addWidget(self.label_id)
        self.lineEdit_id = QtWidgets.QLineEdit(Form)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout.addWidget(self.lineEdit_id)
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.label_class = QtWidgets.QLabel(Form)
        self.label_class.setObjectName("label_class")
        self.verticalLayout.addWidget(self.label_class)
        self.lineEdit_class = QtWidgets.QLineEdit(Form)
        self.lineEdit_class.setObjectName("lineEdit_class")
        self.verticalLayout.addWidget(self.lineEdit_class)
        self.label_sex = QtWidgets.QLabel(Form)
        self.label_sex.setObjectName("label_sex")
        self.verticalLayout.addWidget(self.label_sex)
        self.lineEdit_sex = QtWidgets.QLineEdit(Form)
        self.lineEdit_sex.setObjectName("lineEdit_sex")
        self.verticalLayout.addWidget(self.lineEdit_sex)
        self.label_birth = QtWidgets.QLabel(Form)
        self.label_birth.setObjectName("label_birth")
        self.verticalLayout.addWidget(self.label_birth)
        self.lineEdit_birth = QtWidgets.QLineEdit(Form)
        self.lineEdit_birth.setObjectName("lineEdit_birth")
        self.verticalLayout.addWidget(self.lineEdit_birth)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.bt_check_dirs_faces = QtWidgets.QPushButton(Form)
        self.bt_check_dirs_faces.setObjectName("bt_check_dirs_faces")
        self.verticalLayout.addWidget(self.bt_check_dirs_faces)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.bt_start_collect, self.checkBox_auto_collect)
        Form.setTabOrder(self.checkBox_auto_collect, self.spinBox_set_num)
        Form.setTabOrder(self.spinBox_set_num, self.bt_take_photo)
        Form.setTabOrder(self.bt_take_photo, self.lineEdit_id)
        Form.setTabOrder(self.lineEdit_id, self.bt_check_info)
        Form.setTabOrder(self.bt_check_info, self.bt_change_info)
        Form.setTabOrder(self.bt_change_info, self.tableView)
        Form.setTabOrder(self.tableView, self.bt_check_dirs_faces)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "个人信息采集"))
        self.bt_start_collect.setText(_translate("Form", "开始采集"))
        self.checkBox_auto_collect.setText(_translate("Form", " 自动采集"))
        self.label_collected.setText(_translate("Form", "已采集"))
        self.bt_take_photo.setText(_translate("Form", "拍照"))
        self.bt_check_info.setText(_translate("Form", "查询信息（DB）"))
        self.bt_change_info.setText(_translate("Form", "添加或修改信息(DB)"))
        self.label_id.setText(_translate("Form", "请输入学号："))
        self.label_name.setText(_translate("Form", "请输入姓名："))
        self.label_class.setText(_translate("Form", "请输入班级："))
        self.label_sex.setText(_translate("Form", "请输入性别："))
        self.label_birth.setText(_translate("Form", "请输入生日："))
        self.bt_check_dirs_faces.setText(_translate("Form", "查询数据中所有人脸数量"))
