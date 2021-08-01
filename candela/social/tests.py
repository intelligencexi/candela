from django.test import TestCase, SimpleTestCase, Client
from social import forms
from django.urls import reverse, resolve
from social.views import PostListView, PostDetailView


# Create your tests here.

# unit tests
class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('post-list')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_detail_url_is_resolved(self):
        url = reverse('post-detail')
        self.assertEquals(resolve(url).func.view_class, PostDetailView)


class TestViews(SimpleTestCase):
    def setup(self):
        self.client = Client()
        self.postdetail_url = reverse('post-detail')
        self.postlist_url = reverse('post-list')

    def test_postdetailview_Get(self):
        response = self.client.get(self.postdetail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'social/post-detail.html')

    def test_postlistview_Get(self):
        response = self.client.get(self.postdetail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'social/post-list.html')


# integration tests
class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'CANDELA')

    def feed_works(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')
        self.assertContains(response, '@')


class TestForms(TestCase):
    def test_valid_postforms(self):
        form = forms.PostForm({
            'message': "A post made by me"
        })

        self.assertTrue(form.is_valid())

    def test_invalid_postforms(self):
        form = forms.PostForm({
            'message': "A post made by me"
        })

        self.assertFalse(form.is_valid())
