# -*- coding: utf-8 -*-
"""
Substack Analytics Web Dashboard Launcher
Simple script to start the web dashboard
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages for the web dashboard."""
    print("Installing web dashboard requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_web.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def start_dashboard():
    """Start the web dashboard."""
    print("🚀 Starting Substack Analytics Web Dashboard...")
    print("=" * 60)
    print("Dashboard will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        # Import and run the web dashboard
        from web_dashboard import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError as e:
        print(f"❌ Error importing web dashboard: {e}")
        print("Make sure all requirements are installed.")
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")

if __name__ == "__main__":
    print("Substack Analytics Web Dashboard Launcher")
    print("=" * 50)
    
    # Check if requirements are installed
    try:
        import flask
        print("✅ Flask is already installed")
    except ImportError:
        print("📦 Installing required packages...")
        if not install_requirements():
            print("❌ Failed to install requirements. Please install manually:")
            print("   pip install -r requirements_web.txt")
            sys.exit(1)
    
    # Start the dashboard
    start_dashboard()
