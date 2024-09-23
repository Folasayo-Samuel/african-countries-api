from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from data import get_random_countries, get_countries_by_name

# Create a FastAPI instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the route that returns random African countries
@app.get("/countries", response_model=list)
def read_countries(n: int=10):
    """
    Returns a list of 10 random African countries.
    """
    countries = get_random_countries(n)
    if not countries:
        raise HTTPException(status_code=404, detail="No countries found.")
    return countries

@app.get("/countries/{country_name}")
def get_country(country_name: str):
    """
    Finds a specific country by name from the list.
    If the country is not found, return a custom JSON response expalining the country is not in the list. 
    """

    #Convert the country name to lowercase to make the search case-insensitive
    # country_name = country_name.lower()
    country = get_countries_by_name(country_name)

    # Search for the country name to lowercase to make the search case-insensitive
    # country_name = country_name.lower()

    # Search for the country in the country_fetched_name list
    # for country in country_fetched_name:
        # if country['name'].lower() == country_name:
    if country:
            return country
        
        # If country is not found, return a 404 error with a custom message
    raise HTTPException(status_code=404, detail=f"Country '{country_name}' not found in the list.")
