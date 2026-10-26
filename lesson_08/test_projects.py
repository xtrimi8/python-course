from projects_api import ProjectsAPI


def test_create_project_positive():
    api = ProjectsAPI()
    response = api.create_project("Тестовый проект")
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative():
    api = ProjectsAPI()
    response = api.create_project("")
    assert response.status_code == 400


def test_update_project_positive():
    api = ProjectsAPI()
    create_response = api.create_project("Проект для изменения")
    project_id = create_response.json()["id"]
    update_response = api.update_project(project_id, "Новое имя")
    assert update_response.status_code == 200


def test_update_project_negative():
    api = ProjectsAPI()
    response = api.update_project("несуществующий_id", "Новое имя")
    assert response.status_code == 404


def test_get_project_positive():
    api = ProjectsAPI()
    create_response = api.create_project("Проект для получения")
    project_id = create_response.json()["id"]
    get_response = api.get_project(project_id)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Проект для получения"


def test_get_project_negative():
    api = ProjectsAPI()
    response = api.get_project("несуществующий_id")
    assert response.status_code == 404
