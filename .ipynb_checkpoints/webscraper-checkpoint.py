import requests
from bs4 import BeautifulSoup
from datetime import datetime

def save_article_to_txt(url, filename):
    try:
        # Set the timeout to 60 seconds (1 minute)
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = ''
        for paragraph in soup.find_all('p'):
            article_text += paragraph.get_text() + '\n'
        
        folder_name = os.getcwd() + "/articles_txt"
        os.makedirs(folder_name, exist_ok=True)  # Create the folder if it doesn't exist
        file_path = os.path.join(folder_name, filename)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(article_text)
        return 1  # Success flag: 1 indicates successful retrieval and save
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return 0  # Success flag: 0 indicates unsuccessful retrieval


