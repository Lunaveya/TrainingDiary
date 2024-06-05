from urllib.request import Request
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from diary_app.controllers import ExerciseController
from diary_app.forms import SetsRepsWeightForm
from diary_app.models import Day, Done


# Create your views here.

def home_page(request) -> HttpResponse:
    exercise_controller: ExerciseController = ExerciseController()

    return render(request, 'home.html', {'additional_title': 'Расписание на неделю',
                                         'exercises1': exercise_controller.get_1_exercises(),
                                         'exercises2': exercise_controller.get_2_exercises(),
                                         'exercises3': exercise_controller.get_3_exercises(),
                                         'exercises4': exercise_controller.get_4_exercises(),
                                         'exercises5': exercise_controller.get_5_exercises(),
                                         'exercises6': exercise_controller.get_6_exercises(),
                                         'exercises7': exercise_controller.get_7_exercises(),
                                         })


def today_page(request) -> HttpResponse:
    today = datetime.now()
    day_num = datetime.isoweekday(today)
    names_day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    name_day = names_day[day_num - 1]
    day = day_num
    dones = []

    try:
        days = Day.objects.filter(day_of_the_week=day)
        for item in days:
            dones.extend(Done.objects.filter(day_id=item.id))

    except Exception:
        dones = None

    if request.method == 'POST':
        sets: int = request.POST.get('sets')
        reps: int = request.POST.get('reps')
        weight: int = request.POST.get('weight')

        new_param = Done(
            sets=sets,
            reps=reps,
            weight=weight
        )

        new_param.save()

    return render(request, 'today.html', {'additional_title': 'Расписание на сегодня',
                                            'dones': dones,
                                            'form': SetsRepsWeightForm(),
                                            'name_day': name_day})

