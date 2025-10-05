# -*- coding: utf-8 -*-
"""
Substack Analytics Web Dashboard
A beautiful web interface for displaying Substack analytics data
"""

from flask import Flask, render_template, jsonify, request
import json
import os
from datetime import datetime
from data_collector import SubstackDataCollector

app = Flask(__name__)

def load_analytics_data(publication_name):
    """Load analytics data from the most recent Excel file or run fresh analysis."""
    try:
        # Look for the most recent Excel file
        excel_files = [f for f in os.listdir('.') if f.startswith(f'substack_analytics_{publication_name}_') and f.endswith('.xlsx')]
        
        if excel_files:
            # Get the most recent file
            latest_file = max(excel_files, key=os.path.getctime)
            print(f"Loading data from: {latest_file}")
            
            # For now, we'll run fresh analysis to get the data
            # In a production environment, you might want to parse the Excel file
            collector = SubstackDataCollector(f"https://{publication_name}.substack.com")
            return collector.analyze_publication()
        else:
            # No existing file, run fresh analysis
            print("No existing data found, running fresh analysis...")
            collector = SubstackDataCollector(f"https://{publication_name}.substack.com")
            return collector.analyze_publication()
    except Exception as e:
        print(f"Error loading analytics data: {e}")
        return None

@app.route('/')
def dashboard():
    """Main dashboard page."""
    return render_template('dashboard.html')

@app.route('/api/analytics/<publication_name>')
def get_analytics(publication_name):
    """API endpoint to get analytics data for a publication."""
    try:
        data = load_analytics_data(publication_name)
        if data and 'error' not in data:
            return jsonify({
                'success': True,
                'data': data
            })
        else:
            return jsonify({
                'success': False,
                'error': data.get('error', 'Failed to load analytics data')
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/run_analysis', methods=['POST'])
def run_analysis():
    """API endpoint to run fresh analysis."""
    try:
        data = request.get_json()
        publication_url = data.get('publication_url', '')
        
        if not publication_url:
            return jsonify({
                'success': False,
                'error': 'Publication URL is required'
            })
        
        collector = SubstackDataCollector(publication_url)
        analysis = collector.analyze_publication()
        
        if 'error' in analysis:
            return jsonify({
                'success': False,
                'error': analysis['error']
            })
        
        # Also export to Excel
        excel_filename = collector.export_to_excel(analysis)
        
        return jsonify({
            'success': True,
            'data': analysis,
            'excel_file': excel_filename
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Create static directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
    
    print("Starting Substack Analytics Web Dashboard...")
    print("Dashboard will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    
    app.run(debug=False, host='0.0.0.0', port=5000)
