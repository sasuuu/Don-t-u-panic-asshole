import pygame as py


class Game:

    def __init__(self, text, text2):
        self.text = text
        self.text2 = text2

    def printer(self):
        print(self.text + " " + self.text2)


if __name__ == "__main__":
    py.init()
    window = py.display.set_mode((500, 500))
    py.display.set_caption("Don\'t u panic asshole")

    run = True

    while run:
        py.time.delay(100)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
        py.draw.rect(window, (255, 0, 0), (20, 20, 100, 100))
        py.display.update()


