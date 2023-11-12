# Django News Website

## Overview

This Django News Website is a web application that utilizes external APIs to fetch and display news information. The project is built using the Django framework, providing a robust and scalable structure for managing and presenting news articles.

## Features

- **API Integration:** The website fetches news information from external APIs, ensuring up-to-date and relevant content.
  
- **User-Friendly Interface:** The user interface is designed for easy navigation and readability, providing a pleasant experience for users.

- **Categorization:** News articles are categorized for better organization, allowing users to explore specific topics of interest.

- **Responsive Design:** The website is built with a responsive design, ensuring optimal viewing experience across various devices.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/django-news-website.git
   cd django-news-website

2. **Create a virtual environment:**
  ```bash
  python -m venv venv

3. **Activate the virtual environment:**

  On Windows:
  ```bash
  Copy code
  .\venv\Scripts\activate
  On macOS and Linux:
  ```bash
  source venv/bin/activate

4. **Install dependencies:**

  ```bash
  pip install -r requirements.txt

5. **Apply database migrations:**

  ```bash
  python manage.py migrate

6. **Run the development server:**

  ```bash
  python manage.py runserver

7. **Access the website:**

  Open your web browser and go to http://localhost:8000/ to view the Django News Website.

## Configuration

### API Key:
Obtain an API key from your preferred news API provider and update the NEWS_API_KEY variable in the settings.py file.

### Database Configuration:
Adjust database settings in the settings.py file if needed. By default, the project is configured to use SQLite.

