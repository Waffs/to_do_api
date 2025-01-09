from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todos.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import the Todo model
from models import Todo

# Initialize the database
with app.app_context():
    db.create_all()

# API Endpoints
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    new_todo = Todo(
        title=data['title'],
        description=data.get('description'),
        due_date=datetime.strptime(data['due_date'], '%Y-%m-%d') if data.get('due_date') else None,
        priority=data.get('priority', 'Medium'),
        completed=data.get('completed', False)
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.json
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d') if data.get('due_date') else todo.due_date
    todo.priority = data.get('priority', todo.priority)
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify(todo.to_dict())

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
