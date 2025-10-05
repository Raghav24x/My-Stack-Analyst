@echo off
echo Starting Substack Analytics Web Dashboard...
echo ================================================
echo.
echo Installing requirements...
pip install -r requirements_web.txt
echo.
echo Starting web dashboard...
echo Dashboard will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python web_dashboard.py
pause
