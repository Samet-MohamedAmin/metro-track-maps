from PIL import Image, ImageDraw
import urllib.request
import json
from draw.config import Config
from draw.draw_utils import *
from draw.ref_utilities import ref_scale


class DrawMap:
    def __init__(self):
        self.im = Image.open(Config.Paths.image_original)
        self.im_acc = self.im.copy()
        Config.Variables.width, Config.Variables.height = self.im.size

        self.draw = ImageDraw.Draw(self.im)
        self.draw_acc = ImageDraw.Draw(self.im_acc)

        self.import_data()
        self.draw_data()
        self.save_results()

    def import_data(self):
        content = urllib.request.urlopen(Config.Urls.get_coords()).read()
        self.item_list = json.loads(content)

    def draw_data(self):
        w, h = self.im.size

        for item in self.item_list:
            x0, y0 = ref_scale(item['lon'], item['lat'])
            acc = item['acc']
            if(acc < Config.acc_max):
                draw_point(self.draw, x0, y0, size=6)
                draw_point(self.draw_acc, x0, y0, size=acc)

    def save_results(self):
        self.im.save(Config.Paths.get_image_result(), 'JPEG')
        self.im_acc.save(Config.Paths.get_image_result(acc='_acc'), 'JPEG')