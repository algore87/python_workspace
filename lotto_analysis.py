import csv, os, sys, random
# 2018 lotto analysis
my_numbers = [  [3, 12, 17, 26, 30, 41],
                [2, 3, 7, 10, 28, 37],
                [1, 5, 7, 12, 14, 20],
                [18, 19, 20, 25, 31, 38],
                [4, 12, 17, 25, 33, 37],
                [11, 17, 29, 33, 46, 49]]
csv_data = []
won_data = []
# hit quote mapping
hits_to_quote_dict = {3: "Quote Kl. 8", 4: "Quote Kl. 6", 5: "Quote Kl. 4", 6: "Quote Kl. 2"}

# begin
WORKSPACE = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(WORKSPACE, 'assets', 'csv', 'LOTTO_ab_2018csv.csv')

with open(csv_file_path) as csvfile:
    reader = csv.DictReader(csvfile, restkey='Gewinnzahlen', skipinitialspace='true', delimiter=';')
    i = -1 # -1 both days, 0 only saturdays, 1 only wednesdays
    for row in reader:
        if i == -1:
            csv_data.append(dict(row))
        elif i % 2: 
            csv_data.append(dict(row))
        if i != -1:
            i += 1

# converting
for lotto_row in csv_data:
    # clean up data
    lotto_row["Superzahl"] = int(lotto_row["Superzahl"])
    ## del(lotto_row["Superzahl"])
    """
    for i in range(1,10,2):
        del(lotto_row["Quote Kl. " + str(i)])
    """
    for i in range(1, 10):
       del(lotto_row["Anz. Kl. " + str(i)]) 
    # format
    for i in range(1,10):
        if lotto_row["Quote Kl. " + str(i)] != "--":
            lotto_row["Quote Kl. " + str(i)] = lotto_row["Quote Kl. " + str(i)].replace('.', '')
            lotto_row["Quote Kl. " + str(i)] = lotto_row["Quote Kl. " + str(i)].replace(',', '.')
            lotto_row["Quote Kl. " + str(i)] = float(lotto_row["Quote Kl. " + str(i)])
    lotto_row["Gewinnzahlen"] = [int(i) for i in lotto_row["Gewinnzahlen"]]

# calculate win
money_won_max = 0.0
money_won_min = sys.maxsize
for i in range(10000):
    money_won = 0.0
    for lotto_row in csv_data:
        sz = random.randint(0,9) # random superzahl gezogen
        for x in my_numbers:
            hits = len(set(x) & set(lotto_row["Gewinnzahlen"]))
            if hits == 2 and lotto_row["Superzahl"] == sz:
                money_won += lotto_row["Quote Kl. 9"]
            if hits > 2:
                if lotto_row["Superzahl"] == sz:
                    money_won += lotto_row[hits_to_quote_dict[hits][:-1] + str(int(hits_to_quote_dict[hits][-1]) - 1)]
                else:
                    money_won += lotto_row[hits_to_quote_dict[hits]]
    if money_won > money_won_max:
        money_won_max = money_won
    if money_won < money_won_min:
        money_won_min = money_won
print("Min: " + str(money_won_min))
print("Max: " + str(money_won_max))



