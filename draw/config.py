import os

class Config():
    class Path():
        assets = './assets'
        results = '/results'
        image_original = assets + '/maps/original.jpg'
        image_result = assets + results + '/bla.jpg'
        image_acc_result = assets + results + '/bla_acc.jpg'
        url_coords = 'https://metro-track.herokuapp.com/api/coords/djaj'

        def __init__(self):
            os.mkdir(assets + results)
            



    coords  = (10.1615088, 36.8096696)
    borders = (10.1834, 10.1405, 36.8207, 36.7951)
    acc_max = 200