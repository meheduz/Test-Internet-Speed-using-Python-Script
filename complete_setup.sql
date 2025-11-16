-- Drop existing table if you want fresh start (OPTIONAL - will delete all data)
-- DROP TABLE IF EXISTS speed_log;

-- Create complete speed_log table with all fields
CREATE TABLE IF NOT EXISTS speed_log (
    id BIGSERIAL PRIMARY KEY,
    location_name TEXT NOT NULL,
    download_mbps DECIMAL(10,2) NOT NULL,
    upload_mbps DECIMAL(10,2) NOT NULL,
    connection_type TEXT DEFAULT 'Unknown',
    wifi_network TEXT DEFAULT 'N/A',
    device_info TEXT,
    server_location TEXT,
    ping_ms DECIMAL(8,2),
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Add columns to existing table (if table already exists)
ALTER TABLE speed_log 
ADD COLUMN IF NOT EXISTS connection_type TEXT DEFAULT 'Unknown',
ADD COLUMN IF NOT EXISTS wifi_network TEXT DEFAULT 'N/A',
ADD COLUMN IF NOT EXISTS device_info TEXT,
ADD COLUMN IF NOT EXISTS server_location TEXT,
ADD COLUMN IF NOT EXISTS ping_ms DECIMAL(8,2);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_speed_log_location ON speed_log(location_name);
CREATE INDEX IF NOT EXISTS idx_speed_log_timestamp ON speed_log(timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_speed_log_connection ON speed_log(connection_type);

-- Enable Row Level Security (RLS) for better security
ALTER TABLE speed_log ENABLE ROW LEVEL SECURITY;

-- Create policy to allow all operations (adjust as needed)
CREATE POLICY "Allow all operations" ON speed_log
FOR ALL USING (true) WITH CHECK (true);

-- Sample insert to test table
INSERT INTO speed_log (
    location_name, 
    download_mbps, 
    upload_mbps, 
    connection_type, 
    wifi_network
) VALUES (
    'Test Location', 
    50.25, 
    25.75, 
    'WiFi', 
    'Test Network'
);

-- View table structure
SELECT column_name, data_type, is_nullable, column_default 
FROM information_schema.columns 
WHERE table_name = 'speed_log' 
ORDER BY ordinal_position;