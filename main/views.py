from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Award
from main.forms import AwardForm, ExperienceForm


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

# Experience
def get_experience_json(request):
    category_query = request.GET.get("category", "").strip()
    experiences = Experience.objects.all()

    if category_query:
        experiences = experiences.filter(category=category_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)

    deserialized_data = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experience_list = [item.object for item in deserialized_data]
    selected_category = request.GET.get("category", "").strip()

    context = {
        "name": "Malvin Lionard",
        "experience_list": experience_list,
        "selected_category": selected_category,

    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Malvin Lionard",
        "form": form,
    }
    return render(request, "create_experience.html", context)

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Malvin Lionard",
        "form": form,
        "experience": experience,
    }
    return render(request, "update_experience.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        title = experience.title
        experience.delete()
        messages.success(request, f"Pengalaman '{title}' berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

# Award
def get_awards_json(request):
    title_query = request.GET.get("title", "").strip()
    awards = Award.objects.all()

    if title_query:
        awards = awards.filter(title__icontains=title_query)

    awards_json = serializers.serialize("json", awards)
    return HttpResponse(awards_json, content_type="application/json")

def show_awards(request):
    json_response = get_awards_json(request)

    awards = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    awards_list = [award.object for award in awards]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Malvin Lionard",
        "award_list": awards_list,
        "title_query": title_query,
    }
    return render(request, "awards.html", context)

def create_award(request):
    form = AwardForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pencapaian baru berhasil ditambahkan!")
        return redirect("main:show_awards")

    context = {
        "name": "Malvin Lionard",
        "form": form,
    }
    return render(request, "create_award.html", context)

def update_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    form = AwardForm(request.POST or None, instance=award)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data penghargaan berhasil diperbarui!")
        return redirect("main:show_awards")

    context = {
        "name": "Malvin Lionard",
        "form": form,
        "award": award,
    }

    return render(request, "update_award.html", context)

def delete_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        title = award.title
        award.delete()
        messages.success(request, f"Award '{title}' berhasil dihapus!")
        return redirect("main:show_awards")

    return redirect("main:show_awards")