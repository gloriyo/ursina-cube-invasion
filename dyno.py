from ursina import *                    # this will import everything we need from ursina with just one line.
import random                           # Import the random library

random_generator = random.Random()      # Create a random number generator
texoffset = 0.0                         # define a variable that will keep the texture offset
texoffset2 = 0.0                        # define a variable that will keep the texture offset

evil_dirs = []

def update():
    speed = 1
    for entity in cubes:
        entity.rotation_y += time.dt * 5        # Rotate all the cubes every time update is called
    if held_keys['w']:                          # If q is pressed
        cube.y += 1
        # camera.position += (0, time.dt, 0)      # move up vertically
    if held_keys['s']:   
        cube.y -= 1
    if held_keys['d']:                          # If q is pressed
        cube.x += 1
        # camera.position += (0, time.dt, 0)      # move up vertically
    if held_keys['a']:   
        cube.x -= 1

    # for entity in evil_cubes:
    #     if entity.x > 6 or entity.x < -6 or entity.y > 6 or entity.y < -6:
    #         entity.setPos(random.randint(-6, 6), random.randint(-6, 6), 0)
    #     else:

    for i in range(5):
        if evil_cubes[i].x > 6 or evil_cubes[i].x < -6 or evil_cubes[i].y > 6 or evil_cubes[i].y < -6:
            evil_cubes[i].setPos(random.randint(-6, 6), random.randint(-6, 6), 0)
        else:
            # evil_cubes[i].setPos(evil_cubes[i].x + random.randint(-1, 1), evil_cubes[i].y + random.randint(-1, 1), 0)
            dir = evil_cubes[i].direction
            evil_cubes[i].position = dir * 2
    global texoffset                            # Inform we are going to use the variable defined outside
    global texoffset2                           # Inform we are going to use the variable defined outside
    texoffset += time.dt * 0.2                  # Add a small number to this variable
    setattr(cube, "texture_offset", (0, texoffset))    # Assign as a texture offset
    texoffset2 += time.dt * 0.3                        # Add a small number to this variable
    setattr(box, "texture_offset", (0, texoffset2))  # Assign as a texture offset

    if mouse.hovered_entity == cube:
        info.visible = True
    else:
        info.visible = False




def input(key):
    if key == 'space':
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        cube.color = color.rgb(red, green, blue)

    if key == 'c':
        x = random_generator.random() * 10 - 5     # Value between -5 and 5
        y = random_generator.random() * 10 - 5     # Value between -5 and 5
        z = random_generator.random() * 10 - 5     # Value between -5 and 5
        s = random_generator.random() * 1          # Value between 0 and 1
        newcube = Entity(parent=cube, model='cube', color=color.white, position=(x, y, z), scale=(s,s,s), texture="crate")
        cubes.append(newcube)
        '''Create another child cube and add it to the list but using the newcube as the parent, keep the same colour, make it smaller'''
        childcube = Entity(parent=newcube, model='cube', color=color.white, position=(1, 0, 0), scale=(s/2, s/2, s/2), texture="crate")
        cubes.append(childcube)

app = Ursina()

window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Go Fullscreen
window.exit_button.visible = False      # Show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

cubes = []                              # Create the list
cube = Entity(model='cube', color=color.white, scale=(2,2,2), texture="waterfall", collider="box")


# obstacles
evil_cubes = []
evils = 5
for i in range(evils):
    evil_cube = Entity(model='cube', 
                    color=color.red, 
                    scale=(2,2,2), 
                    position=(random.randint(-6, 6), random.randint(-6, 6), 0),
                    direction=(random.randint(-1, 1), random.randint(-1, 1), 0),
                    texture="waterfall", collider="box")
    evil_cubes.append(evil_cube)  
    evil_dirs.append((-1,-1, 0))

box = Entity(model='cube', 
    color=color.rgba(255,255,255,128),
    scale=(2.5,6,2.5), 
    texture="waterfall")
cubes.append(cube)                      # Add the cube to the list
cubes.append(box)                     # Add the cube to the list

Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text="A powerful waterfall roaring on the mountains")
info.x = -0.5
info.y = 0.4
info.background = True
info.visible = False                    # Do not show this text

app.run()                               # opens a window and starts the game.