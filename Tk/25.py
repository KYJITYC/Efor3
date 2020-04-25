root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)


class ball():

    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])

        self.id = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30


    def set_coords(self):

        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )


    def move(self):
        """Переместить мяч по прошествии единицы времени.
            Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
            self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
            """
        # FIXME
        self.x += self.vx
        self.y -= self.vy


    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
            Args:
                obj: Обьект, с которым проверяется столкновение.
            Returns:
                Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
            """
        # FIXME
        return False