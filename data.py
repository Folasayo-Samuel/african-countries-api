from pymongo import MongoClient
import random


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
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
        """Fetch a specific country by name from MongoDB"""
        country = countries_collection.find_one({"name":{"$regex": f"^{country_name}$", "$options":"i"}}, {"_id":0})
        return country

