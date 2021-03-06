from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', 
        items=sorted(session.get_items(), key=lambda item: item['status'], reverse=True))

@app.route('/create', methods=['POST'])
def create():
    session.add_item(request.form['title'])
    return index()

@app.route('/update', methods=['POST'])
def update():
    for id in request.form:
        item = session.get_item(id)
        item['status'] = 'Complete'
        session.save_item(item)
    return index()

@app.route('/remove/<id>')
def remove(id):
    session.remove_item(id)
    return index()

if __name__ == '__main__':
    app.run()