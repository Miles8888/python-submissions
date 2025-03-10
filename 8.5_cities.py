def describe_city(city, country='paris'):
    """Where is a city?"""
    print(f"{city.title()} is in {country.title()}.")

describe_city('paris')
describe_city('glasgow', 'scotland')
describe_city('bordeaux')