from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
)
from PySide6.QtCore import Qt

from ui.dashboard import DashboardPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project YAZID - GameBoost AI")
        self.resize(1200, 700)

        self.setStyleSheet("""
        QWidget{
            background-color:#121212;
            color:white;
            font-family:Segoe UI;
            font-size:14px;
        }

        QFrame#sidebar{
            background-color:#1B1B1B;
            border-right:1px solid #2C2C2C;
        }

        QPushButton{
            background:transparent;
            border:none;
            padding:12px;
            text-align:left;
            border-radius:8px;
        }

        QPushButton:hover{
            background:#7C3AED;
        }

        QPushButton:pressed{
            background:#5B21B6;
        }

        QLabel#logo{
            font-size:24px;
            font-weight:bold;
            color:#BB86FC;
        }

        QLabel#version{
            color:gray;
        }
        """)

        # -----------------------
        # Layout اصلی
        # -----------------------

        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # -----------------------
        # Sidebar
        # -----------------------

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(220)

        sidebar_layout = QVBoxLayout(sidebar)

        logo = QLabel("⚡ YAZID")
        logo.setObjectName("logo")
        logo.setAlignment(Qt.AlignCenter)

        sidebar_layout.addWidget(logo)

        # -----------------------
        # صفحات
        # -----------------------

        self.stack = QStackedWidget()

        self.dashboard = DashboardPage()

        self.stack.addWidget(self.dashboard)

        self.stack.setCurrentWidget(self.dashboard)

        # -----------------------
        # دکمه Dashboard
        # -----------------------

        dashboard_btn = QPushButton("🏠 Dashboard")
        dashboard_btn.clicked.connect(self.show_dashboard)

        sidebar_layout.addWidget(dashboard_btn)

        # -----------------------
        # دکمه‌های بعدی
        # -----------------------

        names = [
            "📊 Monitor",
            "🚀 Boost",
            "🎮 Games",
            "⚙ Settings",
            "💎 VIP",
            "ℹ About"
        ]

        for name in names:
            btn = QPushButton(name)
            btn.setEnabled(False)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        version = QLabel("YAZID v0.2 Alpha")
        version.setObjectName("version")
        version.setAlignment(Qt.AlignCenter)

        sidebar_layout.addWidget(version)

        root.addWidget(sidebar)
        root.addWidget(self.stack)

    # -----------------------

    def show_dashboard(self):
        print("Dashboard Clicked")
        self.stack.setCurrentWidget(self.dashboard)