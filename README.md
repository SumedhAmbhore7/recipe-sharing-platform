# Recipe Sharing Platform

A web application for sharing and discovering recipes, built with Flask and SQLite.

## Features

- User registration and login
- Upload and share recipes
- View personal recipe collection
- Dashboard for managing recipes

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open http://localhost:5000 in your browser

## Deployment to Render

1. Push your code to GitHub
2. Connect your GitHub repo to Render
3. Set the following environment variables in Render:
   - `SECRET_KEY`: A random secret key for Flask sessions
4. Deploy the web service
5. Note: The app uses SQLite, which is not persistent on Render. Data will be lost on redeploys. Consider switching to PostgreSQL for production.

## Technologies Used

- Flask
- SQLite
- Bootstrap (for frontend)
