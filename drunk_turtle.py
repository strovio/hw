import turtle as tl

tl.speed(0)
tl.delay(0)

def draw_fractal(scale):
    if scale >= 5:
        draw_fractal(scale / 3.0)
        tl.left(12)
        draw_fractal(scale / 1.5)
        tl.right(66)
        draw_fractal(scale / 4.0)
        tl.left(108)
        draw_fractal(scale / 2.5)
    else:
        tl.forward(scale)

scale = 400
tl.pensize(2)
tl.penup()
tl.goto(-scale, -scale/4)
tl.pendown()

draw_fractal(scale)
tl.done()