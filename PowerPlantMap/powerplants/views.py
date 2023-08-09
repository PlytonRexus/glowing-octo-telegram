from rest_framework.views import APIView
from rest_framework.response import Response
from powerplants.models import PowerPlant
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
            })
        return Response(data)

class PowerPlantStats(APIView):
    renderer_classes = [CustomJSONRenderer]

    def get(self, request, state=None):
        queryset = PowerPlant.objects.all()
        if state:
            queryset = queryset.filter(PSTATABB=state)
        total_generation = queryset.aggregate(Sum('GENNTAN'))['GENNTAN__sum']
        data = []
        for plant in queryset:
            percentage = (plant.GENNTAN / total_generation) * 100 if total_generation else 0
            data.append({
                'PSTATABB': plant.PSTATABB,
                'PNAME': plant.PNAME,
                'GENNTAN': plant.GENNTAN,
                'Percentage': percentage,
            })
        return Response(data)

