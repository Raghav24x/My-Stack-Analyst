# -*- coding: utf-8 -*-
"""
Test script for the web dashboard
"""

import requests
import time
import subprocess
import sys
import os

def test_dashboard():
    """Test if the dashboard is working."""
    print("Testing Substack Analytics Web Dashboard...")
    print("=" * 50)
    
    # Wait a moment for the server to start
    print("Waiting for server to start...")
    time.sleep(3)
    
    try:
        # Test the main page
        response = requests.get('http://localhost:5000', timeout=10)
        if response.status_code == 200:
            print("✅ Dashboard is running successfully!")
            print("🌐 Open your browser and go to: http://localhost:5000")
            print("📊 You can now analyze any Substack publication visually!")
            return True
        else:
            print(f"❌ Dashboard returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to dashboard. Make sure it's running.")
        print("💡 Try running: python web_dashboard.py")
        return False
    except Exception as e:
        print(f"❌ Error testing dashboard: {e}")
        return False

if __name__ == "__main__":
    test_dashboard()
