def init():
    pass

def add_vacancy_to_bd():
    pass

def delete_vacancy_from_bd():
    pass

def change_vacancy_in_bd():
    pass

def search_vacancy_by_sal(val):
    result = jobs_collection.find({'$or': [{'salary_min': {'$gte': val}}, {'salary_max': {'$gte': val}}]})
    for doc in result:
        print('----------------')
        print(doc['name'])
        print(doc['employer'])
        print(doc['city'])
        print(doc['link'])
        if doc['salary_max'] is not None and doc['salary_min'] is not None:
            print(f"�� {doc['salary_min']} �� {doc['salary_max']} ���.")
        if doc['salary_min'] is not None:
            print(f"�� {doc['salary_min']} ���.")
        if doc['salary_max'] is not None:
            print(f"�� {doc['salary_max']} ���.")
        print(doc['salary_currency'])
        print('----------------')
    print(f"������� {jobs_collection.count_documents({'$or': [{'salary_min': {'$gte': val}}, {'salary_max': {'$gte': val}}]})} ��������.")
    print('----------------')

def search_vacancy_by_name():
    pass

def search_vacancy_by_metro():
    pass

def search_vacancy_employer():
    pass



init()