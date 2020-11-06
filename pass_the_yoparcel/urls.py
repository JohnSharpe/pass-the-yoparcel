from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('<word>/', views.word_view, name='word')
]
