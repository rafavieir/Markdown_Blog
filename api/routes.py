# routes.py
from index import app, flatpages

POST_DIR = 'posts'

@app.route("/")
def index():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    return render_template('posts.html', posts=posts)

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

@app.route('/sobre/')
def sobre():
    return post('sobre')

@app.route('/contato')
def contato():
    return post('contato')
