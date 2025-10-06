# My Stack Analyst - Substack Analytics Tool

## 🚀 Project Overview
This is a comprehensive Substack analytics tool that helps you analyze any Substack publication's performance, engagement metrics, and content insights.

## 📁 Project Structure
```
My Stack Analyst/
├── data_collector.py          # Main data collection and analysis engine
├── web_dashboard.py           # Web-based dashboard interface
├── start_dashboard.py         # Easy launcher for web dashboard
├── requirements_web.txt       # Python dependencies for web dashboard
├── templates/
│   └── dashboard.html         # Web dashboard HTML template
├── static/                    # Static web assets
├── __pycache__/              # Python cache files
└── *.xlsx                    # Generated Excel reports
```

## 🛠️ Features

### Data Collection (`data_collector.py`)
- **RSS Feed Analysis**: Fetches all posts from Substack RSS feeds
- **Engagement Metrics**: Extracts likes, comments, shares, and restacks
- **Subscriber Count**: Attempts to extract subscriber information
- **Content Analysis**: Word count, reading time, and content insights
- **Excel Export**: Generates comprehensive Excel reports with multiple sheets
- **Comprehensive Scraping**: Multiple methods to extract data from Substack pages

### Web Dashboard (`web_dashboard.py`)
- **Beautiful Interface**: Modern web-based analytics dashboard
- **Real-time Analysis**: Run fresh analysis through the web interface
- **Interactive Charts**: Visual representation of analytics data
- **Easy URL Input**: Enter any Substack publication URL
- **Export Functionality**: Download results as Excel files

## 🚀 How to Run

### Option 1: Web Dashboard (Recommended)
```bash
cd "C:\Users\User\My Stack Analyst"
python start_dashboard.py
```
Then open http://localhost:5000 in your browser

### Option 2: Direct Analysis
```bash
cd "C:\Users\User\My Stack Analyst"
python data_collector.py
```

### Option 3: Web Dashboard Direct
```bash
cd "C:\Users\User\My Stack Analyst"
python web_dashboard.py
```

## 📊 What You Can Analyze

1. **Publication Overview**
   - Publication name and URL
   - Subscriber count (when available)
   - Last updated information

2. **Post Performance**
   - Individual post engagement metrics
   - Top performing posts
   - Average engagement rates
   - Publishing frequency

3. **Content Insights**
   - Word count analysis
   - Reading time estimates
   - Content length trends

4. **Engagement Analysis**
   - Likes, comments, shares, restacks
   - Total engagement scores
   - Engagement trends over time

## 🔧 Configuration

To analyze a different Substack publication, edit line 953 in `data_collector.py`:
```python
PUBLICATION_URL = "https://your-publication.substack.com"
```

Or use the web dashboard to enter any URL interactively.

## 📋 Requirements

Install dependencies with:
```bash
pip install -r requirements_web.txt
pip install requests beautifulsoup4 openpyxl lxml
```

## 📈 Output

The tool generates:
- **Console Output**: Real-time analysis progress and results
- **Excel Files**: Comprehensive reports with multiple sheets
- **Web Dashboard**: Interactive web interface
- **Debug Files**: HTML files for troubleshooting (when needed)

## 🎯 Use Cases

- **Content Creators**: Analyze your own Substack performance
- **Researchers**: Study Substack publication trends
- **Marketers**: Understand audience engagement patterns
- **Analysts**: Generate detailed performance reports

## 🔒 Privacy Note

This tool only accesses publicly available data from Substack RSS feeds and public pages. It respects Substack's terms of service and doesn't access private or subscriber-only content.

## 📝 Last Updated
Created: October 4, 2025
Location: C:\Users\User\My Stack Analyst

---
*Your Substack analytics project is safely backed up and ready to use!* 🎉
