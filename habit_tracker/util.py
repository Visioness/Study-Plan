from .models import Habit


def list_habits():
    return Habit.objects.values_list('name', flat=True).distinct()


def search_habits(habit_name):
    return Habit.objects.filter(name=habit_name)