from django.test import TestCase

# Create your tests here.
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

def test_homepage_access():
    url = reverse('home')
    assert url == "/"
@pytest.mark.django_db
def test_create_tutorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk