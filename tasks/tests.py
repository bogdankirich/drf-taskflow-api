import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from .models import Category, Task

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user(db):
    return User.objects.create_user(username="tester", password="testpassword")


@pytest.fixture
def test_category(db):
    return Category.objects.create(name="Backend Task")


@pytest.mark.django_db
def test_create_task_authentication(api_client, test_user, test_category):
    api_client.force_authenticate(user=test_user)
    payload = {"title": "Learn pytest fixture", "category": test_category.id}

    response = api_client.post("/api/tasks/", data=payload)

    assert response.status_code == 201
    assert Task.objects.count() == 1
    created_task = Task.objects.first()
    assert created_task.owner == test_user
    assert created_task.category == test_category


@pytest.mark.django_db
def test_regular_user_cannot_create_category(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    payload = {"name": "Hacker teritory"}
    response = api_client.post("/api/category/", data=payload)

    assert response.status_code == 403


@pytest.mark.django_db
def test_regular_user_can_read_categories(api_client, test_user, test_category):
    api_client.force_authenticate(user=test_user)
    response = api_client.get("/api/category/")

    assert response.status_code == 200
    assert len(response.data) > 0
