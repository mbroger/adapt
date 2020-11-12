import random
import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QPushButton
from PyQt5.QtCore import Qt


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
##    w = QtWidgets.QWidget()

    ################create list widgets#############################################
    a = QtWidgets.QListWidget()
    
    a.setAcceptDrops(True)
    a.setDragEnabled(True)
    b = QtWidgets.QListWidget()
    b.setAcceptDrops(True)
    b.setDragEnabled(True)
    c = QtWidgets.QListWidget()
    c.setAcceptDrops(True)
    c.setDragEnabled(True)
    d = QtWidgets.QListWidget()
    d.setAcceptDrops(True)
    d.setDragEnabled(True)
    e = QtWidgets.QListWidget()
    e.setAcceptDrops(True)
    e.setDragEnabled(True)
    f = QtWidgets.QListWidget()
    f.setAcceptDrops(True)
    f.setDragEnabled(True)

    def say_hello2():                                                                                     
        print("Button clicked, Hello!")
        u.setWindowTitle("I hope this works")
        u.show()

    def say_hello3():                                                                                     
        print("Button clicked, Hello!")
        u.setWindowTitle("I hope this works")
        u.show()

    comboBox = QtWidgets.QComboBox()
    comboBox.addItem("Open GPS Viewer")
    comboBox.addItem("Go to Viewer")
    comboBox.setFont(QFont('Mulish', 20))
    comboBox.activated.connect(say_hello2)

    u = QtWidgets.QListWidget()

    comboBox2 = QtWidgets.QComboBox()
    comboBox2.addItem("Open Harvest Progress")
    comboBox2.addItem("Go to Progress")
    comboBox2.setFont(QFont('Mulish', 20))
    comboBox2.activated.connect(say_hello3)
  
    #################catagories of "toolbox" options...###########################
    datalist = QtWidgets.QListWidget()
    historylist = QtWidgets.QListWidget()
    qlivelist = QtWidgets.QListWidget()
    analyzerslist = QtWidgets.QListWidget()
    viewerslist = QtWidgets.QListWidget()

    #################combine the widgets###########################################
    
    w = QtWidgets.QListWidget()     #can use QWidget() or QListWidget(), maybe others...
    glay = QtWidgets.QGridLayout(w)

    
    glay.addWidget(a, 1, 0)      #way itself is another grid with "a's" inside of it
    glay.addWidget(b, 1, 1)
    glay.addWidget(c, 1, 2)
    
    glay.addWidget(d, 0, 0)
    glay.addWidget(e, 0, 1)
    glay.addWidget(f, 0, 2)




    def __init__(glay):
        super().__init__()
        
