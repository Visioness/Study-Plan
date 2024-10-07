from django.shortcuts import render, redirect
from .models import Habit
from . import util
import json
from datetime import datetime
from django.db.models import Max

# Create your views here.
def index(request):
    return render(request, "habit_tracker/index.html", {
        "habits": util.list_habits()
    })


def track_habit(request, habit):
    if request.method == "POST":
        # TODO
        data = json.loads(request.body)
        date = data.get('habitDate')
        new_duration = data.get('habitDuration')

        edited_habit = Habit.objects.filter(name=habit, date=date).first()
        edited_habit.duration = new_duration
        edited_habit.save()

        return JsonResponse({'success': True, 'message': 'Habit updated successfully!'})

    elif request.method == "DELETE":
        # TODO
        pass

    else:
        entries = Habit.objects.filter(name=habit)
        calendar_data = []

        max_duration = entries.aggregate(Max('duration'))['duration__max'] or 1

        for entry in entries:
            intensity = entry.duration / max_duration if max_duration != 0 else 0

            calendar_data.append({
                'name': habit,
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
