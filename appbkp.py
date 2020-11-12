from flask import Flask, render_template, request, redirect, url_for
#from flask import session
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    items, statuses = get_items()
    return render_template('index.html',items=sorted(items, key=lambda item: item.status),
        statuses=statuses
    )

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]
@app.route('/', methods=['Get'])
def get_items():
    return session.get('items', _DEFAULT_ITEMS)

@app.route('/get', methods=['Get'])
def get_item(id):
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)

@app.route('/add', methods=['Post'])
def add_item(title):
    items = get_items()
    id = items[-1]['id'] + 1 if items else 0
    item = { 'id': id, 'title': title, 'status': 'Not Started' }
    items.append(item)
    session['items'] = items
    return item


@app.route('/update/<int:todo_id>', methods=['Post'])
def save_item(item):
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]
    session['items'] = updated_items
    return item

if __name__ == '__main__':
    app.run()
