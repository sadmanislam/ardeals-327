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
        assert 'accounts/login' in response.url




