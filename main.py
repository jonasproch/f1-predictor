import fastf1 as f1
from datetime import datetime as dt
from helpers.load_config import load_config
from helpers.collect_past_data import collect_past_data

if __name__ == "__main__":
    # Load config
    config = load_config()

    # Enable caching
    f1.Cache.enable_cache(config.get("App", "cache_folder"))

    # Years to gather data from
    past_years = int(config.get("Prediction", "past_years"))
    current_year = dt.now().year
    years = [year for year in range(current_year - past_years, current_year)]

    grand_prix = "Miami Grand Prix"

    past_data = collect_past_data(years, grand_prix)
