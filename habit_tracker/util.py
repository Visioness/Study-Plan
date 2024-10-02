from .models import Habit
from datetime import timedelta
from django.utils import timezone


def list_habits():
    return Habit.objects.values_list('name', flat=True).distinct()


def search_habits(habit_name):
    entries = list(Habit.objects.filter(name=habit_name))
    sorted_entries = sorted(entries, key=lambda x: x.date, reverse=True)

    return sorted_entries


def create_calendar(habit_name):
    for i in range(30):
        date = timezone.now() - timedelta(days=i) + timedelta(hours=3)
        if not Habit.objects.filter(name=habit_name, date=date):
            new_entry = Habit(
                name=habit_name,
                date=date,
                duration=0,
            )

            new_entry.save()