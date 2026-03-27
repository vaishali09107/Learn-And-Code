from country_finding_service import get_country_full_name, get_adjacent_countries

def adjacent_country_finder():
    print("Adjacent Country Finder Application")

    country_code = input("Enter a Country Code (e.g., IN / US / NZ): ").strip().upper()

    country_name = get_country_full_name(country_code)
    adjacent_countries = get_adjacent_countries(country_code)

    if country_name is None or adjacent_countries is None:
        print("\nInvalid country code or data not available.")
        return

    print(f"\nCountry: {country_name}",end="")

    if len(adjacent_countries) == 0:
        print("Adjacent Countries: None (No land borders)")
    else:
        print("\nAdjacent Countries:")
        for adjacent_country in adjacent_countries:
            print(f"- {adjacent_country}")

if __name__ == "__main__":
    adjacent_country_finder()
