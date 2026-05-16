import requests

BSURL="https://ru.yougile.com/api-v2/"
key = "u49pIh0psW1Q40poGt+if-hKVogWTp5yI5LpkyvtH5urhfwyT+lkNObjGWcvkURi"

def test_add_project_pozitiv():
    may_heders={'Content-Type': 'application/json',
                'Authorization': f'Bearer {key}'}
    body = {"title": "ГосУслуги"}
    response = requests.post(url=f"{BSURL}projects", headers=may_heders, json=body)
    assert response.status_code == 201

def test_add_project_negativ():
    may_heders = {'Content-Type': 'application/json',
                  'Authorization': f'Bearer {key}'}
    body = {"title": ""}
    response = requests.post(url=f"{BSURL}projects", headers=may_heders, json=body)
    assert response.status_code == 400

def test_update_project_pozitiv():
    may_heders = {'Content-Type': 'application/json',
                  'Authorization': f'Bearer {key}'}
    body = {"title": "Старое название"}
    response = requests.post(url=f"{BSURL}projects", headers=may_heders, json=body)
    assert response.status_code == 201
    response_body = response.json()
    id = response_body.get('id')
    # Меняем название
    body = {"title": "Новое название"}
    response = requests.put(url=f"{BSURL}projects/{id}", headers=may_heders, json=body)
    assert response.status_code == 200
    #Проверяем что название поменялось
    response = requests.get(url=f"{BSURL}projects/{id}", headers=may_heders)
    assert response.status_code == 200
    response_body = response.json()
    name = response_body.get('title')
    assert name ==  "Новое название"

def test_update_project_negativ():
    may_heders = {'Content-Type': 'application/json',
                  'Authorization': f'Bearer {key}'}
    body = {"title": "Старое название"}
    response = requests.post(url=f"{BSURL}projects", headers=may_heders, json=body)
    assert response.status_code == 201
    response_body = response.json()
    id = response_body.get('id')
    # Меняем название
    body = {"title": ""}
    response = requests.put(url=f"{BSURL}projects/{id}", headers=may_heders, json=body)
    assert response.status_code == 400
    # Проверяем что название не поменялось
    response = requests.get(url=f"{BSURL}projects/{id}", headers=may_heders)
    assert response.status_code == 200
    response_body = response.json()
    name = response_body.get('title')
    assert name == "Старое название"

def test_id_pozitiv():
    may_heders = {'Content-Type': 'application/json',
                  'Authorization': f'Bearer {key}'}
    body = {"title": "Красивое название"}
    response = requests.post(url=f"{BSURL}projects", headers=may_heders, json=body)
    assert response.status_code == 201
    response_body = response.json()
    id = response_body.get('id')
     # Получить по id
    response = requests.get(url=f"{BSURL}projects/{id}", headers=may_heders)
    assert response.status_code == 200
    response_body = response.json()
    name = response_body.get('title')
    assert name == "Красивое название"

def test_id_negativ():
    may_heders = {'Content-Type': 'application/json',
                  'Authorization': f'Bearer {key}'}
    body = {"title": "Красивое название"}
    response = requests.post(url=f"{BSURL}projects", headers=may_heders, json=body)
    assert response.status_code == 201
    response_body = response.json()
    id = response_body.get('id')
    # Получить по id
    response = requests.get(url=f"{BSURL}projects/{id}")
    assert response.status_code == 401
