import pygame as pg

pg.init()

is_jump = False
jump_counter = 2

class Circle:
    def __init__(self, color, circle_radius, x, y, speed):
        self.color = color
        self.circle_radius = circle_radius
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self):
        pg.draw.circle(win, self.color, (self.x, self.y), self.circle_radius)

    def move_by_kyes(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x -= self.speed
        elif keys[pg.K_RIGHT]:
            self.x += self.speed
        elif keys[pg.K_UP]:
            self.y -= self.speed
        elif keys[pg.K_DOWN]:
            self.y += self.speed


height = 500
wight = 500
win = pg.display.set_mode((wight, height))
circle1 = Circle('yellow', 20, 250, 250, 2)

circle100 = []
x = 0
for i in range(100):
    a = Circle('yellow', 20, x, 250, 2)
    circle100.append(a)
    x += 100
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    win.fill((255, 255, 255))
    circle1.move_by_kyes()
    circle1.draw()
    pg.display.update()
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        is_jump = True

    if is_jump is True:
        if jump_counter >= -30:
            circle1.y -= jump_counter
            jump_counter -= 2
        else:
            jump_counter = 30
            is_jump = False

    for i in circle100:
        i.draw()
    pg.display.update()

    pg.time.delay(10)