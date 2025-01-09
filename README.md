# Todo API

A RESTful API for managing Todo items. This API allows users to create, update, delete, and retrieve Todo items, with additional features like due dates, priority levels, reminders, and calendar sync.

## Features

- Create, update, delete, and retrieve Todo items.
- Assign due dates and priority levels (Low, Medium, High).
- Set reminders for Todo items.
- Calendar synchronization for better task management.
- JSON-based responses for seamless integration with front-end applications.

## Tech Stack

- **Backend Framework**: Flask
- **Database**: SQLite
- **Deployment**: Render (or Vercel)
- **Dependencies**: Flask-SQLAlchemy, Flask-RESTful, Gunicorn

## API Endpoints

### Base URL
`[[API Deployment URL](https://to-do-api-byab.onrender.com)](https://to-do-api-byab.onrender.com)`

### Endpoints

#### 1. Get All Todos
- **URL**: `/todos`
- **Method**: `GET`
- **Response**:
- 
  [
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Purchase milk, bread, and eggs",
      "completed": false,
      "due_date": "2025-01-05",
      "priority": "High"
    }
  ]
#### 2. Get Todo by ID
- **URL**: /todos/{id}
- **Method**: GET
- **Response**:

{
  "id": 1,
  "title": "Buy groceries",
  "description": "Purchase milk, bread, and eggs",
  "completed": false,
  "due_date": "2025-01-05",
  "priority": "High"
}
#### 3. Create a New Todo
**URL**: /todos
**Method**: POST
**Request Body**:

{
  "title": "Buy groceries",
  "description": "Purchase milk, bread, and eggs",
  "due_date": "2025-01-05",
  "priority": "High",
  "completed": false
}
Response:

{
  "message": "Todo created successfully",
  "id": 1
}
#### 4. Update an Existing Todo
**URL**: /todos/{id}
**Method**: PUT
**Request Body**:

{
  "title": "Buy groceries (updated)",
  "description": "Purchase milk, bread, eggs, and butter",
  "due_date": "2025-01-06",
  "priority": "Medium",
  "completed": true
}
Response:

{
  "message": "Todo updated successfully"
}
#### 5. Delete a Todo
**URL**: /todos/{id}
**Method**: DELETE
**Response**:
{
  "message": "Todo deleted successfully"
}

### Installation Prerequisites
Python 3.8 or higher
SQLite
Steps
Clone the repository:

git clone https://github.com/your-username/todo-api.git
cd todo-api
Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Initialize the database:

flask db init
flask db migrate
flask db upgrade

Run the API locally:
flask run

### Deployment
On Render
Push your repository to GitHub.
Sign in to Render.
Create a new Web Service and connect your GitHub repository.
Use the following build command:

pip install -r requirements.txt
Set the Start Command to:

gunicorn -w 4 -b 0.0.0.0:5000 app:app
Deploy the service.
Usage
You can use tools like Postman or cURL to test the API endpoints.

Example cURL Command

curl -X POST https://your-api-deployment-url.com/todos \
-H "Content-Type: application/json" \
-d '{
  "title": "Buy groceries",
  "description": "Purchase milk, bread, and eggs",
  "due_date": "2025-01-05",
  "priority": "High",
  "completed": false
}'

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
Special thanks to the Flask and SQLite communities for their resources and support.


Let me know if you'd like further refinements!
