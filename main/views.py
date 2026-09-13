from django.shortcuts import render

from main.models import Experience, Award


def show_main(request):
    context = {
        "name": "Malvin Lionard",
        "npm": "2506591753",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Fakultas Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Malvin Lionard",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_awards(request):
    awards = Award.objects.all()
    context = {
        "name": "Malvin Lionard",
        "award_list": awards,
    }
    return render(request, "awards.html", context)