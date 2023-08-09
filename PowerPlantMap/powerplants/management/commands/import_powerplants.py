import csv
from django.core.management.base import BaseCommand
from powerplants.models import PowerPlant, State

class Command(BaseCommand):
    help = 'Import power plant data from CSV'

    def handle(self, *args, **options):
        with open('/workspace/glowing-octo-telegram/PowerPlantMap/powerplants/powerplants.csv', 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                PowerPlant.objects.create(
                    SEQGEN=row['SEQGEN'],
                    PSTATABB=row['PSTATABB'],
                    PNAME=row['PNAME'],
                    LAT=row['LAT'],
                    LON=row['LON'],
                    GENNTAN=row['GENNTAN']
                )
        self.stdout.write(self.style.SUCCESS('Power plant data imported successfully'))

        with open('/workspace/glowing-octo-telegram/PowerPlantMap/powerplants/states.csv', 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                State.objects.create(
                    PSTATABB=row['PSTATABB'],
                    TOTALGENNTAN=row['TOTALGENNTAN']
                )
        self.stdout.write(self.style.SUCCESS('States data imported successfully'))

