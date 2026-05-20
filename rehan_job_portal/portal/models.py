from django.db import models
from django.contrib.auth.models import User

# 1️⃣ Company Model
class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logo/')
    location = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name


# 2️⃣ Job Model
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    salary = models.IntegerField()
    job_type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 3️⃣ Applicant Profile Model
class ApplicantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.user.username


# 4️⃣ Application Model
class Application(models.Model):
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='Pending')

    def __str__(self):
        return f"{self.applicant} - {self.job}"


# 5️⃣ Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
