import requests
from bs4 import BeautifulSoup

def scrape_with_id(url, target_id):
    """
    Scrapes a website and returns all HTML tags with the specified ID and their descendants.

    Args:
        url: The URL of the website to scrape.
        target_id: The ID of the HTML element to target.

    Returns:
        A list of BeautifulSoup Tag objects, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        target_elements = soup.find_all(id=target_id)

        if not target_elements:
            print(f"No elements found with ID: {target_id}")
            return None

        return target_elements

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def scrape_with_class(url, target_class):
    """
    Scrapes a website and returns all HTML tags with the specified class and their descendants.

    Args:
        url: The URL of the website to scrape.
        target_class: The class of the HTML element to target.

    Returns:
        A list of BeautifulSoup Tag objects, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        target_elements = soup.find_all(class_=target_class)

        if not target_elements:
            print(f"No elements found with class: {target_class}")
            return None

        return target_elements

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter the URL: ")
    id_or_class = input("Enter 'id' or 'class': ")
    target_value = input("Enter the ID or class value: ")

    if id_or_class.lower() == 'id':
        results = scrape_with_id(url, target_value)
    elif id_or_class.lower() == 'class':
        results = scrape_with_class(url, target_value)
    else:
        print("Invalid input for 'id' or 'class'.")
        results = None

    if results:
        for element in results:
            print(element.prettify()) #prettify makes the html more readable.