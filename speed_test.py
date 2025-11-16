from supabase import create_client
import speedtest
from datetime import datetime
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

location_name = input("Enter location name: ")

st = speedtest.Speedtest()
st.get_best_server()
download_speed = st.download() / 1_000_000
upload_speed = st.upload() / 1_000_000

print(f"Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")

data = {
    "location_name": location_name,
    "download_mbps": download_speed,
    "upload_mbps": upload_speed,
    "timestamp": datetime.now().isoformat()
}

response = supabase.table("speed_log").insert(data).execute()
print("Data saved to Supabase")