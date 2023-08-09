from django.urls import path
from .views import TopNPowerPlants, PowerPlantStats

urlpatterns = [
    path('top/<int:n>/', TopNPowerPlants.as_view(), name='top-n'),
    path('stats/', PowerPlantStats.as_view(), name='power-plant-stats'),
    path('stats/<str:state>/', PowerPlantStats.as_view(), name='state-power-plant-stats'),
]
