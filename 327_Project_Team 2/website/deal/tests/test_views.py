from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from deal.views import index
from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestViews:

    def test_deal_detail_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:index')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_deal_detail_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:index')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url

    def test_userdeals_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('userdeals')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_userdeals_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('userdeals')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url

    def test_alldeals_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:alldeals')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_alldeals_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:alldeals')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url

    def test_apparels_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:apparels')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_apparels_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:apparels')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url

    def test_food_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:food')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_food_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:food')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url

    def test_accessories_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:accessories')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_accessories_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:accessories')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url

    def test_services_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:services')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_services_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:services')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url

    def test_electronics_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:electronics')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_electronics_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:electronics')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url

    def test_dailyessentials_authenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:dailyessentials')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = index(request)
        assert response.status_code == 200

    def test_dailyessentials_unauthenticated(self):
        mixer.blend('deal.Deal')
        path = reverse('deal:dailyessentials')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()

        response = index(request)
        assert 'deal/userdeals' in response.url





