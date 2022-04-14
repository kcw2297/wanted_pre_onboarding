from django.test import TestCase
from funding.models import Funding

class FundingModelTestCase(TestCase):
    def setUp(self):
        Funding.objects.create(description='korea car',target=1000,limitation='10',dday='2023-12-22',title="good car")

    def test_funding_created(self):
        car = Funding.objects.get(title='good car')
        self.assertEqual(car.target,1000)