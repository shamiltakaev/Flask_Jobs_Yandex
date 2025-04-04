from requests import get, post

print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/3').json())
print(get('http://localhost:5000/api/jobs/500').json())
print(get('http://localhost:5000/api/jobs/qwerty').json())


print(post('http://localhost:5000/api/jobs',
           # not full list of characters
           json={'job': 'installation of radiation protection'}).json())
print(post('http://localhost:5000/api/jobs', json={}).json())  # empty request
print(post('http://localhost:5000/api/jobs',
           json={'job': 'installing a long-distance communication antenna', 'team_leader': 4, 'work_size': 5,
                 # cool request
                 'collaborators': '6, 3', 'category': 3, 'is_finished': True}).json())
print(get('http://localhost:5000/api/jobs').json())
