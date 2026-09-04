from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag, Task


class TaskToggleViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="Test task",
        )
        self.url = reverse(
            "tasks:task-toggle",
            kwargs={"pk": self.task.pk},
        )

    def test_toggle_task_with_post(self):
        response = self.client.post(self.url)

        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.task.is_done)
        self.assertRedirects(
            response,
            reverse("tasks:task-list"),
        )

    def test_toggle_done_task_with_post(self):
        self.task.is_done = True
        self.task.save()

        response = self.client.post(self.url)

        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.task.is_done)

    def test_toggle_task_does_not_allow_get(self):
        response = self.client.get(self.url)

        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 405)
        self.assertFalse(self.task.is_done)


class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(
            content="Learn Django",
        )

        self.assertEqual(task.content, "Learn Django")
        self.assertFalse(task.is_done)


class TagModelTest(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(name="Study")

        self.assertEqual(tag.name, "Study")

