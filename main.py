from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QObject, QEvent
from game import Game2048


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        loader = QUiLoader()
        ui_file = QFile("form.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.ui.setParent(self)

        self.ui.setFocusPolicy(Qt.StrongFocus)
        self.ui.setFocus()

        # Game logic
        self.game = Game2048()

        self.ui.RestartButton.clicked.connect(self.restart_game)


        self.apply_styles()
        self.update_ui()

    # ---------- STYLE ----------
    def apply_styles(self):
        # Board and cells styling
        self.ui.setStyleSheet("""
            #board {
                background: #bbada0;
                border-radius: 10px;
                padding: 10px;
            }
            QLabel {
                background: #cdc1b4;
                border-radius: 6px;
                font-size: 32px;
                font-weight: bold;
                color: #776e65;
                min-width: 100px;
                min-height: 100px;
            }
        """)

        # Score label styling

        self.ui.scoreLabel.setStyleSheet("""
            background: #cdc1b4;
            color: #776e65;
            font-size: 24px;
            font-weight: bold;
            border-radius: 6px;
            padding: -20px 10px;
        """)

        self.ui.RestartButton.setStyleSheet("""
            background: #776e65;
            color: #cdc1b4;
            font-size: 24px;
            font-weight: bold;
            border-radius: 6px;
        """)

    # ---------- EVENT FILTER FOR KEYS ----------
    def eventFilter(self, obj: QObject, event: QEvent):
        if event.type() == QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        return False

    # ---------- KEY EVENTS ----------
    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Left:
            self.game.move_left()
        elif key == Qt.Key_Right:
            self.game.move_right()
        elif key == Qt.Key_Up:
            self.game.move_up()
        elif key == Qt.Key_Down:
            self.game.move_down()
        else:
            return

        self.update_ui()

        # Check game over
        if not self.game.can_move():
            self.show_game_over()

    # ---------- UPDATE GRID UI ----------
    def update_ui(self):
        TILE_COLORS = {
            0: ("#cdc1b4", "#776e65"),
            2: ("#eee4da", "#776e65"),
            4: ("#ede0c8", "#776e65"),
            8: ("#f2b179", "#f9f6f2"),
            16: ("#f59563", "#f9f6f2"),
            32: ("#f67c5f", "#f9f6f2"),
            64: ("#f65e3b", "#f9f6f2"),
            128: ("#edcf72", "#f9f6f2"),
            256: ("#edcc61", "#f9f6f2"),
            512: ("#edc850", "#f9f6f2"),
            1024: ("#edc53f", "#f9f6f2"),
            2048: ("#edc22e", "#f9f6f2"),
        }

        # Score
        self.ui.scoreLabel.setText(f"Score: {self.game.score}")

        # Update cells
        for r in range(4):
            for c in range(4):
                label = getattr(self.ui, f"cell_{r}_{c}")
                value = self.game.grid[r][c]

                bg, fg = TILE_COLORS.get(value, ("#3c3a32", "#f9f6f2"))

                # Adjust font size for large numbers
                if value < 128:
                    font_size = 36
                elif value < 1024:
                    font_size = 32
                else:
                    font_size = 28

                label.setStyleSheet(f"""
                    background: {bg};
                    color: {fg};
                    border-radius: 6px;
                    font-weight: bold;
                    font-size: {font_size}px;
                """)

                label.setText("" if value == 0 else str(value))

    # ---------- GAME OVER ----------
    def show_game_over(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Game Over")
        msg.setText(f"Game Over!\nYour score: {self.game.score}")
        msg.setIcon(QMessageBox.Information)

        new_game_button = msg.addButton("New Game", QMessageBox.AcceptRole)
        quit_button = msg.addButton("Quit", QMessageBox.RejectRole)

        msg.exec()

        if msg.clickedButton() == new_game_button:
            self.restart_game()
        else:
            self.close()

    # ---------- RESTART GAME ----------
    def restart_game(self):
        self.game = Game2048()
        self.update_ui()


# ---------- APPLICATION EXEC ----------
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
