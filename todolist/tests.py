# tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Tasks

class tasks_crud_tests(TestCase):
    def setUp(self):
        self.tasks = Tasks.objects.create(title='Test Tasks', description='Test Description', status='Pending')

    def test_create_tasks(self):
        initial_count = Tasks.objects.count()
        new_tasks = Tasks.objects.create(title='New Tasks', description='New Description', status='Pending')
        new_count = Tasks.objects.count()
        self.assertEqual(new_count, initial_count + 1)

    def test_read_tasks(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tasks.title)

    def test_update_tasks(self):
        updated_title = 'Test Tasks'
        updated_description = 'Test Description'
        updated_status = 'Pending'
        update_data = {
            'title': updated_title,
            'description': updated_description,
            'status': updated_status
        }
        response = self.client.post(reverse('edit_task', args=(self.tasks.id,)), update_data)
        self.assertEqual(response.status_code, 200)  # Check for redirect
        updated_task = Tasks.objects.get(id=self.tasks.id)
        self.assertEqual(updated_task.title, updated_title)
        self.assertEqual(updated_task.description, updated_description)
        self.assertEqual(updated_task.status, updated_status)

    def test_delete_tasks(self):
        initial_count = Tasks.objects.count()
        response = self.client.post(reverse('delete_task', args=(self.tasks.id,)))
        self.assertEqual(response.status_code, 302)  # Check for redirect
        new_count = Tasks.objects.count()
        self.assertEqual(new_count, initial_count - 1)
