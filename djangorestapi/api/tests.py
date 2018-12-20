#api/modles.py

from django.test import TestCase
from .models import ToDoList
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ModleTestList(TestCase):
    """Test the bucket list Model."""

    def setUp(self):
        """Defining the test client."""
        self.item_name = "This is my first project"
        self.todo_list = ToDoList(name=self.item_name)

    def test_model_can_create_a_todo_list(self):
        """Test the bucketlist model can create a bucketlist."""
        initial_count = ToDoList.objects.count()
        self.todo_list.save()
        new_count = ToDoList.objects.count()
        self.assertNotEqual(initial_count, new_count)



class TestUpdateList(TestCase):
    """Test for updating list items"""
    
    # define variable needed to run test
    def setUp(self):
        self.client = APIClient()
        self.update_data = {'item_name': 'change item'}
        self.res = self.client.post(reverse(create),self.update_data,format='json')

    # destroys variable after test has run
    def tearDown(self):
        self.client = None
        self.update_data = None
        self.res = None

    # test when input is empty
    def test_empty_input(self):
        self.update_data['item_name'] = ''
        self.assertEqual(self.res.status_code,406)

    # test when input contains only whitespace
    def test_empty_whitespace(self):
        self.update_data['item_name'] = '  '
        self.assertEqual(self.res.status_code,406)

    # test valid data
    def test_valid_data(self):
        self.assertEqual(self.res.status_code,201)

