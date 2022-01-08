from app import app
x=5
@app.route('/')
@app.route('/index')
def index():
    return "hello world"
