from frameapi import FrameAPI

def global_middlewares(request):
    print('Global middleware')

app = FrameAPI(middlewares=[global_middlewares])

def local_middlewares(request):
    print('Local middleware')



@app.get('/')
def home(req, res):
    res.send('Welcome to FrameAPI')

@app.get('/users/{id}', middlewares=[local_middlewares])
def get_users(req, res, id):
    res.send(f'Hello {id} user method:GET')

@app.post('/users')
def post_users(req, res):
    res.send('Hello from /users method:POST')



@app.route('/class', middlewares=[local_middlewares])
class User:
    def __init__(self) -> None:
        pass

    def get(req, res):
        res.render('templates/default.html', {'name': 'Admin'})
    