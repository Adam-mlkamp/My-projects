# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    #draw_oval(canvas, x0, y0, x1, y1)
    # Call the finish_drawing function
    draw_sky(canvas, 0, 0)
    draw_sun(canvas)
    draw_ground(canvas, 0, 0)
    draw_tree(canvas, 240, 290)
    draw_tree(canvas, 600, 290)
    draw_tree(canvas, 300, 290)
    draw_tree(canvas, 500, 290)
    draw_tree(canvas, 400, 290)
    draw_cloud(canvas,0,0)
    draw_cloud(canvas, -100, -50)
    draw_cloud(canvas, 50, 0)
    draw_cloud(canvas, 400, 50)
    draw_cloud(canvas, 350, 100)
    draw_fence(canvas)
    draw_kirby(canvas, 400, 450)
    draw_kirby(canvas, 200, 400)
    draw_kirby(canvas, 700, 350)
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.



def draw_sky(canvas,sky_x,sky_y):
    x1 = sky_x + 800
    y1 = sky_y + 500
    draw_rectangle(canvas, sky_x, sky_y, x1, y1, fill ="light blue", outline="light blue")

def draw_ground(canvas,ground_x,ground_y):
    x1 = ground_x + 800
    y1 = ground_y + 50
    draw_rectangle(canvas, ground_x, ground_y, x1, y1, fill="green", outline="green")

def draw_cloud(canvas,cloud_x,cloud_y):

    x1 = cloud_x + 100
    x2 = x1 + 20
    y1 = cloud_y + 400
    y2 = y1 + 30
    x3 = cloud_x + 200
    y3 = cloud_y + 350
    draw_oval(canvas, x1, y1 , x3, y3,fill="white",outline="white")
    draw_oval(canvas, x2, y2 , x3, y3,fill="white",outline="white")

def draw_fence(canvas):
    x_start = 10
    y_start = 40
    z_start = 25
    for i in range(16):
        draw_rectangle(canvas, x_start, 10, y_start, 150,fill= "white", outline="white")
        draw_polygon(canvas, x_start, 150, y_start, 150, z_start, 175, fill="white",outline="white")
        x_start = x_start + 50
        y_start = y_start + 50
        z_start = z_start + 50

def draw_kirby(canvas,bird_x,bird_y):
    x1 = bird_x - 20
    y1 = bird_y - 20
    x2 = bird_x + 20
    y2 = bird_y + 20
    x3 = x1 + 15
    y3 = y1 + 5
    x4 = x2 - 15
    draw_oval(canvas, x1, y1, x2, y2,fill="pink")
    draw_text(canvas, bird_x, bird_y, "｡ ╹▿╹ ｡",fill="black")
    draw_oval(canvas, x1, y1, x3 , y3,fill="red" )
    draw_oval(canvas, x2, y1,x4 ,y3, fill="red")

def draw_tree(canvas,tree_x,tree_y):
    skirtleft = tree_x - 70
    skirtright = tree_x +70
    skirtbottom = tree_y - 210
    trunkleft = tree_x -10
    trunkright = tree_x + 10
    trunkbottom = tree_y - 260
    draw_rectangle(canvas, trunkleft, trunkbottom, trunkright, skirtbottom, fill="brown",outline="brown")
    draw_polygon(canvas, skirtleft, skirtbottom, tree_x, tree_y, skirtright, skirtbottom,fill="forestGreen",outline="forestGreen")

def draw_sun(canvas):
    draw_oval(canvas, 900, 600, 700, 400, fill="yellow",outline="yellow")

    
# Call the main function so that
# this program will start executing.

main()
