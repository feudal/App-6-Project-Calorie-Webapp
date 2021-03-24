import requests
from bs4 import BeautifulSoup


class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage
    important!!! pass name of the city with hyphen e.x. New york - new-york
    """
    url = 'timeanddate.com/weather'

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def get(self):
        r = requests.get('https://www.timeanddate.com/weather/'+self.country+'/'+self.city)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        temp = soup.select('#qlook .h2')[0]
        temp = temp.text.replace('\xa0°C', '')

        return int(temp)
