# Flask Blog Application

## Overview

This Flask Blog Application is designed to provide users with the ability to create, edit, and delete blog posts. The application leverages Flask for the web framework, SQLAlchemy for database management, and Flask-WTF for form handling. Custom error handling for 404 and 500 errors is also implemented to enhance the user experience.

## Features

- **Create, Edit, and Delete Blog Posts**: Users can create new blog posts, edit existing ones, and delete posts they no longer need.
- **Form Handling**: The application uses Flask-WTF for secure and user-friendly form management.
- **Database Management**: SQLAlchemy is used for efficient and scalable database operations.
- **Custom Error Handling**: Customized error pages for 404 (Not Found) and 500 (Internal Server Error) enhance the robustness of the application.

  ## Endpoints

### Home Page
- **URL:** `/`
- **Method:** `GET`
- **Description:** Displays the home page.

### Add User
- **URL:** `/users/add`
- **Method:** `GET`, `POST`
- **Description:** Adds a new user.

### Update User
- **URL:** `/update/<int:id>`
- **Method:** `GET`, `POST`
- **Description:** Updates user information.

### Delete User
- **URL:** `/delete/<int:id>`
- **Method:** `GET`
- **Description:** Deletes a user.

### Add Post
- **URL:** `/add-post`
- **Method:** `GET`, `POST`
- **Description:** Adds a new blog post.

### View Posts
- **URL:** `/posts`
- **Method:** `GET`
- **Description:** Displays all blog posts.

### View Single Post
- **URL:** `/post/<int:id>`
- **Method:** `GET`
- **Description:** Displays a single blog post.

### Edit Post
- **URL:** `/posts/edit/<int:id>`
- **Method:** `GET`, `POST`
- **Description:** Edits a blog post.

### Delete Post
- **URL:** `/posts/delete/<int:id>`
- **Method:** `GET`
- **Description:** Deletes a blog post.

### Login
- **URL:** `/login`
- **Method:** `GET`, `POST`
- **Description:** User login page.

### Dashboard
- **URL:** `/dashboard`
- **Method:** `GET`, `POST`
- **Description:** User dashboard.

### Logout
- **URL:** `/logout`
- **Method:** `GET`, `POST`
- **Description:** Logs out the user.

### Admin Page
- **URL:** `/admin`
- **Method:** `GET`
- **Description:** Admin page, accessible only by the admin user.

### Search
- **URL:** `/search`
- **Method:** `POST`
- **Description:** Search for blog posts.

### Custom Error Pages
- **404 Error:**
  - **URL:** `/404`
  - **Method:** `GET`
  - **Description:** Custom 404 error page.

- **500 Error:**
  - **URL:** `/500`
  - **Method:** `GET`
  - **Description:** Custom 500 error page.


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

6. Set up the database:
 ```bash
   flask db init
   flask db migrate
   flask db upgrade

7. **Run the application:**
   ```bash
   flask run

## Development

To run the application in development mode, ensure that the following configurations are set in `app.py`:

```python
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

## Usage
Once the application is running, you can access it via your web browser at http://localhost:5000. From there, you can create, edit, and delete blog posts using the provided forms.
   

    
    


   

   
