from django.db import models

# Profile for "About Me" section
class Profile(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='profile_photos/', blank=True)

    def __str__(self):
        return self.name


# Hobbies section
class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Learning journey / timeline
class LearningYear(models.Model):
    year = models.IntegerField()
    achievement = models.TextField()

    def __str__(self):
        # Show first 30 characters of achievement for readability
        return f"{self.year} – {self.achievement[:30]}..."


# Skills section
class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50, blank=True)  # e.g., Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name
