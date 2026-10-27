import pytest
from sqlalchemy import create_engine, text
from db_config import DATABASE_URL


@pytest.fixture
def db():
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    yield connection
    connection.close()


def test_add_student(db):
    result = db.execute(
        text(
            "INSERT INTO student "
            "(user_id, subject_id, level, education_form) "
            "VALUES (9999, 9999, 'Бакалавриат', 'Очная') "
            "RETURNING user_id"
        )
    )
    user_id = result.fetchone()[0]
    db.commit()

    check = db.execute(
        text("SELECT level FROM student WHERE user_id = :id"),
        {"id": user_id}
    ).fetchone()
    assert check[0] == "Бакалавриат"

    db.execute(
        text("DELETE FROM student WHERE user_id = :id"),
        {"id": user_id}
    )
    db.commit()


def test_update_subject(db):
    result = db.execute(
        text("INSERT INTO subject (subject_id, subject_title) "
             "VALUES (9999, 'Тестовый предмет') "
             "RETURNING subject_id")
    )
    subject_id = result.fetchone()[0]
    db.commit()

    db.execute(
        text("UPDATE subject SET subject_title = :title "
             "WHERE subject_id = :id"),
        {"title": "Изменённый предмет", "id": subject_id}
    )
    db.commit()

    check = db.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": subject_id}
    ).fetchone()
    assert check[0] == "Изменённый предмет"

    db.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": subject_id}
    )
    db.commit()


def test_delete_teacher(db):
    result = db.execute(
        text("INSERT INTO teacher (teacher_id, group_id, email) "
             "VALUES (9999, 9999, 'test@test.com') "
             "RETURNING teacher_id")
    )
    teacher_id = result.fetchone()[0]
    db.commit()

    db.execute(
        text("DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": teacher_id}
    )
    db.commit()

    check = db.execute(
        text("SELECT * FROM teacher WHERE teacher_id = :id"),
        {"id": teacher_id}
    ).fetchone()
    assert check is None
