"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui, QtCore


class TFreehandArrowPainter(QtCore.QObject):
    """Painter which does freehand drawing"""

    def __init__(self, canvas):
        """Function to initialise the class"""
        super(TFreehandArrowPainter, self).__init__()

        # set the attributes
        self.colour = QtGui.QColor(168, 34, 3)
        self.name = 'freehand_arrow'

        # set reference to the canvas
        self.canvas = canvas

    def add(self, event):
        """Function which adds a new bit of text to the canvas"""
        self.canvas.items.append({
            'point': QtCore.QPoint(event.x(), event.y()),
            'painter': self.name
        })

    def draw(self, qp, item):
        """Function which actually draws the text"""
        qp.setPen(self.colour)
        qp.drawText(item['point'], 'TADA!')
