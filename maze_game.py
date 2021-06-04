import pgzrun
import random

WIDTH = 700
HEIGHT = 700

TITLE = "FTC GAME"

wall_colour = (0,0,100)
background_colour = (0,0,0)

walls = [ Rect(0,0,WIDTH,20),Rect(WIDTH-20,0,20,HEIGHT), Rect(0, HEIGHT-20, WIDTH, 20),
          Rect(0,0,20,HEIGHT), Rect(80,80,40,140), Rect(80,280,140,40), Rect(80,280,40,140),
          Rect(80,480,40,140), Rect(80,580,140,40), Rect(180,0,40,120), Rect(180,180,40,140),
          Rect(180,380,40,140), Rect(280,80,40,240), Rect(280,280,140,40), Rect(280,380,40,320),
          Rect(380,80,240,40), Rect(380,80,40,140), Rect(380,280,40,340), Rect(380,480,140,40),
          Rect(480,180,220,40), Rect(480,180,40,140), Rect(480,380,140,40), Rect(480,580,140,40),
          Rect(580,280,40,140), Rect(580,480,120,40) ]
tablets = []
for x in range(7):
    for y in range(7):
        tablets.append(Rect(x*100+40, y*100+40, 20, 20))
del tablets[24]

ghosts = []
ghosts.append(Actor("monster", center=(50, 50)))
ghosts[0].direction = "S"
ghosts.append(Actor("monster", center=(650, 50)))
ghosts[1].direction = "W"
ghosts.append(Actor("monster", center=(50, 650)))
ghosts[2].direction = "N"
ghosts.append(Actor("monster", center=(650, 650)))
ghosts[3].direction = "W"

score = 0
lives = 5
game_over = False
player = Actor("player1", center = (350, 350))

def draw():
    if game_over:
        screen.fill((0, 0, 0))
        screen.draw.text("Game over", color=(190, 190, 190), center=(WIDTH/2, HEIGHT/2 - 40))
        Screen.draw.text("You scored {}".format(score), color=(190,190,190), center=(WIDTH/2, HEIGHT/2))
        screen.draw.text("Click in the window to play again! ", color=(190, 190, 190), center=(WIDTH/2, HEIGHT/2))
    else:
        screen.fill(background_colour)
        for wall in walls:
            screen.draw.filled_rect(wall, wall_colour)
        for tablet in tablets:
            screen.draw.filled_rect(tablet, (255, 235, 222))
        for ghost in ghosts:
            ghost.draw()
        player.draw()
        screen.draw.text("Score : {}".format(score), color=(190, 190, 190), topleft=(3,3))
        screen.draw.text("Lives: {}".format(lives), color=(190, 190, 190), topright=(WIDTH-3,3))
        
def update():
    global lives
    global score
    global game_over
    if not game_over:
        old_x, old_y = player.center
        if keyboard.up:
            player.y = player.y -5
        if keyboard.down:
            player.y = player.y + 5
        if keyboard.left:
            player.x = player.x - 5
        if keyboard.right:
            player.x = player.x + 5
        if player.collidelist(walls) != -1:
            player.center = old_x, old_y
        result = player.collidelist(tablets)
        if result != -1:
            del tablets[result]
            score = score + 10
        if player.collidelist(ghosts) != -1:
            lives = lives - 1
            player.center = (350, 350)
        update_ghosts()
        if lives < 1 :
            game_over = True
        if len(tablets) == 0:
            next_level()
            
    
def update_ghosts():
    for ghost in ghosts:
        direction = ghost.direction
        old_x, old_y = ghost.x, ghost.y
        if direction == "N":
            ghost.y = ghost.y - 5
        elif direction == "E":
            ghost.x = ghost.x + 5
        elif direction == "S":
            ghost.y = ghost.y + 5
        else:
            ghost.x = ghost.x - 5
        if ghost.collidelist(walls) != -1:
            ghost.center = old_x, old_y
            ghost.direction = random.choice(["N", "E", "S", "W"])
            
def on_mouse_down():
    if game_over:
        reset()
        
def reset():
    global score
    global game_over
    global lives
    score = 0
    lives = 5
    game_over = False
    player.center = (350, 350)
    reset_ghosts()
    reset_tablets()
    
def reset_ghosts():
    ghosts[0].center = (50, 50)
    ghosts[1].center = (650, 50)
    ghosts[2].center = (50, 650)
    ghosts[3].center = (650, 650)
    
def reset_tablets():
    tablets.clear()
    for x in range(7):
        for y in range(7):
            tablets.append(Rect(x*100+40, y*100+40, 20, 20))
    del tablets[24]
    
def next_level():
    global lives
    player.center = (350, 350)
    reset_ghosts()
    reset_tablets()
    lives = lives + 1
pgzrun.go()


















