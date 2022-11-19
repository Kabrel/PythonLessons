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
            print(f"от {doc['salary_min']} до {doc['salary_max']} руб.")
        if doc['salary_min'] is not None:
            print(f"от {doc['salary_min']} руб.")
        if doc['salary_max'] is not None:
            print(f"до {doc['salary_max']} руб.")
        print(doc['salary_currency'])
        print('----------------')
    print(f"Найдено {jobs_collection.count_documents({'$or': [{'salary_min': {'$gte': val}}, {'salary_max': {'$gte': val}}]})} вакансий.")
    print('----------------')

def search_vacancy_by_name():
    pass

def search_vacancy_by_metro():
    pass

def search_vacancy_employer():
    pass



init()