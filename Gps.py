import serial

def parse_GPGGA(sentence):
    try:
        parts = sentence.split(',')
        if parts[0] == "$GPGGA" and len(parts) > 5 and parts[6] != '0':  # Valid fix
            lat, lat_dir, lon, lon_dir = parts[2:6]
            if lat and lon:
                lat_deg = int(float(lat) / 100)
                lat_min = float(lat) - lat_deg * 100
                latitude = lat_deg + lat_min / 60
                if lat_dir == 'S': latitude = -latitude
                
                lon_deg = int(float(lon) / 100)
                lon_min = float(lon) - lon_deg * 100
                longitude = lon_deg + lon_min / 60
                if lon_dir == 'W': longitude = -longitude
                
                return latitude, longitude
    except:
        pass
    return None, None

# Use /dev/serial0 for GPIO UART (9600 baud typical for NEO-6M)
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

try:
    while True:
        line = ser.readline().decode('ascii', errors='replace').strip()
        print("Line:", line)
        if line.startswith('$GPGGA'):
            lat, lon = parse_GPGGA(line)
            if lat and lon:
                print(f"GPS Fix - Lat: {lat:.6f}, Lon: {lon:.6f}")
            else:
                print("No fix yet (check outdoors)")
except KeyboardInterrupt:
    print("Stopped")
finally:
    ser.close()
