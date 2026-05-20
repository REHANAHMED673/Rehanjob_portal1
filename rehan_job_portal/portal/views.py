from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from jobs.models import Job
from companies.models import Company
from applications.models import Application, SavedJob
from users.models import Profile
from users.forms import ProfileForm


# =========================
# DASHBOARD
# =========================
@login_required
def home(request):

    user = request.user

    # Global counts
    total_jobs = Job.objects.count()
    total_companies = Company.objects.count()

    # User-based counts
    total_applications = Application.objects.filter(user=user).count()
    total_saved = SavedJob.objects.filter(user=user).count()

    # Status counts
    pending = Application.objects.filter(user=user, status="Pending").count()
    accepted = Application.objects.filter(user=user, status="Accepted").count()
    rejected = Application.objects.filter(user=user, status="Rejected").count()

    # Recent applications (IMPORTANT FIX)
    recent_apps = Application.objects.filter(user=user)\
        .select_related("job__company")\
        .order_by("-applied_at")[:5]

    context = {
        "total_jobs": total_jobs,
        "total_companies": total_companies,
        "total_applications": total_applications,
        "total_saved": total_saved,

        "pending": pending,
        "accepted": accepted,
        "rejected": rejected,

        "recent_apps": recent_apps,
    }

    return render(request, "home.html", context)


# =========================
# PROFILE PAGE
# =========================
@login_required
def profile(request):

    user = request.user

    # Get or create profile
    profile, created = Profile.objects.get_or_create(user=user)

    # Stats
    applied_jobs = Application.objects.filter(user=user).count()
    saved_jobs = SavedJob.objects.filter(user=user).count()

    context = {
        "user": user,
        "profile": profile,
        "applied_jobs": applied_jobs,
        "saved_jobs": saved_jobs,
    }

    return render(request, "profile.html", context)


# =========================
# EDIT PROFILE
# =========================
@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = ProfileForm(instance=profile)

    return render(request, "edit_profile.html", {
        "form": form
    })