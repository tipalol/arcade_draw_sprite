import arcade
import os


# Константы
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
TITLE = 'wow'

MOVEMENT_SPEED = 5


# Класс игрока, в котором описываем его движение
class Player(arcade.Sprite):

    def update(self):
        # В следующих двух строчках мы меняем текущие координаты
        # прибавляя к ним изменение (которое равно скорости, если клавиша нажата
        # или равно 0, если клавиша не нажата)
        self.center_x += self.change_x
        self.center_y += self.change_y

        # проверка на выход за пределы экрана
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


# класс игрового окна
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # создаем окно с указанными высотой, шириной и названием (конкретные параментры передаем в main)
        super().__init__(width, height, title)

        # следующие две строчки нужны для более легкого импорта картинок
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # список спрайтов, относящихся к игроку
        self.player_list = None

        # спрайт игрока
        self.player_sprite = None

        arcade.set_background_color(arcade.color.WHITE)

    # здесь задаем начальные параметры
    def setup(self):
        self.player_list = arcade.SpriteList()

        # здесь указываем путь к картинке
        self.player_sprite = Player("connor-wassall-skeleton-heavy-img.jpg",
                                    0.5)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    # метод, в котором мы рисуем все, что на экране
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    # метод выполняется каждый кадр и отвечает за обновление экрана
    def on_update(self, delta_time):
        self.player_list.update()

    # метод выполняется по нажатию клавиш
    # если, например, нажата клавиша вправо,
    # то мы устанавливаем change_x на 5 (на movement_speed)
    # и в методе update класса Player изменим x игрока на 5
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    # метод выполянется при оптускании клавиш и обнуляет change x и change y
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()
