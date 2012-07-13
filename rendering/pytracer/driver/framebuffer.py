import sys
import struct

import PyQt4
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtNetwork import QTcpServer,QTcpSocket, QHostAddress


class TcpServer(QTcpServer):
    def __init__(self, parent = None):
        QTcpServer.__init__(self, parent)
        settings = QSettings()
        self.parent = parent
        # We just assume everything is going fine, gui should do the check here like this:
        # if tcpServer.isListening():
        self.listen(QHostAddress(QHostAddress.Any),
        settings.value("server/port", QVariant(5006)).toInt()[0])
        self.sockets= {}
        QObject.connect(self,SIGNAL("newConnection()"),self.handleIncomingConnection)

    def incomingConnection(self, socketDescriptor):
        # this is called when someone tries to connect
        QTcpServer.incomingConnection(self,socketDescriptor)
        #print "connection stablished"

    def handleIncomingConnection(self):
        #print "NEW CONNECTION"
        self.socket = self.nextPendingConnection()
        self.socket.parent = self.parent
        self.sockets[self.socket.socketDescriptor()] = self.socket
        #self.socket.write(QByteArray("1"))
        QObject.connect( self.socket, SIGNAL("readyRead()"), self.tcpSocketReadyReadEmitted )
        self.socket.readyRead.emit()
        
    def tcpSocketReadyReadEmitted(self):
        txt = str(self.socket.readAll())
        while len(txt) > 0:
            txtAr = struct.unpack("6s",txt[:6])
            txt = txt[8:]  
            if txtAr[0] == "imgnfo":
                uvals = struct.unpack("II",txt[:8])
                txt = txt[8:]
                # resize the window
                w = int(uvals[0])
                h = int(uvals[1])
                self.parent.resize(w,h)
                px = QtGui.QPixmap(w,h)
                px.fill(Qt.black)
                lbl = QtGui.QLabel()
                lbl.setPixmap(px)
                layout = self.parent.layout()
                self.parent.layout().addWidget(lbl)

            elif txtAr[0] == "bucket":
                layout = self.parent.layout()
                lbl = layout.currentWidget()

                uvals = struct.unpack("IIII",txt[:16])
                if uvals[0] == 0 and uvals[1] == 0:
                    lbl.pixmap().fill(Qt.black)
                    
                txt = txt[16:]
                upack = 3*uvals[2]*uvals[3]
                pixels = struct.unpack("%dI"%upack,txt[:upack*4])
                txt = txt[upack*4:]
                px = lbl.pixmap()
                img = px.toImage()

                for y in range(uvals[3]):
                    for x in range(uvals[2]):
                        tpix = ((y * uvals[2]) + x) * 3 
                        value = QtGui.qRgb(pixels[tpix], 
                                           pixels[tpix+1],
                                           pixels[tpix+2])
                        img.setPixel(uvals[0]+x,uvals[1]+y,value)
                px = px.fromImage(img)
                lbl.setPixmap(px)

if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.setLayout(QtGui.QStackedLayout())
    w.show()
    server = TcpServer(parent=w)
    a.exec_()

