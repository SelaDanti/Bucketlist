#api/tests.py

from django.test import TestCase
from .models import ToDoList
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestList(TestCase):
    """Test the bucket list Model."""

    def setUp(self):
        """Defining the test client."""
        self.item_name = "This is my first project"
        self.todo_list = ToDoList(item_name=self.item_name)

    def test_model_can_create_a_todo_list(self):
        """Test the bucketlist model can create a bucketlist."""
        initial_count = ToDoList.objects.count()
        self.todo_list.save()
        new_count = ToDoList.objects.count()
        self.assertNotEqual(initial_count, new_count)
        result =self.todo_list.save()


class TestToDoList(TestCase):
    """Test for updating list items"""

    def setUp(self):
        """define variable needed to run test."""
        self.client = APIClient()
        self.sample_data = {'item_name': 'change item'}
        self.response = self.client.post(reverse('create'),self.sample_data,format='json')

    def tearDown(self):
        """destroys variable after test has run."""
        self.client = None
        self.update_data = None
        self.response = None
    
    def test_api_can_add_new_item(self):
        """Test add functionality"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    """test valid data."""
    def test_valid_data(self):
        self.assertEqual(self.response.status_code,201)

    def test_fetch_a_single_todo_item(self):
        """Test for fetching a todo item from the database"""
        todo = ToDoList.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': todo.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todo)
