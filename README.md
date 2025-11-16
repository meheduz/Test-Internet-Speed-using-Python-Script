# Internet Speed Test Monitor

A cross-platform Python tool for monitoring and tracking internet speed with location-based analysis and network information storage.

## Features

- Real-time internet speed testing (download/upload)
- Location-based speed tracking
- Automatic WiFi network detection
- Connection type identification
- Historical data analysis
- Multi-platform support (macOS, Linux, Windows, Android)
- Supabase database integration

## Prerequisites

- Python 3.x
- Internet connection
- Supabase account (free tier available)

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/meheduz/Test-Internet-Speed-using-Python-Script.git
cd Test-Internet-Speed-using-Python-Script
```

### 2. Create Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Android (Termux):**
```bash
pkg install python git termux-api
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
```

Edit `.env` file with your Supabase credentials:
```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

### 5. Setup Database

Execute this SQL in your Supabase SQL Editor:

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

## Usage

### Run Speed Test
```bash
python enhanced_speed_test.py
```
Enter your location when prompted. The script will:
- Detect your WiFi network automatically
- Measure download and upload speeds
- Save results to database

### View All Results
```bash
python view_data.py
```

### View Location-Specific Data
```bash
python location_data.py
```
Shows historical data and average speeds for a specific location.

### Test Database Connection
```bash
python check_connection.py
```

## Project Structure

```
.
├── config.py                 # Environment configuration
├── enhanced_speed_test.py    # Main speed test with network detection
├── speed_test.py             # Basic speed test
├── view_data.py              # Display all test results
├── location_data.py          # Location-based analysis
├── check_connection.py       # Database connection test
├── complete_setup.sql        # Database setup script
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # Documentation
```

## Database Schema

| Column | Type | Description |
|--------|------|-------------|
| id | BIGSERIAL | Primary key |
| location_name | TEXT | Test location |
| download_mbps | DECIMAL(10,2) | Download speed in Mbps |
| upload_mbps | DECIMAL(10,2) | Upload speed in Mbps |
| connection_type | TEXT | WiFi/Unknown |
| wifi_network | TEXT | WiFi network name |
| timestamp | TIMESTAMPTZ | Test timestamp |

## Platform Support

| Platform | WiFi Detection | Status |
|----------|----------------|--------|
| macOS | networksetup, airport | Supported |
| Linux | iwgetid, nmcli | Supported |
| Windows | netsh wlan | Supported |
| Android (Termux) | termux-wifi-connectioninfo | Supported |

## Technologies

- **Python 3.x** - Core programming language
- **Supabase** - PostgreSQL database and backend
- **speedtest-cli** - Internet speed testing
- **python-dotenv** - Environment variable management

## Security

- Never commit `.env` file to version control
- Keep Supabase credentials private
- Use environment variables for sensitive data
- `.env` is automatically ignored by Git

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

**Meheduz Zaman**
- GitHub: [@meheduz](https://github.com/meheduz)
- Email: 2023331064@student.sust.edu

## Acknowledgments

- Supabase for database infrastructure
- speedtest-cli for speed testing functionality