from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QProgressBar
)

from PySide6.QtCore import Qt, QTimer
import psutil


class InfoCard(QFrame):

    def __init__(self, title):
        super().__init__()

        self.setFixedSize(220, 260)

        self.setStyleSheet("""
        QFrame{
            background:#1C1C1C;
            border:1px solid #2F2F2F;
            border-radius:18px;
        }

        QLabel{
            background:transparent;
            color:white;
        }
        """)

        root = QVBoxLayout(self)
        root.setSpacing(12)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet("""
        font-size:18px;
        color:#BBBBBB;
        font-weight:bold;
        """)

        root.addWidget(self.title)

        bar_layout = QHBoxLayout()

        self.bar = QProgressBar()

        self.bar.setOrientation(Qt.Vertical)

        self.bar.setMinimum(0)
        self.bar.setMaximum(100)
        self.bar.setValue(0)

        self.bar.setTextVisible(False)

        self.bar.setFixedSize(35,150)

        self.bar.setStyleSheet("""
        QProgressBar{
            background:#2E2E2E;
            border:none;
            border-radius:12px;
        }

        QProgressBar::chunk{
            background:#BB86FC;
            border-radius:12px;
        }
        """)

        bar_layout.addStretch()
        bar_layout.addWidget(self.bar)
        bar_layout.addStretch()

        root.addLayout(bar_layout)

        self.value = QLabel("0%")
        self.value.setAlignment(Qt.AlignCenter)

        self.value.setStyleSheet("""
        font-size:28px;
        font-weight:bold;
        color:#BB86FC;
        """)

        root.addWidget(self.value)

        self.live = QLabel("LIVE")
        self.live.setAlignment(Qt.AlignCenter)

        self.live.setStyleSheet("""
        color:gray;
        font-size:12px;
        """)

        root.addWidget(self.live)


        class DashboardPage(QWidget):

         def __init__(self):
          super().__init__()

        root = QVBoxLayout(self)

        root.setContentsMargins(20,20,20,20)
        root.setSpacing(20)

        title = QLabel("Dashboard")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
        font-size:30px;
        font-weight:bold;
        color:#BB86FC;
        """)

        root.addWidget(title)

        cards = QHBoxLayout()
        cards.setSpacing(20)

        self.cpu = InfoCard("🖥 CPU")
        self.ram = InfoCard("🧠 RAM")
        self.disk = InfoCard("💾 Disk")

        cards.addWidget(self.cpu)
        cards.addWidget(self.ram)
        cards.addWidget(self.disk)

        root.addLayout(cards)

        root.addStretch()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(1000)

        self.update_info()

    def set_bar_color(self, bar, value):

        if value < 50:
            color = "#22C55E"

        elif value < 80:
            color = "#FACC15"

        else:
            color = "#EF4444"

        bar.setStyleSheet(f"""
        QProgressBar{{
            background:#2E2E2E;
            border:none;
            border-radius:12px;
        }}

        QProgressBar::chunk{{
            background:{color};
            border-radius:12px;
        }}
        """)

    def update_info(self):

        cpu = int(psutil.cpu_percent(interval=None))
        ram = int(psutil.virtual_memory().percent)
        disk = int(psutil.disk_usage("/").percent)

        # CPU
        self.cpu.bar.setValue(cpu)
        self.cpu.value.setText(f"{cpu}%")
        self.set_bar_color(self.cpu.bar, cpu)

        # RAM
        self.ram.bar.setValue(ram)
        self.ram.value.setText(f"{ram}%")
        self.set_bar_color(self.ram.bar, ram)

        # Disk
        self.disk.bar.setValue(disk)
        self.disk.value.setText(f"{disk}%")
        self.set_bar_color(self.disk.bar, disk)