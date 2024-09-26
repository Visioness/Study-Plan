from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "habit_tracker/index.html")

def track_habit(request, habit):
    return render(request, "habit_tracker/track.html", {
        "habit": habit.title(),
    })
