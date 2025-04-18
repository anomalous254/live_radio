from pyradios import RadioBrowser

def get_unique_stations(stations):
    seen_urls = set()
    unique_stations = []
    for station in stations:
        stream_url = station.get("url_resolved") or station.get("url")
        if stream_url and stream_url not in seen_urls:
            seen_urls.add(stream_url)
            unique_stations.append({
                "name": station.get("name"),
                "favicon": station.get("favicon"),
                "homepage": station.get("homepage"),
                "url": stream_url,
            })
    return unique_stations

def get_stations_by_country(country: str, limit: int = 50):
    rb = RadioBrowser()
    results = rb.search(
        country=country,
        hidebroken=True,
        order="votes",
    )
    return get_unique_stations(results)[:limit]
