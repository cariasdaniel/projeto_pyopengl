import sys
from PySide6 import QtOpenGLWidgets
from PySide6.QtWidgets import *
from OpenGL.GL import *

class MyCanvas (QtOpenGLWidgets.QOpenGLWidget):
    
    def __init__(self, parent = ..., f = ...):
        super(MyCanvas, self).__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("My GL Drawer")
        self.m_w = 0
        self.m_h = 0

    def initializeGL(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
    
    def resizeGL(self, w, h):
        self.m_w = w
        self.m_h = h
        glViewport(0, 0, self.m_w, self.m_h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.m_w, 0.0, self.m_h, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glShadeModel(GL_SMOOTH)
        xA = self.m_w / 2.0
        yA = self.m_h * (3/4)
        xB = self.m_w * (2.0/3.0)
        yB = self.m_h / 3.0
        xC = self.m_w * (1.0/3.0)
        yC = self.m_h / 3.0
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(xA,yA)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(xB,yB)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(xC,yC)
        glEnd()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyCanvas()
    widget.show()
    sys.exit(app.exec())