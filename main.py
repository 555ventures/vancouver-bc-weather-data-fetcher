import webbrowser
from urllib.parse import urlencode


# Function to generate a URL for climate data based on year and month
def generate_climate_data_url(year: int, month: int) -> str:
    base_url = "https://climate.weather.gc.ca/climate_data/hourly_data_e.html"

    # Dictionary of query parameters for the URL
    params = {
        "hlyRange": "2013-06-11|2024-10-06",  # Range for hourly data
        "dlyRange": "2013-06-13|2024-10-06",  # Range for daily data
        "mlyRange": "|",  # Range for monthly data (empty in this case)
        "StationID": 51442,  # Weather station ID for Vancouver
        "Prov": "BC",  # Province (British Columbia)
        "urlExtension": "_e.html",  # URL extension for English version
        "searchType": "stnName",  # Search by station name
        "optLimit": "yearRange",  # Limit option set to year range
        "StartYear": 1840,  # Start year for available data
        "EndYear": 2024,  # End year for available data
        "selRowPerPage": 25,  # Number of rows per page in results
        "Line": 41,  # Line number (significance unclear, might be related to station)
        "searchMethod": "contains",  # Search method for station name
        "txtStationName": "vancouver",  # Station name to search for
        "timeframe": 1,  # Timeframe (1 likely means hourly)
        "time": "LST",  # Time format (LST = Local Standard Time)
        "Year": year,  # Year for requested data
        "Month": month,  # Month for requested data
        "Day": 11,  # Day (fixed to 11th of each month)
    }

    # Construct query string and full URL
    query_string = urlencode(params)
    full_url = f"{base_url}?{query_string}#"
    return full_url


# Function to generate a list of year-month pairs for the desired date range
def get_year_month_range():
    start_year, start_month = 2013, 7  # Start from July 2013
    end_year, end_month = 2024, 8  # End at August 2024

    year_month_list = []
    current_year, current_month = start_year, start_month

    # Generate list of year-month pairs
    while (current_year, current_month) <= (end_year, end_month):
        year_month_list.append((current_year, current_month))

        # Move to the next month, incrementing year if necessary
        if current_month == 12:
            current_year += 1
            current_month = 1
        else:
            current_month += 1

    return year_month_list


# Main execution
year_month_range = get_year_month_range()
for year, month in year_month_range:
    # Generate and open URL for each year-month pair
    url = generate_climate_data_url(year, month)
    input(
        "Press Enter to open the next URL..."
    )  # Wait for user input before opening each URL
    webbrowser.open(url)  # Open URL in default web browser
