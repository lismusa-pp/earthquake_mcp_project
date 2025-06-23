from agent import fetch_earthquake_data, filter_earthquakes
from utils import prepare_data_for_sheet
from google_sheet import write_earthquakes_to_sheet
from win10toast import ToastNotifier

def run_mcp_server():
    toaster = ToastNotifier()
    print("[MCP] Starting agents...")

    data = fetch_earthquake_data()
    if not data:
        print("[MCP] No data received.")
        toaster.show_toast("Earthquake Report", "Failed to fetch data.", duration=5)
        return

    filtered = filter_earthquakes(data)
    print(f"[MCP] Found {len(filtered)} earthquakes above threshold.")

    sheet_data = prepare_data_for_sheet(filtered)
    write_earthquakes_to_sheet(sheet_data)

    print("[MCP] Report sent to Google Sheets.")

    toaster.show_toast(
        "Earthquake Report",
        f"Found {len(filtered)} earthquakes above threshold.",
        duration=10
    )
