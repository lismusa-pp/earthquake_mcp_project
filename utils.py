from datetime import datetime

def format_time(timestamp_ms):
    return datetime.utcfromtimestamp(timestamp_ms / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')

def prepare_data_for_sheet(earthquakes):
    return [
        [
            format_time(eq["time"]),
            eq["place"],
            eq["magnitude"],
            eq["depth"],
            eq["url"]
        ]
        for eq in earthquakes
    ]
