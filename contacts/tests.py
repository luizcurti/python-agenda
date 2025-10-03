from django.test import TestCase
from django.urls import reverse
from .models import Category, Contact


class ContactsModelTests(TestCase):
    def test_create_category_and_contact(self):
        c = Category.objects.create(name='Friends')
        contato = Contact.objects.create(
            first_name='John',
            last_name='Smith',
            phone='12345',
            email='john@example.com',
            category=c,
            visible=True
        )
        self.assertEqual(str(c), 'Friends')
        self.assertEqual(str(contato), 'John')


class ContactsViewTests(TestCase):
    def setUp(self):
        categoria = Category.objects.create(name='Work')
        for i in range(3):
            Contact.objects.create(
                first_name=f'Person{i}',
                last_name='Test',
                phone=f'000{i}',
                category=categoria,
                visible=True
            )

    def test_index_view(self):
        resp = self.client.get(reverse('contacts:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Person0')

    def test_search_without_term_redirect(self):
        resp = self.client.get(reverse('contacts:search'))
        # Should redirect to index because term is required
        self.assertEqual(resp.status_code, 302)


class ContactsAPITests(TestCase):
    def setUp(self):
        self.categoria = Category.objects.create(name='API')
        self.contato = Contact.objects.create(
            first_name='ApiPerson',
            last_name='X',
            phone='999',
            category=self.categoria,
            visible=True
        )

    def test_api_list_contacts(self):
        resp = self.client.get(reverse('contacts:api_contacts'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('ApiPerson', resp.content.decode())

    def test_api_retrieve_contact(self):
        resp = self.client.get(reverse('contacts:api_contact_detail', args=[self.contato.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn('ApiPerson', resp.content.decode())
