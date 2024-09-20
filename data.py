from dotenv import load_dotenv
import os
import random


# Load environment variables from the .env file
load_dotenv()

# Access environment variables
mongodb_uri = os.getenv("MONGODB_URI")

# Using the MongoDB connection string
from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client["africa_db"]

# Fetch the African countries collection
countries_collection = db["countries"]

# List of 10 hardcoded African countries with name, population, and capital
# COUNTRIES = [
#     {'name': 'Nigeria', 'population': '180 million', 'capital': 'Abuja'},
#     {'name': 'Ghana', 'population': '80 million', 'capital': 'Accra'},
#     {'name': 'Kenya', 'population': '53 million', 'capital': 'Nairobi'},
#     {'name': 'South Africa', 'population': '59 million', 'capital': 'Pretoria'},
#     {'name': 'Egypt', 'population': '102 million', 'capital': 'Cairo'},
#     {'name': 'Morocco', 'population': '36 million', 'capital': 'Rabat'},
#     {'name': 'Ethiopia', 'population': '115 million', 'capital': 'Addis Ababa'},
#     {'name': 'Ivory Coast', 'population': '26 million', 'capital': 'Yamoussoukro'},
#     {'name': 'Uganda', 'population': '45 million', 'capital': 'Kampala'},
#     {'name': 'Senegal', 'population': '17 million', 'capital': 'Dakar'},
# ]

def get_random_countries(n=10):
    """Return a list of n random African countries from MongoDB."""

    # Fetch all countries from the collection
    countries = list(countries_collection.find({}, {"_id":0})) # Exclude MongoDB's _id field
    return random.sample(countries, k=min(n, len(countries)))

def get_countries_by_name(country_name):
    """Fetch a specific country by name using MongoDB Atlas Search."""

    # Use MongoDB Atlas Search with the 'search' aggregation pipeline
    pipeline = [
        {
            "$search": {
                "index": "default", # Use the default search index or a custom one if created
                "text":{
                    "query": country_name,
                    "path": "name", # The field to search (e.g., 'name')
                    "fuzzy":{
                        "maxEdits": 1 # Allows up to 1 character to be wrong (for fuzziness)
                    }
                }
            }
        },
        {
            "$limit":1
        },
        {
            "$project": {
                "_id":0,
            }
        }
    ]

# Run the aggregation pipeline
    result = list(countries_collection.aggregate(pipeline))


# Return the first matching result or None if no match found
    return result[0] if result else None



# def get_countries_by_name(country_name):
#         """Fetch a specific country by name from MongoDB"""
#         country = countries_collection.find_one({"name":{"$regex": f"^{country_name}$", "$options":"i"}}, {"_id":0})
#         return country

