from agent import fetch_earthquake_data, filter_earthquakes
from utils import prepare_data_for_sheet
from google_sheet import write_earthquakes_to_sheet

def run_mcp_server():
    print("[MCP] Starting agents...")

    data = fetch_earthquake_data()
    if not data:
        print("[MCP] No data received.")
        return

    filtered = filter_earthquakes(data)
    print(f"[MCP] Found {len(filtered)} earthquakes above threshold.")

    sheet_data = prepare_data_for_sheet(filtered)
    write_earthquakes_to_sheet(sheet_data)

    print("[MCP] Report sent to Google Sheets.")
 


