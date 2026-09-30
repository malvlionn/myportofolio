from django.urls import path

from main.views import create_award, create_experience, delete_award, delete_experience, get_awards_json, get_experience_json, show_awards, show_experience, show_main, update_award, update_experience, register, login_user, logout_user, toggle_star, toggle_star_award, create_award_ajax

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("awards/", show_awards, name="show_awards"),
    path("awards/add/", create_award, name="create_award"),
    path("awards/add-ajax/", create_award_ajax, name="create_award_ajax"),
    path("awards/<uuid:award_id>/edit/", update_award, name="update_award"),
    path("awards/<uuid:award_id>/delete/", delete_award, name="delete_award"),
    path("api/awards/", get_awards_json, name="get_awards_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path(
        "experiences/<uuid:experience_id>/star/",
        toggle_star,
        name="toggle_star", 
    ),
    path(
        "awards/<uuid:award_id>/star/",
        toggle_star_award,
        name="toggle_star_award",
    ),
]