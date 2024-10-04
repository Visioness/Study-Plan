from .models import Habit
from datetime import timedelta, datetime
from django.utils import timezone


def list_habits():
    return Habit.objects.values_list('name', flat=True).distinct()


def search_habits(habit_name):
    entries = list(Habit.objects.filter(name=habit_name))
    sorted_entries = sorted(entries, key=lambda x: x.date)

    return sorted_entries


def create_calendar(habit_name, year):
    entries = search_habits(habit_name)
    
    if entries:
        start_date = entries[-1].date
    else:
        start_date = datetime(year, 1, 1)

    current_date = datetime.today().date()
    day_difference = (current_date - start_date).days

    for i in range(day_difference + 1):
        date = start_date + timedelta(days=i) 
        
        if not Habit.objects.filter(name=habit_name, date=date):
            new_entry = Habit(
                name=habit_name,
                date=date,
                duration=0,
            )

            new_entry.save()