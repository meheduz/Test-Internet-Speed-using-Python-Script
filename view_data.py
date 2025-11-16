from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.table("speed_log").select("*").execute()

print("Speed Test Results:")
print("-" * 50)
for record in response.data:
    print(f"📍 Location: {record['location_name']}")
    print(f"⬇️  Download: {record['download_mbps']:.2f} Mbps")
    print(f"⬆️  Upload: {record['upload_mbps']:.2f} Mbps")
    if record.get('connection_type'):
        print(f"🌐 Connection: {record['connection_type']}")
    if record.get('wifi_network') and record['wifi_network'] != 'N/A':
        print(f"📶 WiFi: {record['wifi_network']}")
    print(f"🕐 Time: {record['timestamp']}")
    print("-" * 30)