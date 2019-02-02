from sense_hat import SenseHat, ACTION_PRESSED
import time
import random

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


p = red
o = cyan
n = yellow
g = green
_ = off
start_screen = [
  p, p, p, p, o, o, o, o,
  p, _, _, p, o, _, _, o,
  p, p, p, p, o, _, _, o,
  p, _, _, _, o, o, o, o,
  n, _, _, n, g, g, g, g,
  n, n, _, n, g, _, _, _,
  n, _, n, n, g, _, g, g,
  n, _, _, n, g, g, g, g
]

s = green
win_screen = [
  _, _, s, s, s, s, _, _,
  _, s, _, _, _, _, s, _,
  s, _, s, _, _, s, _, s,
  s, _, _, _, _, _, _, s,
  s, _, s, _, _, s, _, s,
  s, _, _, s, s, _, _, s,
  _, s, _, _, _, _, s, _,
  _, _, s, s, s, s, _, _
]

f = red
lose_screen = [
  _, _, f, f, f, f, _, _,
  _, f, _, _, _, _, f, _,
  f, _, f, _, _, f, _, f,
  f, _, _, _, _, _, _, f,
  f, _, _, _, _, _, _, f,
  f, _, f, f, f, f, _, f,
  _, f, _, _, _, _, f, _,
  _, _, f, f, f, f, _, _
]

game_display = ( [off] * 8 * 7 ) + ( [gray] * 8 )


# game_display = ( [off] * 8 * 7 ) + ( [gray] * 8 )


# bot_y = 3
# ball_x = 1
# ball_y = 3
# player_score = 0
# bot_score = 0
# ball_x_direction = "right" #right, left
# ball_y_direction = "straight" #up, straight, down


class Paddle:
    def __init__(self, start_x, start_y, color, score_color):
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
        self.score_color = score_color
        self.x = start_x
        self.y = start_y
        self.score = 0

player = Paddle(0, 3, white, green)
bot = Paddle(7, 3, white, red)

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
        if self.x == 0:
            bot_score += 1
            return "score"
        elif self.x == 7:
            player_score += 1
            return "score"
        else:
            if self.y == 0 or self.y == 6:
                self.vel_y *= -1
            elif game_display[ ( self.x + self.vel_x ) + ( ( self.y + self.vel_x ) * 8 ) ] == white:
                self.vel_x *= -1
                self.vel_y = random.randint(-1, 1)
            self.x += self.vel_x
            self.y += self.vel_y

ball = Ball(1, 3, white)


# def show_start_screen():
#   p = red
#   o = cyan
#   n = yellow
#   g = green
#   _ = off
#   start_screen = [
#     p, p, p, p, o, o, o, o,
#     p, _, _, p, o, _, _, o,
#     p, p, p, p, o, _, _, o,
#     p, _, _, _, o, o, o, o,
#     n, _, _, n, g, g, g, g,
#     n, n, _, n, g, _, _, _,
#     n, _, n, n, g, _, g, g,
#     n, _, _, n, g, g, g, g
#   ]
#   sense.set_pixels(start_screen)
#   time.sleep(1)
#   #event = sense.stick.wait_for_event()

# def show_win_screen():
#   sense.show_letter("W", cyan)

# def show_lose_screen():
#   sense.show_letter("L", yellow)


def set_game_pixel(x, y, color):
    global game_display
    game_display[ x + ( y * 8 ) ] = color

def update_game_display():
    global game_display
    game_display = ( [off] * 8 * 7 ) + ( [gray] * 8 )
    for i in [-1, 0, 1]:
        set_game_pixel(player.x + 1, player.y + i, color)
        set_game_pixel(bot.x - 1, bot.y + 1, bot.color)
    set_game_pixel(ball.x, ball.y, ball.color)
    for i in range(player.score):
        set_game_pixel(i, 7, player.score_color)
    for i in range(bot.score):
        set_game_pixel(7 - i, 7, bot.score_color)

# def update_player():
#   for i in range(7):
#     sense.set_pixel(0, i, off) #erase
#   for i in range(-1, 2):
#     sense.set_pixel(0, ( player_y + i), white) #draw

