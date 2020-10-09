from django.test import TestCase
from scraper.models import Job


class JobTestCase(TestCase):
    def setUp(self):
        Job.objects.create(
            url="​https://bluecargo.julink.fr/site1/index.html", name="WHCorp")
        Job.objects.create(
            url="​https://bluecargo.julink.fr/site2/index.html", name="AmericanStorage")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        site1 = Job.objects.get(name="WHCorp")
        site2 = Job.objects.get(name="AmericanStorage")

        self.assertEqual(
            site1.url, '​https://bluecargo.julink.fr/site1/index.html')
        self.assertEqual(
            site2.url, '​https://bluecargo.julink.fr/site2/index.html')
