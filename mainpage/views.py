from django.shortcuts import render
from .models import Description
from .models import Lesson


def homepage(request):
    description_list = Description.objects.all()
    return render(
        request, 
        "index.html", 
        {"description_list": description_list}
    )


def description(request, id):
    description_object = Description.objects.get(id=id)
    return render(request, 'description.html', {"description": description_object})

def lesson(request, id: int):
    context = {}
    one_lesson = Lesson.objects.get(id=id)
    context["lesson"] = one_lesson
    return render(request, "course/lesson.html", context)
