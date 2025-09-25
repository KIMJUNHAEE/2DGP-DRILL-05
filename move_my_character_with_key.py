from pico2d import *

open_canvas(1280, 1020)

character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')

KPU_WIDTH, KPU_HEIGHT = 1280, 1020
running = True

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
Act = 1

move_left = False
move_right = False
move_up = False
move_down = False

# Act 1 : right idle, Act 2 : left idle Act3 : right run, Act 4 : left run
sprite_frame = (
    ((0,300,100,100),(100,300,100,100),(200,300,100,100),(300,300,100,100),(400,300,100,100),(500,300,100,100),(600,300,100,100),(700,300,100,100)),
    ((0,200,100,100),(100,200,100,100),(200,200,100,100),(300,200,100,100),(400,200,100,100),(500,200,100,100),(600,200,100,100),(700,200,100,100)),
    ((0,100,100,100),(100,100,100,100),(200,100,100,100),(300,100,100,100),(400,100,100,100),(500,100,100,100),(600,100,100,100),(700,100,100,100)),
    ((0,0,100,100),(100,0,100,100),(200,0,100,100),(300,0,100,100),(400,0,100,100),(500,0,100,100),(600,0,100,100),(700,0,100,100))
)

def play_Action(Action):
    global running, x, y, frame, dir
    clear_canvas()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(Action[frame][0], Action[frame][1], Action[frame][2], Action[frame][3], x, y, Action[frame][2], Action[frame][3])
    update_canvas()
    frame = (frame + 1) % len(Action)
    delay(0.02)
    pass


def handle_events():
    global running, dir, x, y, move_up, move_down, move_left, move_right, Act

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                move_right = True
            elif event.key == SDLK_LEFT:
                move_left = True
            elif event.key == SDLK_UP:
                move_up = True
            elif event.key == SDLK_DOWN:
                move_down = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                move_right = False
                Act = 1
            elif event.key == SDLK_LEFT:
                move_left = False
                Act = 2
            elif event.key == SDLK_UP:
                move_up = False
                Act = 1
            elif event.key == SDLK_DOWN:
                move_down = False
                Act = 2

    pass


while running:
    handle_events()

    if move_right:
        dir = 1
        Act = 3
    elif move_left:
        dir = -1
        Act = 4
    elif move_up:
        dir = 1
        Act = 3
    elif move_down:
        dir = -1
        Act = 4

    if move_right or move_left:
        if x + 50 < KPU_WIDTH and x-50 > 0:
            x += dir * 10
        elif x + 50 >= KPU_WIDTH:
            x = KPU_WIDTH - 60
        elif x - 50 <= 0:
            x = 60
    elif move_up or move_down:
        if y + 50 < KPU_HEIGHT and y-50 > 0:
            y += dir * 10
        elif y + 50 >= KPU_HEIGHT:
            y = KPU_HEIGHT - 60
        elif y - 50 <= 0:
            y = 60

    if Act == 1:
        Action_frame = sprite_frame[0]
    elif Act == 2:
        Action_frame = sprite_frame[1]
    elif Act == 3:
        Action_frame = sprite_frame[2]
    elif Act == 4:
        Action_frame = sprite_frame[3]

    play_Action(Action_frame)


    pass
