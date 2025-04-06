import os
import requests
from web_scraper import get_website_text_content

def search_web(query):
    """
    Perform a web search using SerpAPI or a similar service.
    
    Args:
        query (str): The search query
        
    Returns:
        list: A list of search results, or None if the search fails
    """
    
    api_key = os.environ.get("SERPAPI_KEY")
    
    if not api_key:
        return handle_search_fallback(query)
    

    base_url = "https://serpapi.com/search"
    
    try:
        params = {
            "q": query,
            "api_key": api_key,
            "engine": "google"
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            results = []
            organic_results = data.get("organic_results", [])
            
            for result in organic_results:
                results.append({
                    "title": result.get("title", ""),
                    "link": result.get("link", ""),
                    "snippet": result.get("snippet", "")
                })
            
            return results
        else:
            return handle_search_fallback(query)
            
    except Exception as e:
        return handle_search_fallback(query)

def handle_search_fallback(query):
    """
    Fallback method for when the primary search API fails.
    Attempts to get results from a direct web scrape of a relevant page.
    
    Args:
        query (str): The search query
        
    Returns:
        list: A list with basic search results, or None if all fallbacks fail
    """
    try:
       
        clean_query = query.replace(" ", "_")
        wiki_url = f"https://en.wikipedia.org/wiki/{clean_query}"
        
        content = get_website_text_content(wiki_url)
        
        if content:
            
            return [{
                "title": f"Wikipedia: {query}",
                "link": wiki_url,
                "snippet": content[:200] + "..." if len(content) > 200 else content
            }]
        
        return None
    except:
        return None
