from supabase import create_client
import speedtest
import subprocess
import platform
from datetime import datetime
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_wifi_info():
    try:
        system = platform.system()
        
        # macOS
        if system == "Darwin":
            for interface in ['en0', 'en1']:
                result = subprocess.run(['networksetup', '-getairportnetwork', interface], 
                                      capture_output=True, text=True)
                if "Current Wi-Fi Network:" in result.stdout:
                    wifi_name = result.stdout.split(": ")[1].strip()
                    return "WiFi", wifi_name
            
            result = subprocess.run(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], 
                                  capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if ' SSID:' in line:
                    wifi_name = line.split(':')[1].strip()
                    if wifi_name:
                        return "WiFi", wifi_name
        
        # Linux / Android (Termux)
        elif system == "Linux":
            # Check if running on Android/Termux
            result = subprocess.run(['termux-wifi-connectioninfo'], capture_output=True, text=True)
            if result.returncode == 0 and result.stdout:
                import json
                try:
                    wifi_data = json.loads(result.stdout)
                    if 'ssid' in wifi_data and wifi_data['ssid']:
                        return "WiFi", wifi_data['ssid'].strip('"')
                except:
                    pass
            
            # Standard Linux
            result = subprocess.run(['iwgetid', '-r'], capture_output=True, text=True)
            if result.stdout.strip():
                return "WiFi", result.stdout.strip()
            
            result = subprocess.run(['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'], 
                                  capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if line.startswith('yes:'):
                    return "WiFi", line.split(':')[1]
        
        # Windows
        elif system == "Windows":
            result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], 
                                  capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if 'SSID' in line and 'BSSID' not in line:
                    wifi_name = line.split(':')[1].strip()
                    if wifi_name:
                        return "WiFi", wifi_name
        
        return "Unknown", "N/A"
    except:
        return "Unknown", "N/A"

location_name = input("📍 Enter your current location: ")

connection_type, wifi_name = get_wifi_info()
print(f"🌐 Connection: {connection_type}")
if wifi_name != "N/A":
    print(f"📶 WiFi Network: {wifi_name}")

print("🚀 Running speed test...")
st = speedtest.Speedtest()
st.get_best_server()
download_speed = st.download() / 1_000_000
upload_speed = st.upload() / 1_000_000

print(f"⬇️  Download: {download_speed:.2f} Mbps")
print(f"⬆️  Upload: {upload_speed:.2f} Mbps")

data = {
    "location_name": location_name,
    "download_mbps": download_speed,
    "upload_mbps": upload_speed,
    "connection_type": connection_type,
    "wifi_network": wifi_name,
    "timestamp": datetime.now().isoformat()
}

response = supabase.table("speed_log").insert(data).execute()
print("✅ Data saved successfully!")