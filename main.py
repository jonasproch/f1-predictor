import fastf1 as f1
from datetime import datetime as dt
from helpers.load_config import load_config

if __name__ == "__main__":
    # Load config
    config = load_config()

    # Enable caching
    f1.Cache.enable_cache(config.get("App", "temp_folder"))

    # Years to gather data from
    past_years = int(config.get("Prediction", "past_years"))
    current_year = dt.now().year
    years = [year for year in range(current_year - past_years, current_year)]

    grand_prix = "Miami Grand Prix"

    for year in years:
        schedule = f1.get_event_schedule(year)
        event = schedule.get_event_by_name(grand_prix)
        race = event.get_race()
        race.load()
        print(race.results)
