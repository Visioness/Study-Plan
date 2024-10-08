from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Max
from django.urls import reverse
from datetime import datetime
from .models import Habit
from . import util
import json

# Create your views here.
def index(request):
    return render(request, "habit_tracker/index.html", {
        "habits": util.list_habits()
    })


def track_habit(request, habit):
    # POST request
    if request.method == "POST":
        # TODO
        data = json.loads(request.body)
        date = data.get('habitDate')
        new_duration = data.get('habitDuration')

        edited_habit = Habit.objects.filter(name=habit, date=date).first()
        edited_habit.duration = new_duration
        edited_habit.save()

        entries = Habit.objects.filter(name=habit)
        max_duration = entries.aggregate(Max('duration'))['duration__max'] or 1
        data = util.update_data(entries, max_duration)

        return JsonResponse({
            'success': True,
            'message': 'Habit updated successfully.',
            'entries': data
        })

    # DELETE request
    elif request.method == "DELETE":
        # TODO
        data = json.loads(request.body)
        date = data.get('habitDate')

        edited_habit = Habit.objects.filter(name=habit, date=date).first()
        edited_habit.duration = 0
        edited_habit.save()

        entries = Habit.objects.filter(name=habit)
        max_duration = entries.aggregate(Max('duration'))['duration__max'] or 1
        data = util.update_data(entries, max_duration)

        return JsonResponse({
            'success': True,
            'message': 'Habit updated successfully.',
            'entries': data
        })

    # GET request
    else:
        entries = Habit.objects.filter(name=habit)
        max_duration = entries.aggregate(Max('duration'))['duration__max'] or 1

        data = util.update_data(entries, max_duration)

        return render(request, "habit_tracker/track.html", {
            "habit": habit,
            "entries": data,
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
            date = datetime.now().date()

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
