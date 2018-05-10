from flask_lat import app


@app.route('/')
def index():
    return 'No more hello world, please'
