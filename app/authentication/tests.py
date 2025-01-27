from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status

from settings.env_config import SUFFIX_API
from utils.suffix_router import SuffixRouter

User = get_user_model()


class UserRegisterTests(APITestCase):
    def setUp(self):
        self.registration_url = f"/{SUFFIX_API}{SuffixRouter.AUTH}"
        self.valid_user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword123",
            "confirm_password": "securepassword123"
        }
        self.invalid_user_data = {
            "username": "",
            "email": "invalidemail",
            "password": "",
            "confirm_password": ""
        }

    def test_register_user_success(self):
        """
        Проверяем, что пользователь успешно регистрируется с валидными данными.
        """
        response = self.client.post(
            self.registration_url,
            data=self.valid_user_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_invalid_data(self):
        """
        Проверяем, что регистрация с некорректными данными возвращает ошибку.
        """
        response = self.client.post(
            self.registration_url,
            data=self.invalid_user_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_duplicate_username(self):
        """
        Проверяем, что нельзя зарегистрировать двух пользователей с одинаковым username.
        """
        self.client.post(
            self.registration_url,
            data=self.valid_user_data,
            format='json'
        )
        response = self.client.post(
            self.registration_url,
            data=self.valid_user_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_register_user_missing_fields(self):
        """
        Проверяем, что регистрация без обязательных полей возвращает ошибку.
        """
        response = self.client.post(
            self.registration_url,
            data={"email": "testuser@example.com"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_with_weak_password(self):
        """
        Проверяем, что нельзя зарегистрироваться с простым паролем.
        """
        weak_password_data = {
            "username": "testuser2",
            "email": "testuser2@example.com",
            "password": "123",
            "confirm_password": "123"
        }
        response = self.client.post(
            self.registration_url,
            data=weak_password_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class UserLoginTest(APITestCase):
    def setUp(self):
        self.login_url: str = f"/{SUFFIX_API}{SuffixRouter.AUTH}login"
        self.valid_user_data = {
            "username": "testuser",
            "password": "securepassword123"
        }
        self.invalid_user_data = {
            "username": "ss",
            "password": "asas"
        }

    def test_login_user_success(self):
        """
        Проверяем, что пользователь успешно входит с валидными данными.
        """
        response = self.client.post(
            self.login_url,
            data=self.valid_user_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user_invalid_data(self):
        """
        Проверяем, что регистрация с некорректными данными возвращает ошибку.
        """
        response = self.client.post(
            self.login_url,
            data=self.invalid_user_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)