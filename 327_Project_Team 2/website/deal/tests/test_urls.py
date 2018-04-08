from django.urls import reverse, resolve


class TestUrls:

    def test_index_url(self):
        path = reverse('deal:index')
        assert resolve(path).view_name == 'deal:index'

    def test_apparels_url(self):
        path = reverse('deal:apparels')
        assert resolve(path).view_name == 'deal:apparels'

    def test_accessories_url(self):
        path = reverse('deal:accessories')
        assert resolve(path).view_name == 'deal:accessories'

    def test_services_url(self):
        path = reverse('deal:services')
        assert resolve(path).view_name == 'deal:services'

    def test_electronics_url(self):
        path = reverse('deal:electronics')
        assert resolve(path).view_name == 'deal:electronics'

    def test_dailyessentials_url(self):
        path = reverse('deal:dailyessentials')
        assert resolve(path).view_name == 'deal:dailyessentials'

    def test_food_url(self):
        path = reverse('deal:food')
        assert resolve(path).view_name == 'deal:food'

    def test_alldeals_url(self):
        path = reverse('deal:alldeals')
        assert resolve(path).view_name == 'deal:alldeals'

    def test_details_url(self):
        path = reverse('deal:detail', kwargs={'deal_id': 1})
        assert resolve(path).view_name == 'deal:detail'

    def test_deal_add_url(self):
        path = reverse('deal:deal-add')
        assert resolve(path).view_name == 'deal:deal-add'

    def test_loginview_url(self):
        path = reverse('loginview')
        assert resolve(path).view_name == 'loginview'

    def test_userdeals_url(self):
        path = reverse('userdeals')
        assert resolve(path).view_name == 'userdeals'

    def test_info_url(self):
        path = reverse('info_json')
        assert resolve(path).view_name == 'info_json'

    def test_details_json_url(self):
        path = reverse('detail_json', kwargs={'pk': 1})
        assert resolve(path).view_name == 'detail_json'

  









