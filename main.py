from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import REGISTRY
from fastapi.responses import PlainTextResponse
from monitoring import metrics_middleware, get_metrics, logger  # Import logging and metrics
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

# Add metrics middleware
app.middleware("http")(metrics_middleware)

# Add logging to all routes
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


# Define the route that returns random African countries
@app.get("/countries", response_model=list)
def read_countries(n: int = 10):
    """
    Returns a list of 10 random African countries.
    """
    logger.info("Fetching random countries...")
    countries = get_random_countries(n)
    if not countries:
        logger.error("No countries found.")
        raise HTTPException(status_code=404, detail="No countries found.")
    logger.info(f"Countries found: {countries}")
    return countries

@app.get("/countries/{country_name}")
def get_country(country_name: str):
    """
    Finds a specific country by name from the list.
    If the country is not found, return a custom JSON response explaining the country is not in the list.
    """
    logger.info(f"Looking for country: {country_name}")
    country = get_countries_by_name(country_name)
    if country:
        logger.info(f"Country found: {country}")
        return country
    logger.error(f"Country '{country_name}' not found.")
    raise HTTPException(status_code=404, detail=f"Country '{country_name}' not found in the list.")

# Prometheus metrics endpoint
@app.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    return await get_metrics()