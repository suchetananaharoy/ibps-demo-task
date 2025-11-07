IBPS Demo Task
This repository contains two parts as per the demo task:
1. Web Scraping Task — Scrapes IBPS (Institute of Banking Personnel Selection) job listings.
2. Django REST API Task — Implements a login API using Django REST Framework.
1. Web Scraping Task (ibps_scraper.py)
✅ Features:
- Scrapes IBPS job listings from official public pages.
- Extracts: Job Title, Location, Publish Date, and Job Link.
- Saves data into a CSV file (ibps_jobs.csv) using Pandas.
Run Instructions
python ibps_scraper.py
Creates ibps_jobs.csv in the same directory.
2. Django REST API Task (ibps_api)
✅ Features: Uses Django REST Framework.
Implements POST /api/login/ for authentication.
Setup Instructions
1. Navigate to project:
   cd ibps_api
2. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
3. Create test user:
   python manage.py createsuperuser
4. Run server:
   python manage.py runserver
API Usage
POST http://127.0.0.1:8000/api/login/
Request:
{
  'username': 'testuser',
  'password': 'testpass123'
}
Response:
{
  'token': 'your_generated_token_here'
}
Requirements
Install dependencies:
   pip install -r requirements.txt
Packages used: requests, beautifulsoup4, pandas, django, djangorestframework
Postman Collection
Included file: Postman_Collection.json (import into Postman to test /api/login/ endpoint).
Project Structure

ibps_project/
│
├── ibps_scraper.py
├── ibps_jobs.csv
├── requirements.txt
├── README.md
│
├── ibps_api/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── ibps_api/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── __init__.py
│   └── accounts/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── __init__.py
│
└── Postman_Collection.json

Test Credentials
Username: testuser
Password: test@123
Email id: testuser@gmail.com
Confirmation Message
I confirm I have read the complete job posting (including salary and terms), and I accept the demo task.
The repository link is https://github.com/suchetananaharoy/ibps-demo-task 
