from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.table("speed_log").select("*").execute()

print("Speed Test Results:")
print("-" * 50)
for record in response.data:
    print(f"Location: {record['location_name']}")
    print(f"Download: {record['download_mbps']:.2f} Mbps")
    print(f"Upload: {record['upload_mbps']:.2f} Mbps")
    print(f"Time: {record['timestamp']}")
    print("-" * 30)