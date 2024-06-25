# Flask Blog Application

## Overview

This Flask Blog Application is designed to provide users with the ability to create, edit, and delete blog posts. The application leverages Flask for the web framework, SQLAlchemy for database management, and Flask-WTF for form handling. Custom error handling for 404 and 500 errors is also implemented to enhance the user experience.

## Features

- **Create, Edit, and Delete Blog Posts**: Users can create new blog posts, edit existing ones, and delete posts they no longer need.
- **Form Handling**: The application uses Flask-WTF for secure and user-friendly form management.
- **Database Management**: SQLAlchemy is used for efficient and scalable database operations.
- **Custom Error Handling**: Customized error pages for 404 (Not Found) and 500 (Internal Server Error) enhance the robustness of the application.

## Project Structure

- `app.py`: The main application file that sets up and runs the Flask application.
- `Create_db.py`: Script for initializing the database.
- `create_tables.py`: Script for creating necessary database tables.
- `Databases.py`: Contains database-related configurations and operations.
- `Models.py`: Defines the database models used in the application.
- `WebForms.py`: Contains form definitions used for creating and editing blog posts.

## Installation

To set up and run the Flask Blog Application, follow these steps:

1. **Clone the repository**:
   ```bash
   https://github.com/an90ass/Blog-Post-Manager.git
   cd <repository_directory>
2. **Create a virtual environment**:
    ```bash
    python -m venv venv
3. **Activate the virtual environment**:
   - On Windows:
    bash    
    venv\Scripts\activate

  - On macOS/Linux:
    bash
    source venv/bin/activate
4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
5. **Initialize the database**:
    ```bash
    python Create_db.py
    python create_tables.py
6. **Run the application:**
   ```bash
   flask run
## Usage
Once the application is running, you can access it via your web browser at http://localhost:5000. From there, you can create, edit, and delete blog posts using the provided forms.
   

    
    


   

   
