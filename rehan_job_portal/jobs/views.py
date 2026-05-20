from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from applications.models import SavedJob
from portal.models import Job


# Show all jobs
def job_list(request):

    jobs = Job.objects.all()

    return render(request, "job_list.html", {
        "jobs": jobs
    })


# Save job (LinkedIn-style feature)
@login_required
def save_job(request, job_id):

    job = Job.objects.get(id=job_id)

    SavedJob.objects.get_or_create(
        user=request.user,
        job=job
    )

    return redirect('/jobs/')