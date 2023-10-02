import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from PyQt5.QtCore import Qt
import wget
import os

try:
    # Включите в блок try/except, если вы также нацелены на Mac/Linux
    from PyQt5.QtWinExtras import QtWin                                         #  !!!
    myappid = 'mycompany.myproduct.subproduct.version'                          #  !!!
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)                      #  !!!    
except ImportError:
    pass

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(resource_path('box.png')))

MainWindow = QtWidgets.QMainWindow()
MainWindow.setWindowIcon(QtGui.QIcon(resource_path('box.png')))
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.setWindowFlags(Qt.FramelessWindowHint)
MainWindow.setAttribute(Qt.WA_TranslucentBackground)
MainWindow.show()

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def dx():
    wget.download('https://download.microsoft.com/download/1/7/1/1718CCC4-6315-4D8E-9543-8E28A4E18C4C/dxwebsetup.exe')
    os.system('dxwebsetup.exe')
    os.remove("dxwebsetup.exe")

def vcnew():
    wget.download('https://aka.ms/vs/17/release/vc_redist.x64.exe')
    os.system('vc_redist.x64.exe')
    os.remove("vc_redist.x64.exe")

def vc13():
    wget.download('https://download.visualstudio.microsoft.com/download/pr/10912041/cee5d6bca2ddbcd039da727bf4acb48a/vcredist_x64.exe')
    os.system('vcredist_x64.exe')
    os.remove("vcredist_x64.exe")

def vc12():
    wget.download('https://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x64.exe')
    os.system('vcredist_x64.exe')
    os.remove("vcredist_x64.exe")

def vc10():
    wget.download('https://download.microsoft.com/download/1/6/5/165255E7-1014-4D0A-B094-B6A430A6BFFC/vcredist_x64.exe')
    os.system('vcredist_x64.exe')
    os.remove("vcredist_x64.exe")

def vc8():
    wget.download('https://download.microsoft.com/download/5/D/8/5D8C65CB-C849-4025-8E95-C3966CAFD8AE/vcredist_x64.exe')
    os.system('vcredist_x64.exe')
    os.remove("vcredist_x64.exe")

def vc5():
    wget.download('https://download.microsoft.com/download/8/B/4/8B42259F-5D70-43F4-AC2E-4B208FD8D66A/vcredist_x64.exe')
    os.system('vcredist_x64.exe')
    os.remove("vcredist_x64.exe")

def n481():
    wget.download('https://download.microsoft.com/download/4/b/2/4b21528a-8944-4a9e-b9d4-6474125e540c/NDP481-Web.exe')
    os.system('NDP481-Web.exe')
    os.remove("NDP481-Web.exe")

def n471():
    wget.download('https://download.visualstudio.microsoft.com/download/pr/4312fa21-59b0-4451-9482-a1376f7f3ba4/9947fce13c11105b48cba170494e787f/ndp471-kb4033342-x86-x64-allos-enu.exe')
    os.system('ndp471-kb4033342-x86-x64-allos-enu.exe')
    os.remove("ndp471-kb4033342-x86-x64-allos-enu.exe")

def n472():
    wget.download('https://download.visualstudio.microsoft.com/download/pr/1f5af042-d0e4-4002-9c59-9ba66bcf15f6/124d2afe5c8f67dfa910da5f9e3db9c1/ndp472-kb4054531-web.exe')
    os.system('ndp472-kb4054531-web.exe')
    os.remove("ndp472-kb4054531-web.exe")

def n47():
    wget.download('https://download.visualstudio.microsoft.com/download/pr/c335e1b1-36f5-4fd4-a0d6-4a0c28df8cb9/885c21e46b1848a0a98fe06b4564de7d/ndp47-kb3186500-web.exe')
    os.system('ndp47-kb3186500-web.exe')
    os.remove("ndp47-kb3186500-web.exe")

def n462():
    wget.download('https://download.visualstudio.microsoft.com/download/pr/8e396c75-4d0d-41d3-aea8-848babc2736a/570f7c7e1975df353a4652ae70b3e0ac/ndp462-kb3151802-web.exe')
    os.system('ndp462-kb3151802-web.exe')
    os.remove("ndp462-kb3151802-web.exe")

def n35():
    wget.download('https://download.visualstudio.microsoft.com/download/pr/b635098a-2d1d-4142-bef6-d237545123cb/2651b87007440a15209cac29634a4e45/dotnetfx35.exe')
    os.system('dotnetfx35.exe')
    os.remove("dotnetfx35.exe")

ui.pushButton.clicked.connect(dx)
ui.pushButton_15.clicked.connect(sys.exit)
ui.pushButton_16.clicked.connect(MainWindow.showMinimized)
ui.pushButton_3.clicked.connect(vcnew)
ui.pushButton_4.clicked.connect(vc13)
ui.pushButton_5.clicked.connect(vc12)
ui.pushButton_6.clicked.connect(vc10)
ui.pushButton_7.clicked.connect(vc8)
ui.pushButton_8.clicked.connect(vc5)
ui.pushButton_9.clicked.connect(n481)
ui.pushButton_12.clicked.connect(n472)
ui.pushButton_13.clicked.connect(n471)
ui.pushButton_11.clicked.connect(n47)
ui.pushButton_14.clicked.connect(n462)
ui.pushButton_10.clicked.connect(n35)


sys.exit(app.exec_())