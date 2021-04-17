from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player/<int:labeling_id>', views.player, name='player'),
    path('creative/<int:creative_id>', views.creative_detail, name='creative_detail'),
]
