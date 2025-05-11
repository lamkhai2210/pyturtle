import turtle, random, winsound

EY = turtle.Turtle()
window = turtle.Screen()
window.register_shape("UFO80.gif")
window.register_shape("star.gif")
window.register_shape("rocket.gif")
window.register_shape("shield.gif")

score_writer = turtle.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.speed(0)
score_writer.goto(-320, 345)
score_writer.write("Score: 0", font=("Comic Sans MS", 18, "bold"))

EY.penup()

speed_writer = turtle.Turtle()
speed_writer.penup()
speed_writer.hideturtle()
speed_writer.speed(0)
speed_writer.goto(220, 345)
speed_writer.write("Speed: 1", font=("Comic Sans MS", 18, "bold"))

lives_writer = turtle.Turtle()
lives_writer.penup()
lives_writer.hideturtle()
lives_writer.speed(0)
lives_writer.goto(-50, 345)
lives_writer.write("Lives: 3", font=("Comic Sans MS", 18, "bold"))

gameover = turtle.Turtle()
gameover.penup()
gameover.hideturtle()
gameover.color("goldenrod1")
gameover.speed(0)
gameover.goto(-210, 0)

window.setup(width=750, height=800)

rocket = turtle.Turtle()
rocket.speed(0)
rocket.penup()
rocket.shape("rocket.gif")
rocket.penup()

star = turtle.Turtle()
star.speed(0)
star.penup()
star.shape("star.gif")
star.color("yellow")
star.penup()

sheild = turtle.Turtle()
sheild.speed(0)
sheild.penup()
sheild.shape("shield.gif")
sheild.penup()

alien1 = turtle.Turtle()
alien1.speed(0)
alien1.shape("UFO80.gif")
alien1.penup()
alien1.color("red")

alien2 = turtle.Turtle()
alien2.speed(0)
alien2.shape("UFO80.gif")
alien2.penup()
alien2.color("red")

alien3 = turtle.Turtle()
alien3.speed(0)
alien3.shape("UFO80.gif")
alien3.penup()
alien3.color("red")



border = turtle.Turtle()
border.speed(0)
border.pensize(3)
border.color("goldenrod1")
border.hideturtle()
border.penup()
border.goto(-330,-330)
border.pendown()

for i in range(4):
  border.forward(660)
  border.left(90)

window.title("Space WAR")
window.bgcolor("dodgerblue")
window.bgpic("space2.gif")
EY.shape("turtle")

lives = 3
turtlespeed = 1
EY.speed(turtlespeed)
EY.color("lawngreen")

def turnLeft():
  EY.left(15)

def turnRight():
  EY.right(15)
  
def addSpeed():
  global turtlespeed
  if turtlespeed < 10:  
    turtlespeed += 1
    EY.speed(turtlespeed)
    speed_writer.clear()
    speed_writer.write(f"Speed: {turtlespeed}", font = ("Comic Sans MS", 18, "bold"))

def decSpeed():
  global turtlespeed
  if turtlespeed > 1:
    turtlespeed -= 1
    EY.speed(turtlespeed)
    speed_writer.clear()
    speed_writer.write(f"Speed: {turtlespeed}", font = ("Comic Sans MS", 18, "bold"))


def checkBorder():
  if EY.xcor() > 320 or EY.xcor() < -320 or EY.ycor() > 320 or EY.ycor() < -320:
    return True
  else: 
    return False


def moveStar():
  x = random.randint(-300, 300)
  y = random.randint(-300, 300)
  star.goto(x,y)

def moveAlien(alien):
  x = random.randint(-300, 300)
  y = random.randint(-300, 300)
  alien.goto(x,y)

def reset():
  EY.speed(0)
  global turtlespeed
  turtlespeed = 1
  EY.goto(0,0)
  EY.speed(turtlespeed)

score = 0

def collideStar():
  if abs(EY.xcor() - star.xcor()) <= 25 and abs(EY.ycor() - star.ycor()) <= 25:
    return True
  else:
    return False

def collideRocket():
  if abs(EY.xcor() - rocket.xcor()) <= 40 and abs(EY.ycor() - rocket.ycor()) <= 40:
    return True
  else:
    return False

def collideAlien(alien):
  if abs(EY.xcor() - alien.xcor()) <= 40 and abs(EY.ycor() - alien.ycor()) <= 40:
    return True
  else:
    return False

moveStar()
moveAlien(alien1)  
moveAlien(alien2)
moveAlien(alien3)   
moveAlien(rocket) 
startgame = True

while startgame:
  EY.forward(4)
  turtle.listen()

  if checkBorder():
    EY.speed(10)
    EY.left(180)
    winsound.PlaySound("Low Boing.wav", winsound.SND_ASYNC)
    EY.speed(turtlespeed)

  if collideStar():
    aliens = [alien1, alien2, alien3]
    moveStar()
    moveAlien(aliens[random.randint(0,2)])
    score += 1
    winsound.PlaySound("Collect.wav", winsound.SND_ASYNC)
    score_writer.clear()
    score_writer.write(f"Score: {score}", font = ("Comic Sans MS", 18, "bold"))
 
  if collideRocket():
    aliens = [alien1, alien2, alien3]
    moveAlien(rocket)
    moveAlien(aliens[random.randint(0,2)])
    lives += 1
    winsound.PlaySound("Magic Spell.wav", winsound.SND_ASYNC)
    lives_writer.clear()
    lives_writer.write(f"Lives: {lives}", font = ("Comic Sans MS", 18, "bold"))

  if collideAlien(alien1):
    moveAlien(alien1)
    lives-=1
    winsound.PlaySound("Bonk2.wav", winsound.SND_ASYNC)
    lives_writer.clear()
    lives_writer.write(f"Lives: {lives}", font = ("Comic Sans MS", 18, "bold"))

  if collideAlien(alien2):
      moveAlien(alien2)
      lives-=1
      winsound.PlaySound("Bonk2.wav", winsound.SND_ASYNC)
      lives_writer.clear()
      lives_writer.write(f"Lives: {lives}", font = ("Comic Sans MS", 18, "bold"))
 
  if collideAlien(alien3):
    moveAlien(alien3)
    lives-=1
    winsound.PlaySound("Bonk2.wav", winsound.SND_ASYNC)
    lives_writer.clear()
    lives_writer.write(f"Lives: {lives}", font = ("Comic Sans MS", 18, "bold"))
 
  if lives == 0:
    gameover.write("GAME OVER", font=("Comic Sans MS", 50, "bold"))
    startgame = False

  turtle.onkey(turnLeft, "a")
  turtle.onkey(turnRight, "d")
  turtle.onkey(addSpeed, "Up")
  turtle.onkey(decSpeed, "Down")
  turtle.onkey(reset, "space")


turtle.mainloop()