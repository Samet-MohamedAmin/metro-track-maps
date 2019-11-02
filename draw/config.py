import os

class Config():
    class Paths():
        assets = 'assets'
        results = '/results'
        image_original = assets + '/maps/original.jpg'

        @staticmethod
        def get_image_result(acc = ''):
            """if acc is specified, then it will return the acc image"""
            return '{}{}/{}{}.jpg'.format(Config.Paths.assets, Config.Paths.results, Config.Urls.user, acc)

        def __init__(self):
            os.mkdir(assets + results)
    
    class Urls():
        user = 'djaj'
        base_coords = 'https://metro-track.herokuapp.com/api/coords/'
        base_result = ''

        @staticmethod
        def get_coords():
            return Config.Urls.base_coords + Config.Urls.user
            



    coords  = (10.1615088, 36.8096696)
    borders = (10.1834, 10.1405, 36.8207, 36.7951)
    acc_max = 200