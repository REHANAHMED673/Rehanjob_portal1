from django.urls import path
from . import views

urlpatterns = [

    # Apply job (form open + submit)
    path("apply/<int:id>/", views.apply_job, name="apply"),

    # Saved jobs page
    path("saved-jobs/", views.saved_jobs, name="saved_jobs"),

    # Remove saved job
    path("remove-saved/<int:id>/", views.remove_saved_job, name="remove_saved"),

    # User applications list
    path("applications/", views.applications_list, name="applications"),
    

    path("notifications/", views.notifications, name="notifications"),

]