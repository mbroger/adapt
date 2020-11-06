import random
import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit

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

    comboBox = QtWidgets.QComboBox()
    comboBox.addItem("Open GPS Viewer")
    comboBox.addItem("Go to Viewer")

    comboBox2 = QtWidgets.QComboBox()
    comboBox2.addItem("Open Harvest Progress")
    comboBox2.addItem("Go to Progress")

    

    #################catagories of "toolbox" options...###########################
    datalist = QtWidgets.QListWidget()
    historylist = QtWidgets.QListWidget()
    qlivelist = QtWidgets.QListWidget()
    analyzerslist = QtWidgets.QListWidget()
    viewerslist = QtWidgets.QListWidget()

    #################combine the widgets###########################################
    
    w = QtWidgets.QListWidget()     #can use QWidget() or QListWidget(), maybe others...
    glay = QtWidgets.QGridLayout(w)

#we can use smaller grids within the larger grid. The whole widget can be one color for gui/
#    organization...
#we need to make a new widget for data, history, live, analyzers, and viewers...
#I know how to change the style of individual widget labels so we can just go with that. 
    
    glay.addWidget(a, 1, 0)      #way itself is another grid with "a's" inside of it
    glay.addWidget(b, 1, 1)
    glay.addWidget(c, 1, 2)
    glay.addWidget(d, 0, 0)
    glay.addWidget(e, 0, 1)
    glay.addWidget(f, 0, 2)
    glay.addWidget(comboBox, 1, 1)
    glay.addWidget(comboBox2, 1, 2)



    def __init__(glay):
        super().__init__()
        
##        glay.water = None  # No external window yet.
        glay.button = QtWidgets.QPushButton("Push for Window")
        glay.button.clicked.connect(glay.addWidget(1, 2))
        global button
        return button
      
        glay.addWidget(button, 1, 2)


    a.setStyleSheet("background-color:blue")
    w.setStyleSheet("background-color:green")

    ##################Toolbox categories to choose...######################################
    datalabel = QtWidgets.QListWidgetItem("Data")
    datalabel.setForeground (QtGui.QColor("red"))
    datalabel.setFont(QFont('Mulish', 20, QFont.Bold))  #might try underline later but idk how tf to do it
    historicallabel = QtWidgets.QListWidgetItem("Historical")
    historicallabel.setForeground (QtGui.QColor("purple"))
    livelabel = QtWidgets.QListWidgetItem("Live")
    livelabel.setForeground (QtGui.QColor("blue"))
    analyzerlabel = QtWidgets.QListWidgetItem("Analyzers")
    analyzerlabel.setForeground (QtGui.QColor("pink"))
    viewerlabel = QtWidgets.QListWidgetItem("WebViewers")
    viewerlabel.setForeground (QtGui.QColor("magenta"))
    field1 = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Parkview Field")
    field2 = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Parkview Field")
    field3 = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Parkview Field")
    field4 = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Parkview Field")
    field5 = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Parkview Field")

    ###################click and drag subcategories...#######################################
    ##historical
    IsoBlue2label = QtWidgets.QListWidgetItem("IsoBlue 2")
    IsoBlue1label = QtWidgets.QListWidgetItem("IsoBlue 1")
    Truck5label = QtWidgets.QListWidgetItem("Truck 5")
    Combine1label = QtWidgets.QListWidgetItem("Combine 1")
    Cart2label = QtWidgets.QListWidgetItem("Cart 2")
    Truck6label = QtWidgets.QListWidgetItem("Truck 6")
    ##Live
    IsoBlue2Live = QtWidgets.QListWidgetItem("IsoBlue 2")
    IsoBlue1Live = QtWidgets.QListWidgetItem("IsoBlue 1")
    ##Analyzers
    Fieldshapelabel = QtWidgets.QListWidgetItem("Field Shape")
    Harvestproglabel = QtWidgets.QListWidgetItem("Harvest Progress")
    Traceabilitylabel = QtWidgets.QListWidgetItem("Traceability")
    ##Web Viewers
    GPSviewer = QtWidgets.QListWidgetItem("GPS Replay")
    Fieldshapeviewer = QtWidgets.QListWidgetItem("Field Shapes")
    Harvestprogviewer = QtWidgets.QListWidgetItem("Harvest Progress")
    Traceabilityviewer = QtWidgets.QListWidgetItem("Traceability")
    
    



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
    a.insertItem(12, analyzerlabel)
    a.insertItem(13, Fieldshapelabel)
    a.insertItem(14, Harvestproglabel)
    a.insertItem(15, Traceabilitylabel)
    a.insertItem(16, viewerlabel)
    a.insertItem(17, GPSviewer)
    a.insertItem(18, Fieldshapeviewer)
    a.insertItem(19, Harvestprogviewer)
    a.insertItem(20, Traceabilityviewer)



   ###################items to be moved around...############################################
##    l1 = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Parkview Field")
##    a.insertItem(1, l1)   #first item to be in the list, label l1
##
##
##    
##    a.insertItem(2, l1)   #second item to be in the list, label l1
##    l1 = QtWidgets.QListWidgetItem(QIcon('Field.png'), "Parkview Field")
##    a.insertItem(3, l1)   #third item to be in the list, label l1

    ##################items to be at the top as labels...####################################
    l5 = QtWidgets.QListWidgetItem("Toolbox")  #using as a label

    d.insertItem(1, l5)   #first item to be in the list, label l1
    l6 = QtWidgets.QListWidgetItem("Workspace 1")  #using as a label
    e.insertItem(1, l6)   #second item to be in the list, label l1
    l7 = QtWidgets.QListWidgetItem("Workspace 2")  #using as a label
    f.insertItem(1, l7)   #third item to be in the list, label l1


    
##    for i in range(3):
##        for j in range(3):
####            label = QtWidgets.QLabel("{}x{}".format(i, j))
##            label = QtWidgets.QLabel()
##            color = QtGui.QColor(*random.sample(range(255), 3))
##            label.setStyleSheet("background-color: {}".format(color.name()))
####            glay.addWidget(label, i, j)
##            glay.addWidget(label, i, j)
    glay.setRowStretch(0, 0)
    glay.setRowStretch(1, 6)
##    glay.setRowStretch(2, 27)
    glay.setColumnStretch(0, 1)
    glay.setColumnStretch(1, 2)
    glay.setColumnStretch(2,3)
    w.resize(640, 480)
    w.setWindowTitle("OATS ADAPT")
    w.show()
##    glay.resize(640, 480)
##    glay.show()
    sys.exit(app.exec_())
