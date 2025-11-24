# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(1000, 568)
        Window.setAutoFillBackground(False)
        self.board = QFrame(Window)
        self.board.setObjectName(u"board")
        self.board.setGeometry(QRect(0, 0, 1001, 571))
        self.board.setFrameShape(QFrame.Shape.StyledPanel)
        self.board.setFrameShadow(QFrame.Shadow.Raised)
        self.board.setLineWidth(0)
        self.gridLayoutWidget = QWidget(self.board)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(90, 70, 451, 441))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cell_3_0 = QLabel(self.gridLayoutWidget)
        self.cell_3_0.setObjectName(u"cell_3_0")
        self.cell_3_0.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cell_3_0.setFont(font)
        self.cell_3_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_3_0, 3, 0, 1, 1)

        self.cell_0_1 = QLabel(self.gridLayoutWidget)
        self.cell_0_1.setObjectName(u"cell_0_1")
        self.cell_0_1.setMinimumSize(QSize(0, 0))
        self.cell_0_1.setFont(font)
        self.cell_0_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_0_1, 0, 1, 1, 1)

        self.cell_2_1 = QLabel(self.gridLayoutWidget)
        self.cell_2_1.setObjectName(u"cell_2_1")
        self.cell_2_1.setMinimumSize(QSize(0, 0))
        self.cell_2_1.setFont(font)
        self.cell_2_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_2_1, 2, 1, 1, 1)

        self.cell_3_3 = QLabel(self.gridLayoutWidget)
        self.cell_3_3.setObjectName(u"cell_3_3")
        self.cell_3_3.setMinimumSize(QSize(0, 0))
        self.cell_3_3.setFont(font)
        self.cell_3_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_3_3, 3, 3, 1, 1)

        self.cell_1_2 = QLabel(self.gridLayoutWidget)
        self.cell_1_2.setObjectName(u"cell_1_2")
        self.cell_1_2.setMinimumSize(QSize(0, 0))
        self.cell_1_2.setFont(font)
        self.cell_1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_1_2, 1, 2, 1, 1)

        self.cell_2_2 = QLabel(self.gridLayoutWidget)
        self.cell_2_2.setObjectName(u"cell_2_2")
        self.cell_2_2.setMinimumSize(QSize(0, 0))
        self.cell_2_2.setFont(font)
        self.cell_2_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_2_2, 2, 2, 1, 1)

        self.cell_3_2 = QLabel(self.gridLayoutWidget)
        self.cell_3_2.setObjectName(u"cell_3_2")
        self.cell_3_2.setMinimumSize(QSize(0, 0))
        self.cell_3_2.setFont(font)
        self.cell_3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_3_2, 3, 2, 1, 1)

        self.cell_2_3 = QLabel(self.gridLayoutWidget)
        self.cell_2_3.setObjectName(u"cell_2_3")
        self.cell_2_3.setMinimumSize(QSize(0, 0))
        self.cell_2_3.setFont(font)
        self.cell_2_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_2_3, 2, 3, 1, 1)

        self.cell_0_2 = QLabel(self.gridLayoutWidget)
        self.cell_0_2.setObjectName(u"cell_0_2")
        self.cell_0_2.setMinimumSize(QSize(0, 0))
        self.cell_0_2.setFont(font)
        self.cell_0_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_0_2, 0, 2, 1, 1)

        self.cell_1_1 = QLabel(self.gridLayoutWidget)
        self.cell_1_1.setObjectName(u"cell_1_1")
        self.cell_1_1.setMinimumSize(QSize(0, 0))
        self.cell_1_1.setFont(font)
        self.cell_1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_1_1, 1, 1, 1, 1)

        self.cell_1_0 = QLabel(self.gridLayoutWidget)
        self.cell_1_0.setObjectName(u"cell_1_0")
        self.cell_1_0.setMinimumSize(QSize(0, 0))
        self.cell_1_0.setFont(font)
        self.cell_1_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_1_0, 1, 0, 1, 1)

        self.cell_0_3 = QLabel(self.gridLayoutWidget)
        self.cell_0_3.setObjectName(u"cell_0_3")
        self.cell_0_3.setMinimumSize(QSize(0, 0))
        self.cell_0_3.setFont(font)
        self.cell_0_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_0_3, 0, 3, 1, 1)

        self.cell_3_1 = QLabel(self.gridLayoutWidget)
        self.cell_3_1.setObjectName(u"cell_3_1")
        self.cell_3_1.setMinimumSize(QSize(0, 0))
        self.cell_3_1.setFont(font)
        self.cell_3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_3_1, 3, 1, 1, 1)

        self.cell_0_0 = QLabel(self.gridLayoutWidget)
        self.cell_0_0.setObjectName(u"cell_0_0")
        self.cell_0_0.setMinimumSize(QSize(0, 0))
        self.cell_0_0.setFont(font)
        self.cell_0_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_0_0, 0, 0, 1, 1)

        self.cell_2_0 = QLabel(self.gridLayoutWidget)
        self.cell_2_0.setObjectName(u"cell_2_0")
        self.cell_2_0.setMinimumSize(QSize(0, 0))
        self.cell_2_0.setFont(font)
        self.cell_2_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_2_0, 2, 0, 1, 1)

        self.cell_1_3 = QLabel(self.gridLayoutWidget)
        self.cell_1_3.setObjectName(u"cell_1_3")
        self.cell_1_3.setMinimumSize(QSize(0, 0))
        self.cell_1_3.setFont(font)
        self.cell_1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cell_1_3, 1, 3, 1, 1)

        self.scoreLabel = QLabel(self.board)
        self.scoreLabel.setObjectName(u"scoreLabel")
        self.scoreLabel.setGeometry(QRect(610, 70, 211, 30))
        self.scoreLabel.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.scoreLabel.setFont(font1)
        self.RestartButton = QPushButton(self.board)
        self.RestartButton.setObjectName(u"RestartButton")
        self.RestartButton.setGeometry(QRect(760, 470, 201, 41))

        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"Form", None))
        self.cell_3_0.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_0_1.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_2_1.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_3_3.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_1_2.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_2_2.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_3_2.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_2_3.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_0_2.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_1_1.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_1_0.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_0_3.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_3_1.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_0_0.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_2_0.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.cell_1_3.setText(QCoreApplication.translate("Window", u"TextLabel", None))
        self.scoreLabel.setText(QCoreApplication.translate("Window", u"Score: 0", None))
        self.RestartButton.setText(QCoreApplication.translate("Window", u"Restart Game", None))
    # retranslateUi

