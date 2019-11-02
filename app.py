from flask import Flask, send_from_directory, redirect
from draw.draw_map import DrawMap
from draw.config import Config

app = Flask(__name__, static_folder=Config.Paths.assets)

@app.route('/')
def hello():
    return 'DrawMaps works!'

@app.route('/{}/<path:path>'.format(Config.Paths.assets))
def send_js(path):
    return send_from_directory('assets', path)


@app.route('/draw/<user>')
def draw_user_map(user):
    Config.Urls.user = user
    DrawMap()

    return redirect('/' + Config.Paths.get_image_result())


if __name__ == '__main__':
    app.run()

