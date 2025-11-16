from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

location = input("Location name দিন: ")

response = supabase.table("speed_log").select("*").eq("location_name", location).order("timestamp", desc=True).execute()

if response.data:
    print(f"\n{location} - Internet Speed History:")
    print("-" * 50)
    for record in response.data:
        print(f"Download: {record['download_mbps']:.2f} Mbps")
        print(f"Upload: {record['upload_mbps']:.2f} Mbps")
        if record.get('connection_type'):
            print(f"Connection: {record['connection_type']}")
        if record.get('wifi_network') and record['wifi_network'] != 'N/A':
            print(f"WiFi: {record['wifi_network']}")
        print(f"Time: {record['timestamp'][:19]}")
        print("-" * 30)
    
    avg_down = sum(r['download_mbps'] for r in response.data) / len(response.data)
    avg_up = sum(r['upload_mbps'] for r in response.data) / len(response.data)
    
    print(f"Average Speed:")
    print(f"Download: {avg_down:.2f} Mbps")
    print(f"Upload: {avg_up:.2f} Mbps")
else:
    print(f"No data found for '{location}'.")