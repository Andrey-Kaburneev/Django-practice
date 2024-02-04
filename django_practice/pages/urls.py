from django.urls import path
from . import views

urlpatterns = [
    path('integer/', views.integer_info),
    path('collections/', views.collection_info),
    path('string/', views.string_info),
    path('boolean/', views.boolean_info),
    path('data_structures/', views.data_structures_info),
    path('algorithms/', views.algorithms_info),
    path('method/', views.method_info),
]
