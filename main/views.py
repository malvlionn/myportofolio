from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Award
from main.forms import AwardForm, ExperienceForm

import datetime

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Malvin Lionard",
        "npm": "2506591753",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Fakultas Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# Experience
def get_experience_json(request):
    category_query = request.GET.get("category", "").strip()
    experiences = Experience.objects.all()

    if category_query:
        experiences = experiences.filter(category=category_query)

    experiences_json = serializers.serialize("json", experiences, use_natural_foreign_keys=True)
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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

    awards_json = serializers.serialize("json", awards, use_natural_foreign_keys=True)
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

@login_required(login_url="/login/")
def create_award(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def update_award(request, award_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def delete_award(request, award_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        title = award.title
        award.delete()
        messages.success(request, f"Award '{title}' berhasil dihapus!")
        return redirect("main:show_awards")

    return redirect("main:show_awards")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Malvin",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        if request.user in award.starred_by.all():
            award.starred_by.remove(request.user)
        else:
            award.starred_by.add(request.user)

    return redirect("main:show_awards")