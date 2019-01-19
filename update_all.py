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


player_y = 3
bot_y = 3
ball_x = 1
ball_y = 3
player_score = 0
bot_score = 0
ball_x_direction = "right" #right, left
ball_y_direction = "straight" #up, straight, down


def show_start_screen():
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
  sense.set_pixels(start_screen)
  time.sleep(1)
  #event = sense.stick.wait_for_event()

def show_win_screen():
  sense.show_letter("W", cyan)

def show_lose_screen():
  sense.show_letter("L", yellow)


def update_player():
  for i in range(7):
    sense.set_pixel(0, i, off) #erase
  for i in range(-1, 2):
    sense.set_pixel(0, ( player_y + i), white) #draw
  
def update_bot():
  for i in range(7):
    sense.set_pixel(7, i, off) #erase
  for i in range(-1, 2):
    sense.set_pixel(7, ( bot_y + i), white) #draw

def update_ball():
  for x in range(1,7):
    for y in range(0,7):
      sense.set_pixel(x, y, off) #erase
  sense.set_pixel(ball_x, ball_y, white) # draw

def update_score():
  for i in range(8):
    sense.set_pixel(i, 7, gray) #erase
  for i in range(player_score):
    sense.set_pixel(i, 7, cyan) #draw player score
  for i in range(bot_score):
    sense.set_pixel(7 - i, 7, yellow) #draw bot score


def move_ball():
  global ball_x, ball_y, ball_x_direction, ball_y_direction
  if ball_x_direction == "right":
    if ball_x < 6:
      ball_x += 1
  elif ball_x_direction == "left":
    if ball_x > 1:
      ball_x += -1
  if ball_y_direction == "up":
    if ball_y == 0:
      ball_y += 1
      ball_y_direction = "down"
    else:
      ball_y += -1
  elif ball_y_direction == "down":
    if ball_y == 6:
      ball_y += -1
      ball_y_direction = "up"
    else:
      ball_y += 1

def hit_or_miss():
  global ball_x_direction, ball_y_direction, player_score, bot_score
  if ball_x == 1:
    ball_x_direction = "right"
    if player_y == ball_y:
      ball_y_direction = "straight"
    elif player_y == ball_y + 1:
      ball_y_direction = "up"
    elif player_y == ball_y - 1:
      ball_y_direction = "down"
    else:
      bot_score += 1
      return "miss"
  elif ball_x == 6:
    ball_x_direction = "left"
    if bot_y == ball_y:
      ball_y_direction = "straight"
    elif bot_y == ball_y + 1:
      ball_y_direction = "down"
    elif bot_y == ball_y - 1:
      ball_y_direction = "up"
    else:
      player_score += 1
      return "miss"

def move_bot():
  global bot_y
  if bot_y > ball_y + 1:
    if bot_y > 1:
      bot_y += -1
  if bot_y < ball_y - 1:
    if bot_y < 5:
      bot_y += 1


def set_stage():
  global player_y, ball_x_direction, ball_y_direction
  player_y = 3
  ball_x_direction = "right"
  ball_y_direction = "straight"
  update_player()
  update_bot()
  update_ball()
  update_score()


def pushed_up(event):
    global player_y
    if event.action == ACTION_PRESSED:
      if player_y > 1:
        player_y += -1
        update_player()

def pushed_down(event):
    global player_y
    if event.action == ACTION_PRESSED:
      if player_y < 5:
        player_y += 1
        update_player()

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down

def main():
  sense.clear()
  show_start_screen()
  sense.clear()
  while True:
    set_stage()
    #sense.stick.wait_for_event(emptybuffer=True)
    time.sleep(1)
    while True:
      edge_test = hit_or_miss()
      if edge_test == "miss":
        break
      move_ball()
      update_ball()
      time.sleep(.15)
      move_bot()
      update_bot()
    if player_score == 3:
      sense.clear()
      show_win_screen()
      break
    if bot_score == 3:
      sense.clear()
      show_lose_screen()
      break
  time.sleep(2)
  sense.clear()
  

main()