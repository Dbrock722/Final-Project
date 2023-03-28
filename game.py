#Daniel Brock (un9re) & Jayden Pierre (ntk4nk)


#game idea
#We plan to make some sort of basic platformer similar to geometry dash due to the blocky environment, but also like super mario as it has enemies. The specifics of what we will include in our platformer have yet to be decided but it most likely will be some sort of side scrolling game. We also plan to have around 3 levels for the game for variety

#Basic features and Implementation:
#User input: We plan on implementing user input by having a character the player will control to traverse the various levels in the game. This character will be able to move left right and jump.
#Game over: We plan to make this game loseable by having an enemy or two, or by having various obstacles the player needs to ‘dodge’ to survive, or if the character the player controls falls to their death. We will keep track of potential game over by having lives and once they run out the game is overraphics/Images: We may not use sprite sheets for everything, but we may use some graphics from online for collectables, otherwise we will build everything like the platforms and enemies.
#Additional features:
#Sprite sheets and collectables. We plan to use sprite sheets for our collectables. Our collectables will be kept tally of and essentially work as a scoring system for our game
#Scrolling level: Essentially we plan on making a wide image and then having the camera move across as our character does so that way it gives the illusion of moving, along with having the game end the second our character goes off screen
#Multiple levels. We plan on having three different unique levels for our game that change each time you pass a different one
#Enemies: We plan to create enemies that can hurt the player and increase the difficulty of the game by having them cause the player to lose lives. Upon losing all the lives the game will be over


import uvage


camera = uvage.Camera(800, 600)
p1 = uvage.from_color(100, 588, "red", 30, 30)
pressed_up = False

#the floors we use for the game
floors = [

    uvage.from_color(100, 599, "green", 200, 75),
    uvage.from_color(350, 599, "green", 100, 75),
    uvage.from_color(500, 599, "green", 50, 75),
    uvage.from_color(700, 599, "green", 250, 75),
    uvage.from_color(850, 525, "white", 75, 25),
    uvage.from_color(1025, 500, "white", 75, 25),
    uvage.from_color(1200, 450, "white", 75, 25),
    uvage.from_color(1400, 575, "white", 75, 25),
    uvage.from_color(1600, 599, "green", 175, 75),
    uvage.from_color(1800, 599, "green", 100, 75),
    uvage.from_color(1950, 550, "white", 100, 25),
    uvage.from_color(2100, 500, "white", 75, 25),
    uvage.from_color(2200, 450, "white", 75, 25),
    uvage.from_color(2300, 400, "white", 75, 25),
    uvage.from_color(2600, 599, "green", 200, 50),
    uvage.from_color(2800, 599, "green", 100, 75),
    uvage.from_color(3000, 599, "green", 200, 75),
    uvage.from_color(3150, 550, "white", 75, 25),
    uvage.from_color(3325, 575, "white", 90, 25),
    uvage.from_color(3500, 550, "white", 150, 25),
    uvage.from_color(3650, 500, "white", 75, 25),
    uvage.from_color(3800, 550, "white", 75, 25),
    uvage.from_color(3900, 599, "green", 120, 75),
    uvage.from_color(4100, 550, "orange", 100, 25),
    uvage.from_color(4100, 587, "beige", 25, 50),
    uvage.from_color(4300, 550, "lime", 100, 25),
    uvage.from_color(4300, 587, "beige", 25, 50),
    uvage.from_color(4500, 450, "orange", 100, 25),
    uvage.from_color(4500, 537, "beige", 25, 150),
    uvage.from_color(4700, 450, "lime", 100, 25),
    uvage.from_color(4700, 537, "beige", 25, 150),
    uvage.from_color(4900, 550, "orange", 100, 25),
    uvage.from_color(4900, 587, "beige", 25, 50),
    uvage.from_color(5150, 550, "lime", 200, 25),
    uvage.from_color(5150, 587, "beige", 25, 50),
    uvage.from_color(5400, 550, "orange", 100, 25),
    uvage.from_color(5400, 587, "beige", 25, 50),
    uvage.from_color(5550, 450, "lime", 100, 25),
    uvage.from_color(5550, 537, "beige", 25, 150),
    uvage.from_color(5700, 400, "orange", 100, 25),
    uvage.from_color(5700, 562, "beige", 25, 300),
    uvage.from_color(5850, 450, "lime", 100, 25),
    uvage.from_color(5850, 537, "beige", 25, 150),
    uvage.from_color(6000, 550, "orange", 100, 25),
    uvage.from_color(6000, 587, "beige", 25, 50),


]