##        glay.water = None  # No external window yet.
        glay.button = QtWidgets.QPushButton("Push for Window")
        glay.button.clicked.connect(glay.addWidget(1, 2))
        global button
        return button
      
        glay.addWidget(button, 1, 2)


    a.setStyleSheet("border-width: 1px; border-style: solid; background-color:royalblue")
    b.setStyleSheet("border-width: 1px; border-style: solid; background-color:royalblue")
    c.setStyleSheet("border-width: 1px; border-style: solid; background-color:royalblue")

  #  a.setStyleSheet("border-width: 0px; border-style: solid")
    w.setStyleSheet("border-width: 0px; border-style: solid; border-color: aliceblue; background-color:royalblue")
    glay.setAlignment(Qt.AlignTop)  #these aren't working for some reason...................
    glay.setAlignment(Qt.AlignCenter)
 #   w.setStyleSheet("border-width: 0px; border-style: solid")

    ##################Toolbox categories to choose...######################################
    datalabel = QtWidgets.QListWidgetItem("Data")
    datalabel.setForeground (QtGui.QColor("aliceblue"))
    datalabel.setFont(QFont('Mulish', 20, QFont.Bold))  
    historicallabel = QtWidgets.QListWidgetItem("Historical")
    historicallabel.setForeground (QtGui.QColor("aliceblue"))
    livelabel = QtWidgets.QListWidgetItem("Live")
    livelabel.setForeground (QtGui.QColor("aliceblue"))
    analyzerlabel = QtWidgets.QListWidgetItem("Analyzers")
    analyzerlabel.setForeground (QtGui.QColor("aliceblue"))
    viewerlabel = QtWidgets.QListWidgetItem("WebViewers")
    viewerlabel.setForeground (QtGui.QColor("aliceblue"))
    Insightslabel = QtWidgets.QListWidgetItem("Insights")
    Insightslabel.setForeground (QtGui.QColor("aliceblue"))
    Insightslabel.setFont(QFont('Mulish', 20, QFont.Bold))

    ###################click and drag subcategories...#######################################
    ##historical
    IsoBlue2label = QtWidgets.QListWidgetItem(QIcon('isoblue.png'),("IsoBlue 2"))
    IsoBlue2label.setForeground (QtGui.QColor("aliceblue"))
    IsoBlue2label.setFont(QFont('Mulish'))
    IsoBlue1label = QtWidgets.QListWidgetItem(QIcon('isoblue.png'),("IsoBlue 1"))
    IsoBlue1label.setForeground (QtGui.QColor("aliceblue"))
    IsoBlue1label.setFont(QFont('Mulish'))
    Truck5label = QtWidgets.QListWidgetItem(QIcon('truck.png'),("Truck 5"))
    Truck5label.setForeground (QtGui.QColor("aliceblue"))
    Truck5label.setFont(QFont('Mulish'))
    Combine1label = QtWidgets.QListWidgetItem(QIcon('combine.png'), ("Combine 1"))
    Combine1label.setForeground (QtGui.QColor("aliceblue"))
    Combine1label.setFont(QFont('Mulish'))
    Cart2label = QtWidgets.QListWidgetItem(QIcon('cart.png'), ("Cart 2"))
    Cart2label.setForeground (QtGui.QColor("aliceblue"))
    Cart2label.setFont(QFont('Mulish'))
    Truck6label = QtWidgets.QListWidgetItem(QIcon('truck.png'), ("Truck 6"))
    Truck6label.setForeground (QtGui.QColor("aliceblue"))
    Truck6label.setFont(QFont('Mulish'))
    ##Live
    IsoBlue2Live = QtWidgets.QListWidgetItem(QIcon('isoblue.png'),("IsoBlue 2"))
    IsoBlue2Live.setForeground (QtGui.QColor("aliceblue"))
    IsoBlue2Live.setFont(QFont('Mulish'))
    IsoBlue1Live = QtWidgets.QListWidgetItem(QIcon('isoblue.png'),("IsoBlue 1"))
    IsoBlue1Live.setForeground (QtGui.QColor("aliceblue"))
    IsoBlue1Live.setFont(QFont('Mulish'))
    ##Analyzers
    Fieldshapelabel = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Field Shape")
    Fieldshapelabel.setForeground (QtGui.QColor("aliceblue"))
    Fieldshapelabel.setFont(QFont('Mulish'))
    Harvestproglabel = QtWidgets.QListWidgetItem(QIcon('hourglass.png'), "Harvest Progress")
    Harvestproglabel.setForeground (QtGui.QColor("aliceblue"))
    Harvestproglabel.setFont(QFont('Mulish'))
    Traceabilitylabel = QtWidgets.QListWidgetItem(QIcon('pencil.png'), "Traceability")
    Traceabilitylabel.setForeground (QtGui.QColor("aliceblue"))
    Traceabilitylabel.setFont(QFont('Mulish'))
    ##Web Viewers
    GPSviewer = QtWidgets.QListWidgetItem(QIcon('replay.png'), "GPS Replay")
    GPSviewer.setForeground (QtGui.QColor("aliceblue"))
    GPSviewer.setFont(QFont('Mulish'))
    Fieldshapeviewer = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Field Shape")
    Fieldshapeviewer.setForeground (QtGui.QColor("aliceblue"))
    Fieldshapeviewer.setFont(QFont('Mulish'))
    Harvestprogviewer = QtWidgets.QListWidgetItem(QIcon('hourglass.png'), "Harvest Progress")
    Harvestprogviewer.setForeground (QtGui.QColor("aliceblue"))
    Harvestprogviewer.setFont(QFont('Mulish'))
    Traceabilityviewer = QtWidgets.QListWidgetItem(QIcon('pencil.png'), "Traceability")
    Traceabilityviewer.setForeground (QtGui.QColor("aliceblue"))
    Traceabilityviewer.setFont(QFont('Mulish'))




    a.insertItem(1, datalabel)
    a.insertItem(2, historicallabel)
    a.insertItem(3, IsoBlue2label)
    a.insertItem(4, IsoBlue1label)
    a.insertItem(5, Truck5label)
    a.insertItem(6, Combine1label)
    a.insertItem(7, Cart2label)
    a.insertItem(8, Truck6label)
    a.insertItem(9, livelabel)
    a.insertItem(10, IsoBlue2Live)
    a.insertItem(11, IsoBlue1Live)
    a.insertItem(12, Insightslabel)
    a.insertItem(13, analyzerlabel)
    a.insertItem(14, Fieldshapelabel)
    a.insertItem(15, Harvestproglabel)
    a.insertItem(16, Traceabilitylabel)
    a.insertItem(17, viewerlabel)
    a.insertItem(18, GPSviewer)
    a.insertItem(19, Fieldshapeviewer)
    a.insertItem(20, Harvestprogviewer)
    a.insertItem(21, Traceabilityviewer)

    glay.addWidget(comboBox, 1, 1)
    
    glay.addWidget(comboBox2, 1, 2)

    


    ##################items to be at the top as labels...####################################
    l5 = QtWidgets.QListWidgetItem("         TOOLBOX")  #using as a label
    l5.setForeground (QtGui.QColor("aliceblue"))
    l5.setFont(QFont('Mulish', 40))
    d.insertItem(1, l5)   #first item to be in the list, label l1
    l6 = QtWidgets.QListWidgetItem("    WORKSPACE 1")  #using as a label
    l6.setForeground (QtGui.QColor("aliceblue"))
    l6.setFont(QFont('Mulish', 40))
    e.insertItem(1, l6)   #second item to be in the list, label l1
    l7 = QtWidgets.QListWidgetItem("    WORKSPACE 2")  #using as a label
    l7.setForeground (QtGui.QColor("aliceblue"))
    l7.setFont(QFont('Mulish', 40))
    f.insertItem(1, l7)   #third item to be in the list, label l1



    glay.setRowStretch(0, 5)
    glay.setRowStretch(1, 50)
##    glay.setRowStretch(2, 27)
    glay.setColumnStretch(0, 1)
    glay.setColumnStretch(1, 1)
    glay.setColumnStretch(2,1)
    w.resize(640, 480)
    w.setWindowTitle("OATS ADAPT")
    w.show()
##    glay.resize(640, 480)
##    glay.show()
    sys.exit(app.exec_())
