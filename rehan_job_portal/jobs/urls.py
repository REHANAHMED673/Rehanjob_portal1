from django.urls import path
from . import views

urlpatterns = [

    # Show all jobs
    path('', views.job_list, name='jobs'),

    # Save job (LinkedIn style bookmark)
    path("jobs/save/<int:job_id>/", views.save_job, name="save_job")

]