borders = uvage.from_color(0, 300, 'light blue', 20, 600)
border2 = uvage.from_color(2000, 300, ' black', 20, 600)
bottom = uvage.from_color(0, 600, 'black', 8000, 20)


score = 0
life = 3
game_on = True
frame = 0
coin_images = uvage.load_sprite_sheet("smallcoin.png", rows=1, columns=6)
flag_image = uvage.load_sprite_sheet("flag.sprite_20.png", rows=1, columns=2)
flag_image2 = uvage.load_sprite_sheet("flag.sprite_20.png", rows=1, columns=2)
flag_image3 = uvage.load_sprite_sheet("flag.sprite_20.png", rows=1, columns=2)
flag3 = uvage.from_image(3900, 544, flag_image3[-1])
flag2 = uvage.from_image(2000, 522, flag_image2[-1])
flag = uvage.from_image(170, 530, flag_image[-1])
coin = uvage.from_image(200, 500, coin_images[-1])

#draws the border to kill you incase you get stuck
def border():
  camera.draw(borders)


#controls the drawing of flags and their animation
def flags():
    global frame
    camera.draw(flag)
    camera.draw(flag2)
    camera.draw(flag3)
    if game_on == True:
        frame += .3
        if frame >= 2:
           frame = 0
        flag.image = flag_image[int(frame)]
        flag2.image = flag_image2[int(frame)]
        flag3.image = flag_image3[int(frame)]
#controls coin animation
def coins():
    global coin_images, coin, frame
    if game_on == True:
        frame += .3
        if frame >= 5:
           frame = 0
        coin.image = coin_images[int(frame)]


#handles the creation of the 3rd level
def level3():
    global score
    global life
    end = uvage.from_color(6040,300,'purple', 20, 600)
    if p1.x >= 3900:
        camera.clear('purple')
        camera.draw(p1)
        camera.draw(flag3)
        camera.draw(uvage.from_text(4100, 200, "Stage 3", 50, 'light blue', bold=True))
        scoring() # draws the scores
        camera.draw(end)
        for i in floors:
            camera.draw(i)
        #stops the camera from moving off the screen
        if p1.x >= 5670:
            camera.move(-6.3, 0)
        #allows for the player to stop moving and reach the end of the game
        if p1.touches(end):
            p1.move_to_stop_overlapping(end)
            camera.clear('light blue')
            camera.draw(uvage.from_text(5650, 300, "You Won!", 50, "Red", bold=True))
            camera.draw(uvage.from_text(5650,200,"Your score was: " + str(score), 50, "Red", bold=True))


def level2():
  global life
  if p1.x >= 2000:
       camera.clear('grey')
       camera.draw(flag2)
       camera.draw(p1)
       camera.draw(uvage.from_text(2200, 200, "Stage 2", 50, 'blue', bold=True))
       camera.move(3.3,0)
       p1.speedx = 3.3
       p1.move_speed()
       coins()
       scoring()
       for i in floors:
          camera.draw(i)
       if life == 0:
          camera.move(-.3, 0)
          p1.speedx = 0
          p1.move_speed()

