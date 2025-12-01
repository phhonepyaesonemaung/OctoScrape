from bs4 import BeautifulSoup


with open('home.html', 'r') as html_file:
    content = html_file.read() # this is reading the file
    soup = BeautifulSoup( content , 'lxml')
    tags = soup.find_all('h5')
    for tag in tags:
        print(tag.text)

    