from django.test import TestCase
from django.urls import reverse
from LB.models import LBUser

class TestOuterViews(TestCase):
    def test_home(self):
        res = self.client.get(reverse("home-page"))
        self.assertEquals(res.status_code, 200)

    def test_login(self):
        res = self.client.get(reverse("login"))
        self.assertEquals(res.status_code, 200)

    def test_registration(self):
        res = self.client.get(reverse("register"))
        self.assertEquals(res.status_code, 200)


class TestMiddleViews(TestCase):
    def setUp(self):
        user1 = LBUser(first_name="Test", last_name="User", email="test@test.com", username="test", age=19)
        user1.set_password("test")
        user1.save()

    def test_login_fail(self):
        res = self.client.post(reverse("login"), {
            "username": "test",
            "password": "wrong" 
        })
        self.assertEquals(res.url, reverse("login"))


    def test_login_pass(self):
        res = self.client.post(reverse("login"), {
            "username": "test",
            "password": "test" 
        })
        self.assertEquals(res.status_code, 200)
        self.assertEquals(res.url, reverse("feed"))

    def test_logout(self):
        res = self.client.post(reverse("logout"))
        self.assertEquals(res.status_code, 200)
        self.assertEquals(res.url, reverse("login"))


