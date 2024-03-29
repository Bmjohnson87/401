#!/usr/bin/python3
# help from Tommy Taylor
import webbrowser
import requests

# The below Python script shows one possible method to return the cookie from a site that supports cookies.


# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Cookies are my favorite
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;                       .----.                             
  `. " `.                     .' " .'                     .'  o   `.
   `.  '`.                   .' ' .'                      .  o  O  .
   `.  '`.                   .' ' .'                      .   o    .
    `.    `-._           _.-' "  .'  .----.                 '----'
      `. "    '"--...--"'  . ' .'  .'  o   `.               

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
def site_cookie(cookie):
    # Send cookie back to the site
    response = requests.get(targetsite, cookies = cookie)
    return response.content



# - Generate a .html file to capture the contents of the HTTP response
def html_file(content):
    with open("response.html", "wb") as file:
        file.write(content)


# - Open it with Firefox
def firefox_webpage(html_file):
    firefox_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get("firefox").open(html_file)


response_content = site_cookie(cookie)
html_file(response_content)
print("Response captured in response.html")
firefox_webpage("response.html")