#def update_bot():
#   for i in range(7):
#     sense.set_pixel(7, i, off) #erase
#   for i in range(-1, 2):
#     sense.set_pixel(7, ( bot_y + i), white) #draw

# def update_ball():
#   for x in range(1,7):
#     for y in range(0,7):
#       sense.set_pixel(x, y, off) #erase
#   sense.set_pixel(ball_x, ball_y, white) # draw

# def update_score():
#   for i in range(8):
#     sense.set_pixel(i, 7, gray) #erase
#   for i in range(player_score):
#     sense.set_pixel(i, 7, cyan) #draw player score
#   for i in range(bot_score):
#     sense.set_pixel(7 - i, 7, yellow) #draw bot score




# def move_ball():
#   global ball_x, ball_y, ball_x_direction, ball_y_direction
#   if ball_x_direction == "right":
#     if ball_x < 6:
#       ball_x += 1
#   elif ball_x_direction == "left":
#     if ball_x > 1:
#       ball_x += -1
#   if ball_y_direction == "up":
#     if ball_y == 0:
#       ball_y += 1
#       ball_y_direction = "down"
#     else:
#       ball_y += -1
#   elif ball_y_direction == "down":
#     if ball_y == 6:
#       ball_y += -1
#       ball_y_direction = "up"
#     else:
#       ball_y += 1

# def hit_or_miss():
#   global ball_x_direction, ball_y_direction, player_score, bot_score
#   if ball_x == 1:
#     ball_x_direction = "right"
#     if player_y == ball_y:
#       ball_y_direction = "straight"
#     elif player_y == ball_y + 1:
#       ball_y_direction = "up"
#     elif player_y == ball_y - 1:
#       ball_y_direction = "down"
#     else:
#       bot_score += 1
#       return "miss"
#   elif ball_x == 6:
#     ball_x_direction = "left"
#     if bot_y == ball_y:
#       ball_y_direction = "straight"
#     elif bot_y == ball_y + 1:
#       ball_y_direction = "down"
#     elif bot_y == ball_y - 1:
#       ball_y_direction = "up"
#     else:
#       player_score += 1
#       return "miss"

# def move_bot():
#   global bot_y
#   if bot_y > ball_y + 1:
#     if bot_y > 1:
#       bot_y += -1
#   if bot_y < ball_y - 1:
#     if bot_y < 5:
#       bot_y += 1


def start_round():
    player.x = player.start_x
    player.y = player.start_y
    bot.x = bot.start_x
    bot.y = bot.start_y
    ball.x = ball.start_x
    ball.y = ball.start_y
    ball.vel_x = 1
    ball.vel_y = random.randint(-1, 1)
    update_game_display()

# def set_stage():
#   global player_y, ball_x_direction, ball_y_direction
#   player_y = 3
#   ball_x_direction = "right"
#   ball_y_direction = "straight"
#   update_player()
#   update_bot()
#   update_ball()
#   update_score()


def pushed_up(event):
    if event.action == ACTION_PRESSED:
      if player.y > 1:
        player.y += -1

def pushed_down(event):
    if event.action == ACTION_PRESSED:
      if player.y < 5:
        player.y += 1

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down

def main():
    sense.clear()
    sense.set_pixels(start_screen)
    time.sleep(1.5)
    sense.clear()
    while True:
        start_round()
        while True:
            if ball.move() == "score":
                break
        if player.score == 3:
            sense.clear()
            sense.set_pixels(win_screen)
        elif bot.score == 3:
            sense.clear()
            sense.set_pixels(lose_screen)
        else:
            time.sleep(.1)

main()

# def main():
#   sense.clear()
#   show_start_screen()
#   sense.clear()
#   while True:
#     set_stage()
#     #sense.stick.wait_for_event(emptybuffer=True)
#     time.sleep(1)
#     while True:
#       edge_test = hit_or_miss()
#       if edge_test == "miss":
#         break
#       move_ball()
#       update_ball()
#       time.sleep(.15)
#       move_bot()
#       update_bot()
#     if player_score == 3:
#       sense.clear()
#       show_win_screen()
#       break
#     if bot_score == 3:
#       sense.clear()
#       show_lose_screen()
#       break
#   time.sleep(2)
#   sense.clear()
#
# main()
