from country_data import country_full_name, adjacent_countries

def get_country_full_name(country_code):
    normalized_country_code = country_code.upper()
    return country_full_name.get(normalized_country_code)

def get_adjacent_countries(country_code):
    normalized_country_code = country_code.upper()
    return adjacent_countries.get(normalized_country_code)
