from draw.config import Config
from draw.ref_utilities import convert_pillow_ref


def draw_lines(draw, x, y, color = 'red'):
    width, height = Config.Variables.width, Config.Variables.height
    x, y = convert_pillow_ref(x, y)
    radiant = 200
    line_width = 1
    draw.line([(x, 0), (x, height)], fill=color, width=line_width)
    draw.line([(0, y), (width, y)], fill=color, width=line_width)

def draw_point(draw, x, y, color = 'red', size = 100):
    width, height = Config.Variables.width, Config.Variables.height
    x, y = convert_pillow_ref(x, y)
    draw.ellipse([(x - size/2, y - size/2), (x + size/2, y + size/2)], fill=color)
