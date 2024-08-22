from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserMan
from .serializers import UserManSerializer

class UserManTests(APITestCase):

    def setUp(self):
        # Create some users for testing
        self.user1 = UserMan.objects.create(name="User1")
        self.user2 = UserMan.objects.create(name="User2")
        self.user3 = UserMan.objects.create(name="User3")

    def test_list_users(self):
        url = "/users/"
        response = self.client.get(url)
        users = UserMan.objects.all()
        serializer = UserManSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        url = "/user/create/"
        data = {'name': 'NewUser'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserMan.objects.count(), 4)  # Including the new user
        self.assertEqual(UserMan.objects.get(id=4).name, 'NewUser')

    def test_retrieve_user_by_id(self):
        url = f"/user/{self.user1.id}/"
        response = self.client.get(url)
        serializer = UserManSerializer(self.user1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], serializer.data)

    def test_retrieve_user_by_name(self):
        url = f"/user/{self.user2.name}/"
        response = self.client.get(url)
        serializer = UserManSerializer(self.user2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], serializer.data)

    def test_update_user_by_id(self):
        url = f"/user/update/{self.user1.id}/"
        data = {'name': 'UpdatedUser1'}
        response = self.client.put(url, data)
        self.user1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "User updated successfully")
        self.assertEqual(self.user1.name, 'UpdatedUser1')

    def test_update_user_by_name(self):
        url = f"/user/update/{self.user2.name}/"
        data = {'name': 'UpdatedUser2'}
        response = self.client.put(url, data)
        self.user2.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "User updated successfully")
        self.assertEqual(self.user2.name, 'UpdatedUser2')

    def test_delete_user_by_id(self):
        url = f"/user/delete/{self.user1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "User deleted successfully")
        self.assertFalse(UserMan.objects.filter(id=self.user1.id).exists())

    def test_delete_user_by_name(self):
        url = f"/user/delete/{self.user2.name}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "User deleted successfully")
        self.assertFalse(UserMan.objects.filter(name=self.user2.name).exists())

    def test_retrieve_user_not_found(self):
        url = "/user/999/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "Not found")

    def test_update_user_not_found(self):
        url = "/user/update/999/"
        data = {'name': 'NonExistentUser'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "User not found")

    def test_delete_user_not_found(self):
        url = "/user/delete/999/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "User not found")
