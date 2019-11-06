from draw.config import Config


def convert_pillow_ref(x, y):
    height = Config.Variables.height
    return x, height - y

def ref_scale(x, y):
    width, height = Config.Variables.width, Config.Variables.height
    scaleX = width / abs(Config.borders[1] - Config.borders[0])
    scaleY = height / abs(Config.borders[3] - Config.borders[2])

    return ((x - Config.borders[0]) * scaleX, (y - Config.borders[2]) * scaleY)


