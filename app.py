from flask import Flask, render_template, redirect, url_for, request
import os
from todo_app.data import trello_items as trello
#from todo_app.flask_config import Config

app = Flask(__name__)
#app.config.from_object(Config)


@app.route('/')
def index():
    items = trello.get_items()
    statuses = trello.get_lists()
    return render_template('index.html', items = items, statuses = statuses)


@app.route('/create', methods=['POST'])
def add_item():
    name = request.form['title']
    description = request.form['desc']
    due_date = request.form['due']
    trello.add_item(name)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_item_status():
    status_id = request.form['status']
    item_id = request.form['id']
    trello.move_card_to_list_by_id(item_id, status_id)
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete_item(id):
    trello.complete_item(id)
    return redirect(url_for('index'))

@app.route('/remove/<id>')
def remove_item(id):
    # delete item
    return redirect(url_for('index')) 


if __name__ == '__main__':
    app.run()
