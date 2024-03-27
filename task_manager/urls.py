from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks", views.task_list, name="task_list"),
    path("task/new/", views.create_task, name="create_task"),
    path("task/<int:task_id>/done/", views.mark_task_done, name="mark_task_done"),
    path("task/<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path(
        "task/<int:task_id>/undo/",
        views.undo_mark_task_done,
        name="undo_mark_task_done",
    ),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("sign-in/", views.sign_in, name="sign_in"),
]
