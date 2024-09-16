from fastapi import FastAPI, HTTPException
from data import get_random_countries, COUNTRIES

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

@app.get("/countries/{country_name}")
def get_country(country_name: str):
    """
    Finds a specific country by name from the list.
    If the country is not found, return a custom JSON response expalining the country is not in the list. 
    """

    #Convert the country name to lowercase to make the search case-insensitive
    country_name = country_name.lower()

    # Search for the country name to lowercase to make the search case-insensitive
    country_name = country_name.lower()

    # Search for the country in the COUNTRIES list
    for country in COUNTRIES:
        if country['name'].lower() == country_name:
            return country
        
        # If country is not found, return a 404 error with a custom message
        raise HTTPException(status_code=404, detail=f"Country '{country_name}' not found in the list.")
