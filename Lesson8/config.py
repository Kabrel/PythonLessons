

# Mongo DB
client = MongoClient('127.0.0.1', 27017)

db = client['HH_jobs']

jobs_collection = db.jobs

'''
—труктура данных проекта:
{'_id': 'job_id',
 'название':'name',
 'работодатель': 'employer',
 'город': 'city',
 'метро': 'metro',
 'минимальна€ зарплата': 'salary_min',
 'максимальна€ зарплата': 'salary_max',
 'валюта зарплаты': 'salary_currency',
 'день размещени€ вакансии': 'vac_day',
 'мес€ц размещени€ вакансии': 'vac_month'
} 
'''

