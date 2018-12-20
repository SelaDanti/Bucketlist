#api/tests.py

from django.test import TestCase
from .models import ToDoList
from responset_framework.test import APIClient
from responset_framework import status
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
        self.assertEqual(result.status_code,status.HTTP_201_CREATED)


class TestUpdateList(TestCase):
    """Test for updating list items"""
    
    # define variable needed to run test
    def setUp(self):
        self.client = APIClient()
        self.update_data = {'item_name': 'change item'}
        self.response = self.client.post(reverse('create'),self.update_data,format='json')

    # destroys variable after test has run
    def tearDown(self):
        self.client = None
        self.update_data = None
        self.response = None

    # test when input is empty
    def test_empty_input(self):
        self.update_data['item_name'] = ''
        self.assertEqual(self.response.status_code,406)

    # test when input contains only whitespace
    def test_empty_whitespace(self):
        self.update_data['item_name'] = '  '
        self.assertEqual(self.response.status_code,406)

    # test valid data
    def test_valid_data(self):
        self.assertEqual(self.response.status_code,201)

    def test_fetch_all_todo_items(self):
        """Test for fetching todo items from the database"""
        todo = ToDoList.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': todo.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todo)
