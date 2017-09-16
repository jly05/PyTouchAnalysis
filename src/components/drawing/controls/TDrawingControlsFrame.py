"""

PyTouchAnalysis
Version 0.0
(c) Jamie Lynch 2017

"""

from PySide import QtGui
from components.drawing.controls.TDrawingControlButton import TDrawingControlButton


class TDrawingControlsFrame(QtGui.QFrame):
    """Custom frame which contains all of the drawing buttons"""

    def __init__(self, main):
        """Function to initialise the class"""
        super(TDrawingControlsFrame, self).__init__()

        # Set reference to main window and video
        self.main = main

        # set the frame style
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameShadow(QtGui.QFrame.Plain)

        # Create the UI
        self.init_ui()

    def init_ui(self):
        """Function which creates the UI"""

        # Create and set the grid as layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        clickable_icons = ['straight_arrow', 'freehand_arrow', 'line',
                 'multipoint_arc', 'multipoint_square_outline', 'multipoint_square_filled',
                 'free']
        icons = ['clear', 'undo']
        buttons = []

        # Create the buttons and add them to the grid
        for num, icon in enumerate(clickable_icons):
            button = TDrawingControlButton(QtGui.QIcon('resources/icons/{}.png'.format(icon)), '', self.stub, True)
            buttons.append(button)
            # add to the grid in 3 wide rows
            # num // 3 -> 0, 0, 0, 1, 1, 1, etc...
            # num % 3 -> 0, 1, 2, 0, 1, 2, etc...
            grid.addWidget(button, num // 3, num % 3)

        for num, icon in enumerate(icons):
            num += len(clickable_icons)
            button = TDrawingControlButton(QtGui.QIcon('resources/icons/{}.png'.format(icon)), '', self.stub)
            buttons.append(button)
            # add to the grid in 3 wide rows
            # num // 3 -> 0, 0, 0, 1, 1, 1, etc...
            # num % 3 -> 0, 1, 2, 0, 1, 2, etc...
            grid.addWidget(button, num // 3, num % 3)

    def stub(self):
        """Stubbed function to get things working"""
        # TODO: Remove
        return
