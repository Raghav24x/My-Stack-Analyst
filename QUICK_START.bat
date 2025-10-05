@echo off
echo ========================================
echo    My Stack Analyst - Quick Start
echo ========================================
echo.
echo Starting Substack Analytics Dashboard...
echo Dashboard will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

cd /d "%~dp0"
python web_dashboard.py

pause

