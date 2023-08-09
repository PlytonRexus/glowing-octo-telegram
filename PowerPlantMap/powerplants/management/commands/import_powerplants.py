import csv
from django.core.management.base import BaseCommand
from powerplants.models import PowerPlant

class Command(BaseCommand):
    help = 'Import power plant data from CSV'

    def handle(self, *args, **options):
        with open('/workspace/glowing-octo-telegram/PowerPlantMap/powerplants/powerplants.csv', 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                PowerPlant.objects.create(
                    SEQGEN=row['SEQGEN'],
                    YEAR=row['YEAR'],
                    PSTATABB=row['PSTATABB'],
                    PNAME=row['PNAME'],
                    GENNTAN=row['GENNTAN'],
                )
        self.stdout.write(self.style.SUCCESS('Power plant data imported successfully'))

