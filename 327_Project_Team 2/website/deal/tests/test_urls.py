from django.urls import reverse, resolve


class TestUrls:

    def test_index_url(self):
        path = reverse('deal:index')
        assert resolve(path).view_name == 'deal:index'

    def test_alldeals_url(self):
        path = reverse('deal:alldeals')
        assert resolve(path).view_name == 'deal:alldeals'

    def test_details_url(self):
        path = reverse('deal:detail', kwargs={'deal_id': 1})
        assert resolve(path).view_name == 'deal:detail'

    def test_info_url(self):
        path = reverse('info_json')
        assert resolve(path).view_name == 'info_json'

    def test_details_json_url(self):
        path = reverse('detail_json', kwargs={'pk': 1})
        assert resolve(path).view_name == 'detail_json'

  









