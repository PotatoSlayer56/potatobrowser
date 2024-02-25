import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit, QTabWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Potato's Private Browser v1.0")
        self.setWindowIcon(QIcon("icons/potato.png"))
        self.setGeometry(0,0, 900,600)

        toolBar = QToolBar()
        self.addToolBar(toolBar)

        bookmarksBar = QToolBar()
        self.addToolBar(bookmarksBar)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("icons/back.png"))
        self.backButton.setIconSize(QSize(24,24))
        self.backButton.clicked.connect(self.backBtn)
        toolBar.addWidget(self.backButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("icons/forward.png"))
        self.forwardButton.setIconSize(QSize(24,24))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolBar.addWidget(self.forwardButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("icons/reload.png"))
        self.reloadButton.setIconSize(QSize(24,24))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolBar.addWidget(self.reloadButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("icons/home.png"))
        self.homeButton.setIconSize(QSize(24,24))
        self.homeButton.clicked.connect(self.homeBtn)
        toolBar.addWidget(self.homeButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif", 18))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolBar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("icons/search.png"))
        self.searchButton.setIconSize(QSize(24,24))
        self.searchButton.clicked.connect(self.searchBtn)
        toolBar.addWidget(self.searchButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = "https://google.com"
        self.webEngineView.load(QUrl(initialUrl))

        self.bookmarkOne = QPushButton()
        self.bookmarkOne.setIcon(QIcon("icons/youtube.png"))
        self.bookmarkOne.setIconSize(QSize(18,18))
        self.bookmarkOne.setText("Youtube")
        self.bookmarkOne.setFont(QFont("Sanserif"))
        self.bookmarkOne.clicked.connect(self.bookmarkOneBtn)
        bookmarksBar.addWidget(self.bookmarkOne)

    def searchBtn(self):
        myUrl = self.addressLineEdit.text()
        if myUrl.startswith("https://"):
           myUrl = myUrl
        elif myUrl.startswith("http://"):
            myUrl = myUrl
        else:
            myUrl = "https://" + myUrl

        self.webEngineView.load(QUrl(myUrl))

    def homeBtn(self):
        self.webEngineView.load(QUrl("https://google.com"))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()

    def bookmarkOneBtn(self):
        self.webEngineView.load(QUrl("https://youtube.com"))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
