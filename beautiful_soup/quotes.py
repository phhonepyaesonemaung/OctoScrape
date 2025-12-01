from bs4 import BeautifulSoup
import requests
import time
print("Type of Quotes")
user_type = input ("Enter the type of quote you want >")
def fetch_quotes():
        html_text = requests.get('https://quotes.toscrape.com/').text
        soup = BeautifulSoup(html_text,'lxml')
        card = soup.find_all('div', class_='quote')
        for index,quote in enumerate(card):
            tags = quote.find_all('div', class_='tags')[0].text
            if user_type in tags:
                with open(f'quotes/{index}.txt', 'w') as f:
                     
                    text = quote.find_all('span', class_='text')[0].text
                    author = quote.find_all('small', class_='author')[0].text
                    about = quote.find_all('a')[0]['href']
            
                    f.write(f'{text} \n')
                    f.write(f'{author}\n')
                    f.write(f'https://quotes.toscrape.com{about}')

if __name__ == '__main__':
    while True:
        fetch_quotes()
        wait_time = 10
        print(f'Waiting for {wait_time} seconds...')
        time.sleep(wait_time*60)
