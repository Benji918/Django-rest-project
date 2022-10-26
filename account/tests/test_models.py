from rest_framework.test import APITestCase
from account.models import User

class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user(username='Benjamin', email='Kodif@gmail.com', password='123456789')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'Kodif@gmail.com')
        self.assertEqual(user.username, 'Benjamin')
        self.assertFalse(user.is_staff)

    def test_creates_super_user(self):
        user = User.objects.create_superuser(
            'cryce', 'crycetruly@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'crycetruly@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='Kodif@gmail.com', password='123456789')

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(
                username='',
                email='Kodif@gmail.com',
                password='1234vbb56789'
            )

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="username", email='', password='password123!@')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(
                username='username', email='', password='password123!@')

    def test_cant_create_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                username='kodi',
                email='fdkfd@gmail.com',
                password='odfjdjfdojf',
                is_staff=False
            )

    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username='username', email='crycetruly@gmail.com', password='password123!@', is_superuser=False)
