#!/usr/bin/env python3
"""
Populate MongoDB with sample superhero team data using native PyMongo.
This bypasses Django ORM to avoid djongo ObjectID/ForeignKey incompatibilities.
"""

import os
import sys
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

# Clear existing collections
print("Clearing existing collections...")
db.octofit_tracker_team.delete_many({})
db.octofit_tracker_user.delete_many({})
db.octofit_tracker_activity.delete_many({})
db.octofit_tracker_workout.delete_many({})
db.octofit_tracker_leaderboard.delete_many({})

# Create teams
print("Creating teams...")
teams = [
    {
        '_id': ObjectId(),
        'name': 'Marvel',
        'description': 'Mighty Marvel superheroes'
    },
    {
        '_id': ObjectId(),
        'name': 'DC',
        'description': 'Powerful DC superheroes'
    }
]
team_result = db.octofit_tracker_team.insert_many(teams)
marvel_id = team_result.inserted_ids[0]
dc_id = team_result.inserted_ids[1]
print(f"✅ Created Marvel team: {marvel_id}")
print(f"✅ Created DC team: {dc_id}")

# Create users
print("Creating users...")
users = [
    {
        '_id': ObjectId(),
        'name': 'Spider-Man',
        'email': 'spiderman@marvel.com',
        'team': marvel_id,
        'is_superhero': True
    },
    {
        '_id': ObjectId(),
        'name': 'Iron Man',
        'email': 'ironman@marvel.com',
        'team': marvel_id,
        'is_superhero': True
    },
    {
        '_id': ObjectId(),
        'name': 'Batman',
        'email': 'batman@dc.com',
        'team': dc_id,
        'is_superhero': True
    },
    {
        '_id': ObjectId(),
        'name': 'Superman',
        'email': 'superman@dc.com',
        'team': dc_id,
        'is_superhero': True
    }
]
user_result = db.octofit_tracker_user.insert_many(users)
user_ids = user_result.inserted_ids
print(f"✅ Created {len(user_ids)} users")

# Create activities
print("Creating activities...")
activities = [
    {
        '_id': ObjectId(),
        'name': 'Morning Run',
        'description': 'Ran 5 miles in the park',
        'user': user_ids[0],
        'date': datetime.now()
    },
    {
        '_id': ObjectId(),
        'name': 'Gym Session',
        'description': 'Upper body strength training',
        'user': user_ids[1],
        'date': datetime.now()
    },
    {
        '_id': ObjectId(),
        'name': 'Yoga',
        'description': 'Evening yoga session',
        'user': user_ids[2],
        'date': datetime.now()
    },
    {
        '_id': ObjectId(),
        'name': 'Swimming',
        'description': 'Laps in the pool',
        'user': user_ids[3],
        'date': datetime.now()
    }
]
activity_result = db.octofit_tracker_activity.insert_many(activities)
print(f"✅ Created {len(activity_result.inserted_ids)} activities")

# Create workouts
print("Creating workouts...")
workouts = [
    {
        '_id': ObjectId(),
        'name': 'Cardio Blast',
        'description': 'High-intensity cardio workout',
        'duration_minutes': 30,
        'calories_burned': 250,
        'suggested_for': user_ids[:2]  # Marvel users
    },
    {
        '_id': ObjectId(),
        'name': 'Strength Training',
        'description': 'Full body strength routine',
        'duration_minutes': 45,
        'calories_burned': 350,
        'suggested_for': user_ids[2:]  # DC users
    },
    {
        '_id': ObjectId(),
        'name': 'Flexibility Training',
        'description': 'Stretching and mobility work',
        'duration_minutes': 20,
        'calories_burned': 100,
        'suggested_for': user_ids
    }
]
workout_result = db.octofit_tracker_workout.insert_many(workouts)
print(f"✅ Created {len(workout_result.inserted_ids)} workouts")

# Create leaderboard entries
print("Creating leaderboard entries...")
leaderboard_entries = [
    {
        '_id': ObjectId(),
        'user': user_ids[0],
        'score': 850,
        'rank': 1,
        'team': marvel_id
    },
    {
        '_id': ObjectId(),
        'user': user_ids[1],
        'score': 800,
        'rank': 2,
        'team': marvel_id
    },
    {
        '_id': ObjectId(),
        'user': user_ids[2],
        'score': 900,
        'rank': 1,
        'team': dc_id
    },
    {
        '_id': ObjectId(),
        'user': user_ids[3],
        'score': 750,
        'rank': 2,
        'team': dc_id
    }
]
leaderboard_result = db.octofit_tracker_leaderboard.insert_many(leaderboard_entries)
print(f"✅ Created {len(leaderboard_result.inserted_ids)} leaderboard entries")

print("\n✅ Database populated successfully with native PyMongo!")
print(f"✅ Created {len(teams)} teams, {len(users)} users, {len(activities)} activities, {len(workouts)} workouts, {len(leaderboard_entries)} leaderboard entries")
