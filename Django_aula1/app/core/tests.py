from django.test import TestCase

# Create your tests here.
class NatalTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_test(self):
        self.assertContains(self.response, 'natal', status_code=200)

    def test_template_natal(self):
        self.assertTemplateUsed(self.response, 'natal.html')