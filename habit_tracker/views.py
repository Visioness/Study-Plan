from django.shortcuts import render, redirect
from .models import Habit
from django.utils import timezone
from . import util

# Create your views here.
def index(request):
    return render(request, "habit_tracker/index.html", {
        "habits": util.list_habits()
    })


def track_habit(request, habit):
    return render(request, "habit_tracker/track.html", {
        "habit": habit,
        "entries": util.search_habits(habit)
    })


def add_habit_entry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        duration = request.POST.get("duration")

        if not date:
            date = timezone.now()

        habit = Habit.objects.filter(name=name, date=date).first()
        
        if habit:
            habit.duration = habit.duration + int(duration)
            habit.save()

        else:
            habit = Habit(name=name, date=date, duration=duration)
            habit.save()

        return redirect("habit_tracker:track_habit", habit.name)
            
    else:
        return render(request, "habit_tracker/add.html")