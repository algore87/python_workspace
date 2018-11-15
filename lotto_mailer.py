from bs4 import BeautifulSoup
from requests import get

lotto_url = "https://www.lotto.de/lotto-6aus49/lottozahlen"
lotto_dict = {"date": "", "numbers": [], "super_nr": 0}
quote_dict = {"class": 0, "description":"", "nr_of_winners": 0, "winning_price": 0.00}
response = get(lotto_url)
response.encoding = "utf-8"

# parse html tree response.text
lotto_soup = BeautifulSoup(response.text, 'html.parser')
lotto_6_49_soup = lotto_soup.find('div', class_="WinningNumbers WinningNumbers--lotto6aus49")
lotto_winning_numbers_soup = lotto_6_49_soup.find_all('span', class_="LottoBall__circle")
lotto_date_soup = lotto_soup.find('span', class_="WinningNumbers__date")
### todo: parse win quotes with prices
lotto_6_49_quotes_soup = lotto_soup.find('div', class_= "OddsTableContainer__content")

# format data
lotto_dict["date"] = lotto_date_soup.text
for item in lotto_winning_numbers_soup:
    lotto_dict["numbers"].append(int(item.text))
lotto_dict["super_nr"] = lotto_dict["numbers"].pop()

my_numbers = [  [3, 12, 17, 26, 30, 41],
                [2, 3, 7, 10, 28, 37],
                [1, 5, 7, 12, 14, 20],
                [18, 19, 20, 25, 31, 38],
                [4, 12, 17, 25, 33, 37],
                [11, 17, 29, 33, 46, 49]]

# evaluate win
print(lotto_6_49_quotes_soup.find('div', class_="GameAmount").text)
print("€")

"""
- compare my_numbers [[],[],...] with lotto_dict["numbers"]
- max hits per list
- send mail with numbers hit
- TODO: evaluate the quote and calculate the amount of money won.
"""
