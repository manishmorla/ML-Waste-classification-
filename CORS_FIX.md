# Fixing "Unable to Fetch" Error

## Problem

When opening `index.html` directly (file:// protocol), browsers block CORS requests to `localhost`. This causes the "Unable to fetch" error.

## Solutions

### Solution 1: Use Local Server (Recommended) ✅

**Windows:**
1. Open Command Prompt in the `frontend` folder
2. Run: `python -m http.server 8000`
3. Open browser: `http://localhost:8000`

**Or use the provided script:**
```bash
cd frontend
start-server.bat
```

**macOS/Linux:**
```bash
cd frontend
python3 -m http.server 8000
```

### Solution 2: Check Backend is Running

Make sure the backend is running:
```bash
python backend/app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
```

### Solution 3: Verify Connection

1. Open browser console (F12)
2. Check for error messages
3. The frontend now shows a connection status indicator

### Solution 4: Browser Settings (Not Recommended)

Some browsers allow disabling CORS for development, but this is not recommended for security reasons.

## Quick Fix Steps

1. **Terminal 1 - Start Backend:**
   ```bash
   python backend/app.py
   ```

2. **Terminal 2 - Start Frontend Server:**
   ```bash
   cd frontend
   python -m http.server 8000
   ```

3. **Open Browser:**
   - Go to: `http://localhost:8000`
   - You should see "✅ Backend Connected" message

## Testing Connection

Test if backend is accessible:
```bash
curl http://localhost:5000/api/health
```

Should return:
```json
{"status": "healthy", "model_loaded": true, ...}
```

## Common Issues

### "Cannot connect to backend"
- ✅ Backend not running → Start with `python backend/app.py`
- ✅ Wrong port → Check backend is on port 5000
- ✅ Firewall blocking → Allow Python through firewall

### "CORS error"
- ✅ Use local server instead of file://
- ✅ Backend CORS is configured correctly

### "Network error"
- ✅ Check both servers are running
- ✅ Check browser console for details

## Updated Features

The frontend now includes:
- ✅ Better error messages
- ✅ Connection status indicator
- ✅ Automatic health checking
- ✅ Improved CORS handling
