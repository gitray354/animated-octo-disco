# Todo List Web App

A simple yet powerful Todo List application built with Python Flask and SQLite database.

## Features

- ✅ Create, read, update, and delete todos
- ✅ Mark todos as completed
- ✅ Add descriptions and due dates to todos
- ✅ Filter todos by completion status
- ✅ RESTful API endpoints
- ✅ SQLite database for data persistence

## Tech Stack

- **Framework**: Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Language**: Python 3.8+

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/gitray354/animated-octo-disco.git
cd animated-octo-disco
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

The app will start at `http://localhost:5000`

## API Endpoints

### Get all todos
```
GET /api/todos
```
Optional query parameter: `?completed=true` or `?completed=false`

**Example Response:**
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "due_date": "2026-02-25T00:00:00",
    "created_at": "2026-02-20T02:52:00",
    "updated_at": "2026-02-20T02:52:00"
  }
]
```

### Create a new todo
```
POST /api/todos
```

**Request Body:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "due_date": "2026-02-25T00:00:00"
}
```

**Note:** Only `title` is required. `description` and `due_date` are optional.

### Get a specific todo
```
GET /api/todos/{id}
```

### Update a todo
```
PUT /api/todos/{id}
```

**Request Body (update any fields):**
```json
{
  "title": "Buy groceries",
  "completed": false,
  "due_date": "2026-02-25T00:00:00"
}
```

### Mark a todo as complete
```
PUT /api/todos/{id}/complete
```

### Delete a todo
```
DELETE /api/todos/{id}
```

## Example Usage

### Create a todo
```bash
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Build a web app"}'
```

### Get all todos
```bash
curl http://localhost:5000/api/todos
```

### Get only completed todos
```bash
curl http://localhost:5000/api/todos?completed=true
```

### Mark todo as complete
```bash
curl -X PUT http://localhost:5000/api/todos/1/complete
```

### Delete a todo
```bash
curl -X DELETE http://localhost:5000/api/todos/1
```

## Project Structure

```
animated-octo-disco/
├── app.py              # Main application file
├── models.py           # Database models (Todo model)
├── requirements.txt    # Python dependencies
├── todos.db           # SQLite database (created automatically)
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── LICENSE            # Apache 2.0 License
```

## Next Steps

- Add a web UI with HTML/CSS templates
- Implement user authentication (multiple users, each with their own todos)
- Add todo categories or tags
- Implement priorities and reminders
- Add API documentation with Swagger/OpenAPI
- Deploy to a cloud platform (Heroku, AWS, etc.)

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

## Support

Need help? Feel free to open an issue on GitHub!

Happy coding! 🚀