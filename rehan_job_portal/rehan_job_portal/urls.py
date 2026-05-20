from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# ✅ MEDIA SUPPORT
from django.conf import settings
from django.conf.urls.static import static


# =========================
# SMART START ROUTE
# =========================
def start(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    return redirect('/login/')


# =========================
# URL PATTERNS
# =========================
urlpatterns = [

    # Default route → login or dashboard
    path('', start),

    # Admin
    path('admin/', admin.site.urls),

    # Users (login, register, logout)
    path('', include('users.urls')),

    # Portal (home, profile)
    path('', include('portal.urls')),

    # Jobs
    path('jobs/', include('jobs.urls')),

    # Companies
    path('companies/', include('companies.urls')),

    # Applications
    path('', include('applications.urls')),
]


# =========================
# MEDIA FILES (VERY IMPORTANT)
# =========================
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)