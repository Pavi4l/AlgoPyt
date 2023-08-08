from pygame import *

window = display.set_mode((500, 500))
picture = transform.scale(image.load('background.png'), (700, 500))
display.set_caption('Зелёный квадрат VS Hero')

#window = display.set_mode((700, 500))
#back = (255, 255, 255)
#window.fill(back)

GREEN = (0, 255, 0)
win_width = 700
win_height = 500


class Card(sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)
player1 = Card(90, 80, 100, 200, GREEN)

class Pic(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
player2 = Pic('hero.png', 200, 300, 300, 100)



run = True
while run:
    time.delay(50)
    window.blit(picture, (0, 0))
    player1.draw()
    player2.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()        