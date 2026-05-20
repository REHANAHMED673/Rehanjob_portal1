from django.db import models
from companies.models import Company


class Job(models.Model):

    JOB_TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
    )

    EXPERIENCE_LEVEL = (
        ('Fresher', 'Fresher'),
        ('Junior', 'Junior'),
        ('Mid Level', 'Mid Level'),
        ('Senior', 'Senior'),
    )

    title = models.CharField(max_length=200)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    description = models.TextField()

    location = models.CharField(max_length=100)

    salary = models.IntegerField()

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE
    )

    experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVEL
    )

    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title