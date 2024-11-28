import tkinter
import random


class SnakeGame:
    def __init__(self, master): #настройки игры
        self.master = master
        self.master.title('Змейка')

        self.canvas = tkinter.Canvas(master, width=400, height=400, bg='black')
        self.canvas.pack()

        self.snake = [(200, 200), (190, 200), (180, 200)]
        self.direction = 'Right'
        self.food_position = self.place_food()

        self.scope = 0
        self.game_over = False

        self.score_text = self.canvas.create_text(
            50, 10, text=f'Счет: {self.scope}', fill='white', font=('Arial', 12)
        )
        self.master.bind("<Key>", self.change_direction)
        self.update()

    def place_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return x, y

    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = ['Up', 'Down', 'Left', 'Right']
        opposites = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        if new_direction in all_directions and new_direction != opposites[self.direction]:
            self.direction = new_direction

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == 'Up':
            head_y -= 10
        elif self.direction == 'Down':
            head_y += 10
        elif self.direction == 'Left':
            head_x -= 10
        elif self.direction == 'Right':
            head_x += 10

        new_head = (head_x, head_y)

        if (
            head_x < 0
            or head_x >= 400
            or head_y < 0
            or head_y >= 400
            or new_head in self.snake
        ):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food_position:
            self.food_position = self.place_food()
            self.scope += 1
            self.canvas.itemconfig(self.score_text, text=f'Счет: {self.scope}')
        else:
            self.snake.pop()

    def update(self):
        if not self.game_over:
            self.move_snake()
            self.draw()
            self.master.after(100, self.update)
        else:
            self.canvas.create_text(
                200, 200, text='Игра окончена', fill='white', font=('Arial', 24)
            )

    def draw(self):
        self.canvas.delete('all')
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='green')

        food_x, food_y = self.food_position
        self.canvas.create_oval(food_x, food_y, food_x + 10, food_y + 10, fill='red')

        self.canvas.create_text(
            50, 10, text=f'Счет: {self.scope}', fill='white', font=('Arial', 12)
        )


root = tkinter.Tk()
game = SnakeGame(root)
root.mainloop()
