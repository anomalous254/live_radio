# live_radio

Get live radio station stream info by country using pyradios.

## Installation

```bash
pip install live_radio
```

## Usage

```python
from live_radio import get_stations_by_country

stations = get_stations_by_country("Kenya", limit=10)
for station in stations:
    print(station["name"], station["url"])
```

