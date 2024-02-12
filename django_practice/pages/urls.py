from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('integer/', views.integer_info, name='integer_info'),
    path('collections/', views.collection_info, name='collection_info'),
    path('string/', views.string_info, name='string_info'),
    path('boolean/', views.boolean_info, name='boolean_info'),
    path(
        'data_structures/',
        views.data_structures_info,
        name='data_structures_info'
        ),
    path('algorithms/', views.algorithms_info, name='algorithms_info'),
    path('method/', views.method_info, name='method_info'),
]
