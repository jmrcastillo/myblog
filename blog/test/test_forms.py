

from django.test import SimpleTestCase
from blog.forms import EmailPostForm


class TestEmailForms(SimpleTestCase):

    def test_email_valid_data(self):
        form = EmailPostForm(data={
            'name': 'jmr',
            'email': 'jmr@gmail.com',
            'to': 'jm.cass20@gmail.com',
            'comments': 'I learn a lot from your stuff'
            })

        self.assertTrue(form.is_valid())

    def test_email_no_data(self):
        form = EmailPostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
