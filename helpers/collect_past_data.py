import fastf1 as f1


def collect_past_data(years: list[int], gp_name: str):
    race_data = []

    for year in years:
        try:
            schedule = f1.get_event_schedule(year)
            event = schedule.get_event_by_name(gp_name)

            if event is None:
                print(f"No event found for {gp_name} in {year}")
                continue

            race = event.get_race()
            race.load()

            race_results = race.results.copy()
            race_results["Year"] = year
            race_data.append(race_results)
        except Exception as e:
            print(f"An error occured while collecting data for {year}: {e}")

    return {"race": race_data}
