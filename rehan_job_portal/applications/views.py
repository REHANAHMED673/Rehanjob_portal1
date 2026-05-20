from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Application, SavedJob, Notification
from portal.models import Job


# =========================
# APPLY JOB (FORM + SUBMIT)
# =========================
@login_required
def apply_job(request, id):

    job = get_object_or_404(Job, id=id)

    # FORM SUBMIT
    if request.method == "POST":

        # Duplicate check
        if Application.objects.filter(user=request.user, job=job).exists():
            messages.warning(request, "You already applied for this job.")
            return redirect("applications")

        # Get form data
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        cover_letter = request.POST.get("cover_letter")
        resume = request.FILES.get("resume")

        # SAVE APPLICATION
        application = Application.objects.create(
            user=request.user,
            job=job,
            full_name=full_name,
            email=email,
            phone=phone,
            cover_letter=cover_letter,
            resume=resume
        )

        # 🔥 CREATE NOTIFICATION
        Notification.objects.create(
            user=request.user,
            message=f"You applied for {job.title}"
        )

        messages.success(request, "Application submitted successfully!")

        return redirect("applications")

    # FORM PAGE
    return render(request, "apply_job.html", {
        "job": job
    })


# =========================
# SAVED JOBS
# =========================
@login_required
def saved_jobs(request):

    jobs = SavedJob.objects.filter(user=request.user).select_related("job")

    return render(request, "saved_jobs.html", {
        "jobs": jobs
    })


# =========================
# REMOVE SAVED JOB
# =========================
@login_required
def remove_saved_job(request, id):

    saved = get_object_or_404(SavedJob, id=id, user=request.user)
    saved.delete()

    messages.success(request, "Saved job removed.")

    return redirect("saved_jobs")


# =========================
# APPLICATION LIST
# =========================
@login_required
def applications_list(request):

    applications = Application.objects.filter(user=request.user)\
        .select_related("job__company")\
        .order_by("-applied_at")

    return render(request, "applications.html", {
        "applications": applications
    })


# =========================
# NOTIFICATIONS PAGE
# =========================
@login_required
def notifications(request):

    notifications = request.user.notifications.all().order_by("-created_at")

    # Mark as read
    notifications.update(is_read=True)

    return render(request, "notifications.html", {
        "notifications": notifications
    })