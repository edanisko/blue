from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import json
import re
from scraper.models import Job, Product, TruckCompany, Return, Driver, Warehouse, Schedule


class Command(BaseCommand):

    def handle(self, **options):

        # get the job
        job = Job.objects.get(name='WHCorp')

        # collect html
        page = requests.get(job.url)

        # convert to soup
        soup = BeautifulSoup(page.content, 'html.parser')

        # get schedule for WHCorp
        elements = soup.find_all("table", class_="table table-striped")
        schedule = {

        }

        reg1 = "<th>(Morning|Afternoon)\s\(([0-9]{1,2})am - ([0-9]{1,2})pm\)</th>"
        reg2 = "<th>Week ([0-9]*)</th>"
        reg3 = "<td>OPEN</td>"

        for element in elements:
            print(element)
