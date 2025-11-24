import random

class Game2048:
    def __init__(self):
        # Размер поля (выбирать 4 на 4 только)
        self.size = 4
        # Создаем пустое поле (заполненное нулями)
        self.grid = [[0] * self.size for _ in range(self.size)]
        # Текущие очки
        self.score = 0
        # Добавляем две случайные начальные плитки
        self.add_tile()
        self.add_tile()

    # ##### ДОБАВЛЕНИЕ НОВОЙ ПЛИТКИ #####s
    def add_tile(self):
        # Находим все пустые клетки (значение 0)
        empty = [(r, c) for r in range(self.size) for c in range(self.size)
                 if self.grid[r][c] == 0]
        if empty:
            # Выбираем случайную пустую клетку
            r, c = random.choice(empty)
            # С вероятностью 0.9 ставим 2, иначе 4
            self.grid[r][c] = 2 if random.random() < 0.9 else 4

    # #### СЖАТИЕ РЯДА ВЛЕВО ####
    def compress(self, row):
        """
        Сдвигает все ненулевые числа в ряду влево,
        оставляя справа нули
        """
        new_row = [i for i in row if i != 0]          # все ненулевые числа
        new_row += [0] * (self.size - len(new_row))   # Добавляем нули справа
        return new_row

    # ###### ОБЪЕДИНЕНИЕ ПЛИТОК В РЯДУ ######
    def merge(self, row):
        """
        Объединяет одинаковые соседние числа слева направо
        Возвращает новый ряд и сумму очков, полученных при сложении (столкновении плиток)
        """
        score = 0
        for i in range(self.size - 1):
            # если текущая клетка равна следующей и не ноль   (можно соединить только одинковые клетки)
            if row[i] == row[i+1] and row[i] != 0:
                row[i] *= 2          # Удваиваем значение
                row[i+1] = 0         # Следующую обнуляем
                score += row[i]      # Добавляем очки
        return row, score

    # #### ДВИЖЕНИЕ ВЛЕВО ##### ВНИМЕНИЕ ВСЁ ДЕЛАЕТСЯ ЧЕЕРЕЗ ДВИЖЕНИЕ ВЛЕВО И СЖАТИЕ
    def move_left(self):
        moved = False          # произошло ли движение
        total_score = 0        # Сумма очков за этот ход
        new_grid = []

        for row in self.grid:
            compressed = self.compress(row)          # Сжимаем ряд влево
            merged, score = self.merge(compressed)  # Объединяем плитки
            compressed = self.compress(merged)      # Снова сжимаем после слияния
            new_grid.append(compressed)             # Добавляем в новый ряд
            total_score += score                    # Добавляем очки
            if compressed != row:
                moved = True                        # Если ряд изменился, движение произошло

        self.grid = new_grid

        # Добавляем очки к общему счету
        if total_score > 0:
            self.score += total_score

        # Если произошло движение, добавляем новую плитку
        if moved:
            self.add_tile()

    # ##### ДВИЖЕНИЕ ВПРАВО #####
    def move_right(self):
        # Разворачиваем каждую строку, делаем движение влево и разворачиваем обратно
        self.grid = [row[::-1] for row in self.grid]
        self.move_left()
        self.grid = [row[::-1] for row in self.grid]

    # ##### ДВИЖЕНИЕ ВВЕРХ #####
    def move_up(self):
        # Транспонируем сетку (ДЕЛАЕМ СТРОКИ СТОЛБАЦМИ И НАОБООРОТ)
        self.grid = list(map(list, zip(*self.grid)))
        self.move_left()                   # Движение влево по транспонированной сетке
        self.grid = list(map(list, zip(*self.grid)))  # Транспонируем обратно

    # ##### ДВИЖЕНИЕ ВНИЗ #####
    def move_down(self):
        # Транспонируем сетку, движение вправо, транспонируем обратно   (ТО ЕСТЬ ДВИЖЕНИЕ ВЛЕВО РАЗВЕРНУТОЙ ТРАНСПОНИРОВАННОЙ СЕТКИ)
        self.grid = list(map(list, zip(*self.grid)))
        self.move_right()
        self.grid = list(map(list, zip(*self.grid)))

    # ##### ПРОВЕРКА, МОЖНО ЛИ ДВИГАТЬСЯ #####
    def can_move(self):
        # Если есть хотя бы одна пустая клетка, ход возможен
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0:
                    return True

        # Проверка горизонтальных слияний
        for r in range(self.size):
            for c in range(self.size - 1):
                if self.grid[r][c] == self.grid[r][c + 1]:
                    return True

        # Проверка вертикальных слияний
        for c in range(self.size):
            for r in range(self.size - 1):
                if self.grid[r][c] == self.grid[r + 1][c]:
                    return True

        # Если ни одна клетка не пустая и нет возможных слияний — ход невозможен
        return False
