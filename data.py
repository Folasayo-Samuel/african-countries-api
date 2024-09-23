from pymongo import MongoClient
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


        """Fetch a specific country by name from MongoDB"""
        #Use MongoDB Atlas Search with the 'search' aggregation pipeline
        pipeline = [
              {
                    "$search":{
                          "index": "default", #Use the default search index 
                          "text":{
                                "query": country_name, 
                                "path": "name",  #Path to the field in which to search
                                "fuzzy":{
                                      "maxEdits":1 #Allows up to 1 character be wrong (for fuzziness)
                                }
                          }
                    }
              },
              {
                    "$limit": 1
              },
              {
                    "$project":{
                          "_id":0
                    }
              }
        ]

# Run the aggregation pipeline
        result = list(countries_collection.aggregate(pipeline))

#Return the first matching result or None if no match found
        return result[0] if result else None

