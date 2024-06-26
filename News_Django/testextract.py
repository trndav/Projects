# import requests
# from bs4 import BeautifulSoup

# def extract_title(url):
#     # Send a GET request to the URL
#     response = requests.get(url)
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content of the webpage
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Find all elements with class 'card__article-link'
#         # titles = soup.find_all(class_='card__article-link')
#         titles = soup.find_all(class_='card__title')        
        
#         # Extract the titles from the elements
#         title_list = [title.get_text() for title in titles]
        
#         return title_list
#     else:
#         # Print an error message if the request was not successful
#         print('Error fetching webpage:', response.status_code)

# # Example URL from jutarnji.hr
# url = 'https://www.jutarnji.hr/vijesti/najcitanije'
# url2 = 'https://www.jutarnji.hr/vijesti/najcitanije'
# titles = extract_title(url)
# titles2 = extract_title(url)

# # Print the extracted titles
# lines = 0
# for title in titles:
#     lines += 1
#     print(title.strip())
# print(lines)

# Google news extract
import requests
from bs4 import BeautifulSoup

def extract_google_news_titles():
    url = "https://news.google.com/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # Find all elements with class 'ipQwMb ekueJc gEATFF RD0gLb'
        # These contain news article titles
        titles = soup.find_all(class_='ipQwMb ekueJc gEATFF RD0gLb')
        # Extract the text from the titles
        news_titles = [title.text for title in titles]
        return news_titles
    else:
        print("Failed to fetch Google News page")
        return []

# Example usage
titles = extract_google_news_titles()
for title in titles:
    print(title)