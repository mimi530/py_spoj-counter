import requests
nick = input("Podaj nick uzytkownika: ")
url = 'http://pl.spoj.com/users/' + nick
odpowiedz = requests.get(url)
strona = odpowiedz.content
from bs4 import BeautifulSoup
soup = BeautifulSoup(strona, 'html.parser')
zadania = soup.find('table', class_='table table-condensed')
zadania = zadania.find_all('td')
licznik = 0
for zadanie in zadania:
    if zadanie.get_text() != '':
        licznik+=1
print(licznik)