# -*- coding: utf-8 -*-
"""
Substack Analytics - Usage Example
==================================

This example shows how to use the improved Substack Analytics system
with flexible URL input and accurate data extraction.
"""

from data_collector import SubstackDataCollector

def analyze_publication(publication_input):
    """
    Analyze a Substack publication with flexible input.
    
    Args:
        publication_input (str): Can be:
            - Publication name: "cashandcache"
            - Full URL: "https://cashandcache.substack.com"
            - URL with /feed: "https://cashandcache.substack.com/feed"
    """
    print(f"Analyzing: {publication_input}")
    print("=" * 60)
    
    # Create collector with flexible input
    collector = SubstackDataCollector(publication_input)
    
    # Run analysis
    analysis = collector.analyze_publication(limit=10)
    
    if "error" in analysis:
        print(f"Error: {analysis['error']}")
        return None
    
    # Display results
    pub = analysis['publication']
    analytics = analysis['analytics']
    
    print(f"\n[PUBLICATION OVERVIEW]")
    print(f"Name: {pub['name']}")
    print(f"URL: {pub['url']}")
    print(f"Subscribers: {pub['subscriber_count'] or 'Not available'}")
    
    print(f"\n[PERFORMANCE METRICS]")
    print(f"Posts Analyzed: {analytics['total_posts_analyzed']}")
    print(f"Average Likes per Post: {analytics['average_likes_per_post']}")
    print(f"Average Comments per Post: {analytics['average_comments_per_post']}")
    print(f"Average Shares per Post: {analytics['average_shares_per_post']}")
    print(f"Average Word Count: {analytics['average_word_count']}")
    print(f"Average Reading Time: {analytics['average_reading_time']} minutes")
    print(f"Publishing Frequency: {analytics['publishing_frequency']} posts/week")
    print(f"Total Engagement: {analytics['total_engagement']}")
    
    # Export to Excel
    excel_filename = collector.export_to_excel(analysis)
    print(f"\n[EXPORT] Excel file created: {excel_filename}")
    
    return analysis

if __name__ == "__main__":
    # Example 1: Using publication name
    print("Example 1: Using publication name")
    analyze_publication("cashandcache")
    
    print("\n" + "="*80 + "\n")
    
    # Example 2: Using full URL
    print("Example 2: Using full URL")
    analyze_publication("https://cashandcache.substack.com")
    
    print("\n" + "="*80 + "\n")
    
    # Example 3: Using URL with /feed
    print("Example 3: Using URL with /feed")
    analyze_publication("https://cashandcache.substack.com/feed")
