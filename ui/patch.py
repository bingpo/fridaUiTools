# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patch.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PatchDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(372, 463)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.cmbPackage = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbPackage.setObjectName("cmbPackage")
        self.cmbPackage.addItem("")
        self.gridLayout_2.addWidget(self.cmbPackage, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.txtPatchAsm = QtWidgets.QLineEdit(self.groupBox)
        self.txtPatchAsm.setText("")
        self.txtPatchAsm.setObjectName("txtPatchAsm")
        self.gridLayout.addWidget(self.txtPatchAsm, 4, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.listModule = QtWidgets.QListWidget(self.groupBox)
        self.listModule.setObjectName("listModule")
        self.gridLayout.addWidget(self.listModule, 1, 3, 1, 1)
        self.txtAddress = QtWidgets.QLineEdit(self.groupBox)
        self.txtAddress.setText("")
        self.txtAddress.setObjectName("txtAddress")
        self.gridLayout.addWidget(self.txtAddress, 2, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnSubmit = QtWidgets.QPushButton(self.groupBox)
        self.btnSubmit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnSubmit.setObjectName("btnSubmit")
        self.horizontalLayout_2.addWidget(self.btnSubmit)
        self.btnClear = QtWidgets.QPushButton(self.groupBox)
        self.btnClear.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout_2.addWidget(self.btnClear)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 3, 1, 1)
        self.txtModule = QtWidgets.QLineEdit(self.groupBox)
        self.txtModule.setObjectName("txtModule")
        self.gridLayout.addWidget(self.txtModule, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.txtPatch = QtWidgets.QLineEdit(self.groupBox)
        self.txtPatch.setText("")
        self.txtPatch.setObjectName("txtPatch")
        self.gridLayout.addWidget(self.txtPatch, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.cmbMode = QtWidgets.QComboBox(self.groupBox)
        self.cmbMode.setObjectName("cmbMode")
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.gridLayout.addWidget(self.cmbMode, 5, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Patch"))
        self.groupBox_2.setTitle(_translate("Dialog", "指定缓存数据"))
        self.label_5.setText(_translate("Dialog", "进程名："))
        self.cmbPackage.setItemText(0, _translate("Dialog", "选择缓存数据"))
        self.groupBox.setTitle(_translate("Dialog", "patch"))
        self.label_6.setText(_translate("Dialog", "patch Asm："))
        self.btnSubmit.setText(_translate("Dialog", "提交"))
        self.btnClear.setText(_translate("Dialog", "清空"))
        self.txtModule.setText(_translate("Dialog", "libnative-lib.so"))
        self.label_2.setText(_translate("Dialog", "地址："))
        self.label_3.setText(_translate("Dialog", "模块名："))
        self.label_4.setText(_translate("Dialog", "patch Code："))
        self.label_7.setText(_translate("Dialog", "mode："))
        self.cmbMode.setItemText(0, _translate("Dialog", "arm64"))
        self.cmbMode.setItemText(1, _translate("Dialog", "arm"))
        self.groupBox_3.setTitle(_translate("Dialog", "GroupBox"))
        self.label.setText(_translate("Dialog", "提示：code样例 1F 20 03 D5"))

