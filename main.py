from utils import load_candidates, get_all, get_by_pk, get_by_skill
from flask import Flask

list_candidates = get_all(load_candidates('candidates.json'))

app = Flask(__name__)

@app.route("/")
def index():
    str = '<pre>'
    for i in list_candidates:
        str += f'{i} \n \n'
    str += '</pre>'
    return str

@app.route('/candidates/<int:pk>')
def get_man(pk):
    man = get_by_pk(pk, list_candidates)
    if man:
        str = f'<img scr = "{man.picture}">'
        str += f'<pre> {man} </pre>'
    else:
        str = "Not found"
    return str

@app.route('/skills/<x>')
def get_mans(x):
    x = x.lower()
    mans = get_by_skill(x, list_candidates)
    if mans:
        str = '<pre>'
        for i in mans:
            str += f'{i} \n \n'
        str += '</pre>'
    else:
        str = 'Not found'
    return str

if __name__ == '__main__':
    app.run(port = 5000)

