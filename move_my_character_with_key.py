from pico2d import *

open_canvas(1280, 1024)

character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
running = True

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
speed = 0

# Act 1 : right idle, Act 2 : left idle Act3 : right run, Act 4 : left run
sprite_frame = (
    ((0,300,100,100),(100,300,100,100),(200,300,100,100),(300,300,100,100),(400,300,100,100),(500,300,100,100),(600,300,100,100),(700,300,100,100)),
    ((0,200,100,100),(100,200,100,100),(200,200,100,100),(300,200,100,100),(400,200,100,100),(500,200,100,100),(600,200,100,100),(700,200,100,100)),
    ((0,100,100,100),(100,100,100,100),(200,100,100,100),(300,100,100,100),(400,100,100,100),(500,100,100,100),(600,100,100,100),(700,100,100,100)),
    ((0,0,100,100),(100,0,100,100),(200,0,100,100),(300,0,100,100),(400,0,100,100),(500,0,100,100),(600,0,100,100),(700,0,100,100))
)

def play_Action(Action):
    global running, x, y, frame, dir, speed
    clear_canvas()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(Action[frame][0], Action[frame][1], Action[frame][2], Action[frame][3], x, y, 100, 100)
    update_canvas()
    frame = (frame + 1) % len(Action)
    delay(0.1)

    pass


while True:

    for Action in sprite_frame:
        play_Action(Action)


    pass
