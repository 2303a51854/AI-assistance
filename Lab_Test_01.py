#Task-1: Country Information API
#Prompt: Act as a developer to integrate a country information API to fetch country details.It should be accepted country name as input, display capital, population, currency and region.
#Handle invalid country names and incomplete data. The output should be a country information lookup tool with structured output.
import requests
def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()[0]
        country_info = {
            "Name": data.get("name", {}).get("common", "N/A"),
            "Capital": data.get("capital", ["N/A"])[0],
            "Population": data.get("population", "N/A"),
            "Currency": list(data.get("currencies", {}).keys())[0] if data.get("currencies") else "N/A",
            "Region": data.get("region", "N/A")
        }
        return country_info
    except requests.exceptions.HTTPError:
        return {"Error": "Country not found."}
    except Exception as e:
        return {"Error": str(e)}
if __name__ == "__main__":
    country_name = input("Enter country name: ")
    info = get_country_info(country_name)
    for key, value in info.items():
        print(f"{key}: {value}")
#Justification:
#1. The code uses the `requests` library to fetch data from the REST Countries API, which is a reliable source for country information.
#2. The function `get_country_info` handles both successful responses and potential errors, ensuring that the user receives meaningful feedback even when the input is invalid.
#3. The output is structured in a clear and organized manner, making it easy for users to understand the information about the country they queried.

#Task-2: Event Countdown Timer
#Prompt: As a developer,build an event countdown page with live countdown timer, event details, registration CTA. Create JavaScript countdown logic. 
#Add animated number counters, style with modern gradients. The output should be live event countdown page with animations.
#
#Justification:
#1. Created an HTML file (event_countdown.html) with a live countdown timer using JavaScript.
#2. The timer updates every second and displays days, hours, minutes, and seconds remaining.
#3. The page features modern gradient backgrounds and a responsive design with a registration button.
#4. Event details and a call-to-action button are prominently displayed for user engagement.
