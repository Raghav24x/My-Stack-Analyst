#!/usr/bin/env python3
"""
Cleanup script to remove unnecessary files from the Substack Analytics directory.
This will keep only the essential files needed to run the analytics tool.
"""

import os
import glob
from datetime import datetime

def cleanup_files():
    """Remove clutter files and keep only essential ones."""
    
    # Files to keep (essential)
    essential_files = {
        'data_collector.py',
        'substack_article.md', 
        'usage_example.py',
        '__init__.py'
    }
    
    # Directories to keep
    essential_dirs = {
        '__pycache__'
    }
    
    # Patterns for files to delete
    patterns_to_delete = [
        'accurate_*.py',
        'advanced_*.py',
        'analytics_*.py',
        'analyze_*.py',
        'clean_*.py',
        'comprehensive_*.py',
        'developer_*.py',
        'enhanced_*.py',
        'final_*.py',
        'minimal_*.py',
        'quality_*.py',
        'realistic_*.py',
        'real_*.py',
        'rss_*.py',
        'run_*.py',
        'safe_*.py',
        'simple_*.py',
        'test_*.py',
        'ultra_*.py',
        'visualization.py',
        'debug_*.html',
        'login',
        'logout',
        '='
    ]
    
    # Get all files in current directory
    current_dir = os.getcwd()
    all_files = os.listdir(current_dir)
    
    deleted_count = 0
    kept_count = 0
    
    print("Starting cleanup of Substack Analytics directory...")
    print(f"Current directory: {current_dir}")
    print("=" * 60)
    
    # Delete files matching patterns
    for pattern in patterns_to_delete:
        matching_files = glob.glob(pattern)
        for file in matching_files:
            if os.path.isfile(file):
                try:
                    os.remove(file)
                    print(f"Deleted: {file}")
                    deleted_count += 1
                except Exception as e:
                    print(f"Could not delete {file}: {e}")
    
    # Keep only the most recent Excel file
    excel_files = glob.glob('substack_analytics_cashandcache_*.xlsx')
    if len(excel_files) > 1:
        # Sort by modification time, keep the newest
        excel_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        files_to_delete = excel_files[1:]  # Keep the first (newest), delete the rest
        
        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"Deleted old Excel: {file}")
                deleted_count += 1
            except Exception as e:
                print(f"Could not delete {file}: {e}")
    
    # Remove empty directories
    try:
        if os.path.exists('substack-analytics') and os.path.isdir('substack-analytics'):
            os.rmdir('substack-analytics')
            print("Deleted empty directory: substack-analytics")
            deleted_count += 1
    except Exception as e:
        print(f"Could not delete directory: {e}")
    
    # Count remaining files
    remaining_files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]
    kept_count = len(remaining_files)
    
    print("=" * 60)
    print(f"Cleanup complete!")
    print(f"Files deleted: {deleted_count}")
    print(f"Files kept: {kept_count}")
    print("\nEssential files remaining:")
    for file in sorted(remaining_files):
        print(f"   - {file}")
    
    print("\nTo run analytics: python data_collector.py")

if __name__ == "__main__":
    cleanup_files()
