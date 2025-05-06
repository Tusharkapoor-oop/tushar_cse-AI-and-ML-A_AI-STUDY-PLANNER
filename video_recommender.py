# video_recommender.py

from urllib.parse import quote_plus

def recommend_videos(topics):
    """
    Given a list of topics, returns a dict mapping
    each topic to a properly URL-encoded YouTube search URL.
    """
    base_url = "https://www.youtube.com/results?search_query="
    video_links = {}

    for topic in topics:
        # quote_plus handles spaces and special characters
        query = quote_plus(topic)
        video_links[topic] = f"{base_url}{query}"

    return video_links