def dying():
  global borders
  camera.draw(borders)
  global life
  if p1.x < 2000:
      if p1.y >= 600 or camera.x - 400 > p1.x:
        borders.x = 0
        p1.y = 588
        p1.x = 100
        life -= 1
        camera.center = [400, 300]
  elif p1.x >= 2000 and p1.x <= 3899:
      if p1.y >= 600 or camera.x - 400 > p1.x:
        borders.x = 1800
        p1.y = 522.5
        p1.x = 1950
        life -= 1
        camera.center = [2200, 300]
  elif p1.x >= 3900:
      if p1.y >= 600 or camera.x - 400 > p1.x:
          borders.x = 3800
          p1.y = 544
          p1.x = 3850
          camera.center = [3900, 300]
          life -= 1

def game_over():
   global life
   if life <= 0:
       camera.move(0, 0)
       camera.clear("black")
       camera.draw(uvage.from_text(400, 300, "Game Over!", 50, "Red", bold=True))
       p1.speedx = -6.4
       p1.move_speed()
       camera.draw(uvage.from_text(2200, 300, "Game Over!", 50, "Red", bold=True))
       camera.draw((uvage.from_text(4200,300, "Game Over!", 50, "Red", bold=True)))

def movement():
   if life > 0:
    camera.move(3, 0)





def collisions():
  global floors
  for floor in floors:
      camera.draw(floor)
      if p1.touches(floor):
          p1.move_to_stop_overlapping(floor)
          p1.speedy = 0

def player1():
  global floors
  p1.yspeed += 1
  camera.draw(uvage.from_text(500,300, 'press space to jump', 50, 'red', bold=True))

  for i in floors:
    if p1.bottom_touches(i):
        p1.yspeed = 0
        if uvage.is_pressing("space"):
            if p1.x < 2000:
                p1.yspeed = - 18
            if p1.x >= 2000:
                p1.yspeed = - 10
  p1.move_speed()
  p1.xspeed = 3
  if p1.x > 5900:
      p1.xpeed = 0
  camera.draw(p1)

def coin_handling():
   global score

def coin_handling():
   global score
   if p1.touches(coin) and coin.x == 200:
       score += 10
       coin.x += 2000
       coin.y -= 150
   elif p1.x > 300 and coin.x == 200:
       coin.x += 2000
       coin.y -= 150
   if p1.touches(coin) and coin.x == 2200:
       score += 10
       coin.x += 1700
       coin.y += 150
   elif p1.x > 2400 and coin.x == 2200:
       coin.x += 1700
       coin.y += 150
   if p1.touches(coin) and coin.x == 3900:
       score += 10
       coin.x += 500
   elif p1.x > 4000 and coin.x == 3900:
       coin.x += 500
   if p1.touches(coin) and coin.x == 4400:
       score += 10
       coin.x += 850
       coin.y -= 75
   elif p1.x > 4600 and coin.x == 4400:
       coin.x += 850
       coin.y -= 75
   if p1.touches(coin) and coin.x == 5250:
       score += 10
       coin.x += 550
       coin.y -= 50
   elif p1.x > 5300 and coin.x == 5250:
       coin.x += 550
       coin.y -= 50
   if p1.touches(coin) and coin.x == 5800:
       score += 10
       coin.y = 800
   elif p1.x > 5800 and coin.x == 5800:
       coin.y = 800


def scoring():
    global score
    camera.draw(coin)
    score_track = (uvage.from_text(camera.x-210, camera.y - 200, str(score), 50, "Red", bold=True))
    life_track = (uvage.from_text(camera.x - 40, camera.y - 200, str(life), 50, "Red", bold=True))
    name_score = uvage.from_text(camera.x - 300, camera.y - 200, "Score:", 50, "Red",bold=True)
    name_life = uvage.from_text(camera.x - 120, camera.y - 200, "Lives:", 50, "Red", bold=True)
    camera.draw(name_life)
    camera.draw(name_score)
    camera.draw(score_track)
    camera.draw(life_track)
    score_track.move(5,0)
    life_track.move(5,0)


def tick():

 global score
 movement()
 coins()
 camera.clear('light blue')
 flags()
 scoring()
 coin_handling()
 player1()
 collisions()
 #border()
 dying()
 level2()
 level3()
 game_over()
 camera.display()

uvage.timer_loop(30, tick)


