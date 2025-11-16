# 📊 Internet Speed Test Monitor

Monitor and track internet speed tests with location and network information stored in Supabase.

## 🚀 Setup

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd "Next Gen "
```

### 2. Create Virtual Environment

**Desktop (macOS/Linux/Windows):**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

**Android (Termux):**
```bash
pkg install python git
pip install virtualenv
python -m venv venv
source venv/bin/activate
# Install Termux:API for WiFi detection
pkg install termux-api
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
```
Edit `.env` and add your Supabase credentials:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

### 5. Setup Database
Run this SQL in Supabase SQL Editor:
```sql
CREATE TABLE speed_log (
    id BIGSERIAL PRIMARY KEY,
    location_name TEXT NOT NULL,
    download_mbps DECIMAL(10,2) NOT NULL,
    upload_mbps DECIMAL(10,2) NOT NULL,
    connection_type TEXT DEFAULT 'Unknown',
    wifi_network TEXT DEFAULT 'N/A',
    timestamp TIMESTAMPTZ DEFAULT NOW()
);
```

## 📋 Available Scripts

### Enhanced Speed Test (Recommended)
```bash
python enhanced_speed_test.py
```
- Auto-detects WiFi network
- Captures connection type
- Measures download/upload speed
- Saves to database

### Basic Speed Test
```bash
python speed_test.py
```
- Simple speed test
- Manual location input

### View All Data
```bash
python view_data.py
```
- Display all speed test results

### Location-Specific Data
```bash
python location_data.py
```
- View data for specific location
- Shows average speeds

### Check Connection
```bash
python check_connection.py
```
- Test database connection
- Show latest record

## 📱 Daily Usage

```bash
cd "Next Gen "
source venv/bin/activate
python enhanced_speed_test.py
```

## 🗂️ Project Structure

```
Next Gen /
├── config.py              # Configuration loader
├── enhanced_speed_test.py # Main speed test with network info
├── speed_test.py          # Basic speed test
├── view_data.py           # View all results
├── location_data.py       # Location-specific analysis
├── check_connection.py    # Database connection test
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔒 Security

- Never commit `.env` file
- Keep Supabase credentials private
- Use environment variables for sensitive data

## 📊 Database Schema

```sql
speed_log
├── id (BIGSERIAL)
├── location_name (TEXT)
├── download_mbps (DECIMAL)
├── upload_mbps (DECIMAL)
├── connection_type (TEXT)
├── wifi_network (TEXT)
└── timestamp (TIMESTAMPTZ)
```

## 🛠️ Technologies

- Python 3.x
- Supabase (PostgreSQL)
- speedtest-cli
- python-dotenv