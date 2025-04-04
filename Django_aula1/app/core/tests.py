from django.test import TestCase
from core.models import FeriadoModel
from datetime import datetime

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
    

class FeriadoModelTest(TestCase):
    def setUp(self):
        self.cadastro = FeriadoModel.objects.create(nome='Natal', dia=25, mes=12)

    def test_create(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_name(self):
        feriado_no_banco = FeriadoModel.objects.first()
        self.assertEqual(feriado_no_banco.nome, "Natal")