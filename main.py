from fastapi import FastAPI
from data import get_random_countries

# Create a FastAPI instance
app = FastAPI()

# Define the route that returns random African countries
@app.get("/countries", response_model=list)
def read_countries():
    """
    Returns a list of 10 random African countries.
    """
    countries = get_random_countries()
    return countries

