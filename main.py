from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QObject, QEvent
from game import Game2048  # Импорт класса игры 2048



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ##### ЗАГРУЗКА UI #####
        loader = QUiLoader()  # создаем загрузчик UI
        ui_file = QFile("form.ui")  # указываем путь к .ui файлу
        ui_file.open(QFile.ReadOnly)  # открываем файл
        self.ui = loader.load(ui_file, self)  # загружаем UI в self.ui
        ui_file.close()  # закрываем файл

        # устанавливаем родителя для UI
        self.ui.setParent(self)

        # ##### ФОКУС ДЛЯ КНОПОК #####  НЕ УБИРАТЬ!!!!!!! --------------------------------
        self.ui.setFocusPolicy(Qt.StrongFocus)
        self.ui.setFocus()
#------------------------------------------------------------- НЕ УБИРАТЬ!

        # ##### ЛОГИКА ИГРЫ #####
        self.game = Game2048()  # объект игры

        # ##### КНОПКА ПЕРЕЗАПУСКА #####
        # подключаем сигнал нажатия к функции restart_game
        self.ui.RestartButton.clicked.connect(self.restart_game)

        # ##### СТИЛИ И ОБНОВЛЕНИЕ UI #####
        self.apply_styles()  # применяем стили к элементам
        self.update_ui()     # обновляем отображение игрового поля

    # ##### СТИЛИ #####
    def apply_styles(self):
        # Стиль доски и клеток (стилизуется как css )
        self.ui.setStyleSheet("""
            #board {
                background: #bbada0;  /* фон доски */
                border-radius: 10px;   /* скругление углов */
                padding: 10px;         /* отступы внутри доски */
            }
            QLabel {
                background: #cdc1b4;  /* фон клеток */
                border-radius: 6px;    /* скругление клеток */
                font-size: 32px;       /* размер шрифта */
                font-weight: bold;     /* жирный шрифт */
                color: #776e65;        /* цвет текста */
                min-width: 100px;      /* минимальная ширина клетки */
                min-height: 100px;     /* минимальная высота клетки */
            }
        """)

        # cтиль для лейбла скора
        self.ui.scoreLabel.setStyleSheet("""
            background: #cdc1b4;
            color: #776e65;
            font-size: 24px;
            font-weight: bold;
            border-radius: 6px;
            padding: -20px 10px;   /* вертикальные и горизонтальные отступы */
        """)

        # cтиль для лейбла бест скор
        self.ui.bestScore.setStyleSheet("""
            background: #cdc1b4;
            color: #776e65;
            font-size: 24px;
            font-weight: bold;
            border-radius: 6px;
            padding: -20px 10px;   /* вертикальные и горизонтальные отступы */
        """)

        # Стиль кнопки рестарта
        self.ui.RestartButton.setStyleSheet("""
            background: #776e65;
            color: #cdc1b4;
            font-size: 24px;
            font-weight: bold;
            border-radius: 6px;
        """)

    # ---------- ФИЛЬТР СОБЫТИЙ ДЛЯ КЛАВИАТУРЫ ----------
    def eventFilter(self, obj: QObject, event: QEvent):
        # усли событие — нажатие клавиши
        if event.type() == QEvent.KeyPress:
            self.keyPressEvent(event)  # перенаправляем на обработку keyPressEvent
            return True
        return False

    # ---------- ОБРАБОТКА НАЖАТИЯ КЛАВИШ ----------
    def keyPressEvent(self, event):
        key = event.key()  # какая стрелка нажата

        # какая стрелка нажата
        if key == Qt.Key_Left:
            self.game.move_left()
        elif key == Qt.Key_Right:
            self.game.move_right()
        elif key == Qt.Key_Up:
            self.game.move_up()
        elif key == Qt.Key_Down:
            self.game.move_down()
        else:
            return  # если нажата не стрелка

        self.update_ui()  # Обновляем интерфейс после хода

        # проверка конца игры
        if not self.game.can_move():
            self.show_game_over()

    # ---------- ОБНОВЛЕНИЕ UI (КЛЕТКИ И СЧЕТ) ----------
    def update_ui(self):
        # Цвета клеток по значениям
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

        # обновляем скор
        self.ui.scoreLabel.setText(f"Score: {self.game.score}")

        # Обновляем каждую клетку
        for r in range(4):
            for c in range(4):
                label = getattr(self.ui, f"cell_{r}_{c}")  # Получаем QLabel
                value = self.game.grid[r][c]               # Текущее значение клетки

                bg, fg = TILE_COLORS.get(value, ("#3c3a32", "#f9f6f2"))

                # чем больше число, тем меньше щрифт (чтобы влезало в клетку)
                if value < 128:
                    font_size = 36
                elif value < 1024:
                    font_size = 32
                else:
                    font_size = 28

                # стиль клетки
                label.setStyleSheet(f"""
                    background: {bg};
                    color: {fg};
                    border-radius: 6px;
                    font-weight: bold;
                    font-size: {font_size}px;
                """)

                # Устанавливаем текст клетки
                label.setText("" if value == 0 else str(value))

    # ---------- ОКНО КОНЦА ИГРЫ ----------
    def show_game_over(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Game Over")
        msg.setText(f"Game Over!\nYour score: {self.game.score}")
        msg.setIcon(QMessageBox.Information)

        # кнопки выбора после проигрыша
        new_game_button = msg.addButton("New Game", QMessageBox.AcceptRole) #начать новую игру
        quit_button = msg.addButton("Quit", QMessageBox.RejectRole)   #выйти

        msg.exec()  # Показать диалоговое окно

        # Проверяем, какая кнопка нажата
        if msg.clickedButton() == new_game_button:
            self.restart_game()
        else:
            self.close()

    # ---------- ПЕРЕЗАПУСК ИГРЫ ----------
    def restart_game(self):
        self.game = Game2048()  # Создаем новую игру
        self.update_ui()         # обновляем ui



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
