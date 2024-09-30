from django.urls import path
from . import views

app_name = "habit_tracker"
urlpatterns = [
    path('', views.index, name="index"),
    path('track/<str:habit>', views.track_habit, name="track_habit"),
    path('add/', views.add_habit_entry, name="add_habit_entry"),
]
