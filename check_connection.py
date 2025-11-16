from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    response = supabase.table("speed_log").select("count").execute()
    
    print("✅ Database connection successful!")
    print(f"📊 Total records: {len(response.data)}")
    
    latest = supabase.table("speed_log").select("*").order("timestamp", desc=True).limit(1).execute()
    
    if latest.data:
        record = latest.data[0]
        print(f"🏠 Latest: {record['location_name']}")
        print(f"⬇️  Download: {record['download_mbps']} Mbps")
        print(f"⬆️  Upload: {record['upload_mbps']} Mbps")
    else:
        print("📭 No data found")
        
except Exception as e:
    print("❌ Connection failed!")
    print(f"Error: {e}")