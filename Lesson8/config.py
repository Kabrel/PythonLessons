

# Mongo DB
client = MongoClient('127.0.0.1', 27017)

db = client['HH_jobs']

jobs_collection = db.jobs

'''
��������� ������ �������:
{'_id': 'job_id',
 '��������':'name',
 '������������': 'employer',
 '�����': 'city',
 '�����': 'metro',
 '����������� ��������': 'salary_min',
 '������������ ��������': 'salary_max',
 '������ ��������': 'salary_currency',
 '���� ���������� ��������': 'vac_day',
 '����� ���������� ��������': 'vac_month'
} 
'''

