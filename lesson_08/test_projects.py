from projects_api import ProjectsAPI


def test_create_project_positive():
    api = ProjectsAPI()
    response = api.create_project("Тестовый проект")
    assert response.status_code == 201
    assert "id" in response.json()
    project_id = response.json()["id"]
    api.delete_project(project_id)


def test_create_project_negative():
    api = ProjectsAPI()
    response = api.create_project("")
    assert response.status_code == 400
    assert "error" in response.json()


def test_update_project_positive():
    api = ProjectsAPI()
    create_response = api.create_project("Проект для изменения")
    project_id = create_response.json()["id"]
    update_response = api.update_project(project_id, "Новое имя")
    assert update_response.status_code == 200
    api.delete_project(project_id)


def test_update_project_negative():
    api = ProjectsAPI()
    response = api.update_project("несуществующий_id", "Новое имя")
    assert response.status_code == 404
    assert "error" in response.json()


def test_get_project_positive():
    api = ProjectsAPI()
    create_response = api.create_project("Проект для получения")
    project_id = create_response.json()["id"]
    get_response = api.get_project(project_id)
    assert get_response.status_code == 200
    assert "Проект для получения" in get_response.json()["title"]
    api.delete_project(project_id)


def test_get_project_negative():
    api = ProjectsAPI()
    response = api.get_project("несуществующий_id")
    assert response.status_code == 404
    assert "error" in response.json()
