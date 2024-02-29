import requests
from bs4 import BeautifulSoup

# Target URLs for testing
positive_test_url = "https://xss-game.appspot.com/level1/frame"
negative_test_url = "http://dvwa.local/login.php"

# The payload to test XSS vulnerability
payload = "<script>alert('XSS')</script>"

def test_xss(url):
    # Send the payload to the target URL
    response = requests.get(url, params={'test': payload})
    
    # Use BeautifulSoup to parse the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Check if the payload is reflected in the response
    if payload in str(soup):
        print(f"Possible XSS vulnerability detected on {url}")
    else:
        print(f"No XSS vulnerability detected on {url}")

# Testing the URLs
test_xss(positive_test_url)
test_xss(negative_test_url)
