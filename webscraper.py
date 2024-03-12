import requests
from bs4 import BeautifulSoup

def print_headings_and_application_names():
    url = "https://www.python.org/about/apps/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print headings
    print("Headings:")
    headings = soup.find_all('h1')
    for heading in headings:
        print(heading.get_text())

    # Print application names
    print("\nApplication Names:")
    links = soup.find_all('a', href=lambda href: href and '/apps/' in href)
    for link in links:
        application_name = link.get_text()
        print(application_name)

if __name__ == "__main__":
    print_headings_and_application_names()
