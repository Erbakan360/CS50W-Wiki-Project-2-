# CS50W Wiki (Project 1)

A Wikipedia-like online encyclopedia that allows users to view, create, and edit entries.

Key Features: Uses Markdown for content storage and converts it to HTML for display. Includes a search feature that supports substring matching, a "Random Page" generator, and a full CRUD system for managing encyclopedia entries.

Tech: Python, Django, Markdown, HTML, CSS.

Project Requiremetns: https://cs50.harvard.edu/web/projects/1/wiki/

 Setup Instructions:
--------------------------------------------------
0. Download code/ Clone repository
   ```
   git clone https://github.com/Erbakan360/CS50W-Wiki-Project-1.git
   ```
1. Change directory to the wiki
   ```
   cd wiki
   ```

2. Install dependencies:
   ```
   pip install django markdown2
   ```

3. Run database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
  
4. Start the development server:
    ```
    python manage.py runserver
    ```
