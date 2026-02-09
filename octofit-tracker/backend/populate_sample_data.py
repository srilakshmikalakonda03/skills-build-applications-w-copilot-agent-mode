#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

# Clear existing data
print("Clearing existing data...")
Leaderboard.objects.all().delete()
Activity.objects.all().delete()
Workout.objects.all().delete()
User.objects.all().delete()
Team.objects.all().delete()

# Create Teams
print("Creating teams...")
marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
dc = Team.objects.create(name='DC', description='Team DC Superheroes')

# Create Users
print("Creating users...")
users = [
    User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
    User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
    User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
    User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
]

# Create Activities
print("Creating activities...")
Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
Activity.objects.create(user=users[3], type='Yoga', duration=40, date=timezone.now().date())

# Create Workouts
print("Creating workouts...")
workout1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
workout2 = Workout.objects.create(name='Agility Training', description='Agility and speed drills')
workout1.suggested_for.set(users)
workout2.suggested_for.set(users)

# Create Leaderboard
print("Creating leaderboard entries...")
Leaderboard.objects.create(user=users[0], score=100)
Leaderboard.objects.create(user=users[1], score=90)
Leaderboard.objects.create(user=users[2], score=95)
Leaderboard.objects.create(user=users[3], score=85)

print("✅ Database populated successfully with sample data!")
