from draw.config import Config


def convert_coords(x, y, width, height):
    scaleX = width / abs(Config.borders[0] - Config.borders[1])
    scaleY = height / abs(Config.borders[2] - Config.borders[3])

    return ((x - Config.borders[1]) * scaleX, (Config.borders[2] - y) * scaleY)

def draw_lines(draw, x, y, width, height, color = 'red'):
    radiant = 200
    line_width = 1
    draw.line([(x, 0), (x, height)], fill=color, width=line_width)
    draw.line([(0, y), (width, y)], fill=color, width=line_width)

def draw_point(draw, x, y, color = 'red', size = 10):
    draw.ellipse([(x - size/2, y - size/2), (x + size/2, y + size/2)], fill=color)
