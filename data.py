import random

# List of 10 hardcoded African countries with name, population, and capital
COUNTRIES = [
    {'name': 'Nigeria', 'population': '180 million', 'capital': 'Abuja'},
    {'name': 'Ghana', 'population': '80 million', 'capital': 'Accra'},
    {'name': 'Kenya', 'population': '53 million', 'capital': 'Nairobi'},
    {'name': 'South Africa', 'population': '59 million', 'capital': 'Pretoria'},
    {'name': 'Egypt', 'population': '102 million', 'capital': 'Cairo'},
    {'name': 'Morocco', 'population': '36 million', 'capital': 'Rabat'},
    {'name': 'Ethiopia', 'population': '115 million', 'capital': 'Addis Ababa'},
    {'name': 'Ivory Coast', 'population': '26 million', 'capital': 'Yamoussoukro'},
    {'name': 'Uganda', 'population': '45 million', 'capital': 'Kampala'},
    {'name': 'Senegal', 'population': '17 million', 'capital': 'Dakar'},
]

def get_random_countries(n=10):
    """Return a list of n random African countries."""
    return random.sample(COUNTRIES, k=n)

