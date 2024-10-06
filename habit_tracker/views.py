from django.shortcuts import render, redirect
from .models import Habit
from django.utils import timezone
from . import util

from datetime import datetime, timedelta
from django.db.models import Max
import json

# Create your views here.
def index(request):
    return render(request, "habit_tracker/index.html", {
        "habits": util.list_habits()
    })


def track_habit(request, habit):
    entries = Habit.objects.filter(name=habit)
    calendar_data = []

    max_duration = entries.aggregate(Max('duration'))['duration__max'] or 1

    for entry in entries:
        intensity = entry.duration / max_duration if max_duration != 0 else 0

        calendar_data.append({
            'date': entry.date,
            'duration': entry.duration,
            'intensity': intensity,
        })

    return render(request, "habit_tracker/track.html", {
        "habit": habit,
        "entries": calendar_data,
        "weekdays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    })


def add_habit_entry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        duration = request.POST.get("duration")

        if name not in util.list_habits():
            util.create_calendar(name, 2024)

        if not date:
            date = timezone.now()

        habit = Habit.objects.filter(name=name, date=date).first()

        if habit:
            habit.duration = habit.duration + int(duration)
            habit.save()

        else:
            habit = Habit(name=name, date=date + timedelta(hours=3), duration=duration)
            habit.save()

        return redirect("habit_tracker:track_habit", habit.name)

    else:
        return render(request, "habit_tracker/add.html")
