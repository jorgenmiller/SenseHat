from sense_hat import SenseHat, ACTION_PRESSED
import time

sense = SenseHat()
sense.clear()


white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
cyan = [0, 255, 255]
pink = [255, 0, 255]
yellow = [255, 255, 0]
gray = [100, 100, 100]
off = [0, 0, 0]

game_display = ( [off] * 8 * 7 ) + ( [gray] * 8 )

def set_game_pixel(x, y, color):
    global game_display
    game_display[ x + ( y * 8 ) ] = color

def update_game_display():
    global game_display
    game_display = ( [off] * 8 * 7 ) + ( [gray] * 8 )
    #for i in [-1, 0, 1]:
    #    set_game_pixel(player.x + 1, player.y + i, color)
    #    set_game_pixel(bot.x - 1, bot.y + 1, bot.color)
    set_game_pixel(ball.x, ball.y, ball.color)
    #for i in range(palyer.score):
    #    set_game_pixel(i, 7, player.score_color)
    #for i in range(bot.score):
    #    set_game_pixel(7 - i, 7, bot.score_color)

class Ball:
    def __init__(self, start_x, start_y, color):
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
        self.x = start_x
        self.y = start_y
        self.vel_x = 0
        self.vel_y = 0
    def move(self):
        if self.y == 0 or self.y == 6:
            self.vel_y *= -1
        if self.x == 0:
          #bot_score += 1
          #start_round()
          print("score!")
          self.vel_x *= -1
        elif self.x == 7:
          #player_score += 1
          #start_round()
          print("score!")
          self.vel_x *= -1
        elif not game_display[ ( self.x + self.vel_x ) + ( ( self.y + self.vel_x ) * 8 ) ] in [off, gray] :
            print("collsision")
        self.x += self.vel_x
        self.y += self.vel_y

ball = Ball(1, 3, white)
ball.vel_x = 1
ball.vel_y = 1

while True:
  sense.clear()
  ball.move()
  update_game_display()
  sense.set_pixels(game_display)
  time.sleep(.1)
