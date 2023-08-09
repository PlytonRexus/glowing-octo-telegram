from rest_framework.views import APIView
from rest_framework.response import Response
from powerplants.models import PowerPlant, State
from django.db.models import Sum
from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Customize the response data or formatting if needed
        return super().render(data, accepted_media_type, renderer_context)

class TopNPowerPlants(APIView):
    renderer_classes = [CustomJSONRenderer]

    def get(self, request, n):
        top_plants = PowerPlant.objects.order_by('-GENNTAN')[:n]
        data = []
        for plant in top_plants:
            data.append({
                'PSTATABB': plant.PSTATABB,
                'PNAME': plant.PNAME,
                'GENNTAN': plant.GENNTAN,
                'LAT': plant.LAT,
                'LON': plant.LON,
            })
        return Response(data)

class PowerPlantStats(APIView):
    renderer_classes = [CustomJSONRenderer]

    def get(self, request, state=None):
        queryset = PowerPlant.objects.all()
        TOTALGENERATION = None
        if state:
            queryset = queryset.filter(PSTATABB=state)
            TOTALGENERATION = State.objects.get(PSTATABB=state).TOTALGENNTAN
        data = []
        total_generation = None
        for plant in queryset:
            if not TOTALGENERATION:
                total_generation = State.objects.get(PSTATABB=plant.PSTATABB).TOTALGENNTAN
            percentage = (plant.GENNTAN / (total_generation if not TOTALGENERATION else TOTALGENERATION)) * 100 if (total_generation or TOTALGENERATION) else 0
            data.append({
                'PSTATABB': plant.PSTATABB,
                'PNAME': plant.PNAME,
                'GENNTAN': plant.GENNTAN,
                'LAT': plant.LAT,
                'LON': plant.LON,
                'PERCENTAGE': percentage,
            })
        return Response(data)

