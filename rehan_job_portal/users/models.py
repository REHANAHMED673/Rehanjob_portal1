from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # Profile Photo
    profile_pic = models.ImageField(
        upload_to='profiles/',
        default='profiles/default.png',
        blank=True,
        null=True
    )

    # Basic Info
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    # Professional Info
    skills = models.TextField(blank=True, help_text="Comma separated skills")
    experience = models.TextField(blank=True)

    # Resume
    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    # Auto time
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username