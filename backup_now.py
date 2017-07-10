# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backup_now.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import zipfile
import shutil
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(747, 462)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(460, 60, 241, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 240, 231, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 400, 181, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 110, 671, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 290, 671, 31))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.pushButton.clicked.connect(self.select_source)
        self.pushButton_2.clicked.connect(self.select_dest)
        self.pushButton_3.clicked.connect(self.backup)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Backup Tool", None))
        self.pushButton.setText(_translate("Dialog", "Select Source", None))
        self.pushButton_2.setText(_translate("Dialog", "Select Destination", None))
        self.pushButton_3.setText(_translate("Dialog", "BackUp Now", None))


    def select_source(self):
        print('Source_selected')
        working_directory =  str(QtGui.QFileDialog.getExistingDirectory(Dialog, 'Select USB Drive Location'))
        print(working_directory)  
        
        self.working_directory = working_directory
        self.textBrowser.setText(working_directory)        
        
    def select_dest(self):    
        print('dest_selected')
        self.save_name = str(QtGui.QFileDialog.getSaveFileName(Dialog, "Save Project File", "", "xlsx files (*.zip)"))
        self.textBrowser_2.setText(self.save_name)  
        
    def backup(self):
        print('Backup in progress')
        source_folder = self.working_directory
        target_zip = self.save_name
        zipf = zipfile.ZipFile(target_zip, "w")
        for subdir, dirs, files in os.walk(source_folder):
            for file in files:
                #print os.path.join(subdir, file)
                zipf.write(os.path.join(subdir, file))
                #print "Created ", target_zip  
                
        print('Backup Complete')
      
        

            
            

    def docopy(source_folder, target_folder):
        for subdir, dirs, files in os.walk(source_folder):
            for file in files:
                #print os.path.join(subdir, file)
                shutil.copy2(os.path.join(subdir, file), target_folder)
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

