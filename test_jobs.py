from requests import get, post

print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/3').json())
print(get('http://localhost:5000/api/v2/jobs/500').json())
print(get('http://localhost:5000/api/v2/jobs/qwerty').json())


print(post('http://localhost:5000/api/v2/jobs',
           # Нет полных данных
           json={'job': 'installation of radiation protection'}).json())
print(post('http://localhost:5000/api/v2/jobs', json={}).json())  # Пустое тело запроса
print("1")
print(post('http://localhost:5000/api/v2/jobs',
           json={'job': 'installing a long-distance communication antenna', 'team_leader': 4, 'work_size': "5",
                 # Правильное добавление
                 'collaborators': '6, 3', 'is_finished': True}).json())
print("2")
print(get('http://localhost:5000/api/v2/jobs').json())
