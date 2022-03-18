#Author: Bernardo Calvo

MSG_TRANSFERTO = "Transfer to {}"
MSG_TRANSFERFROM = "Transfer from {}"
MSG_CHART = "Percentage spent by category\n"

MAX_CHAR = 30
MAX_CHAR_DESC = 23

class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description=""):
    self.ledger.append({"amount":amount, "description":description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount":-amount, "description":description})
      return True
    return False

  def get_balance(self):
    res = 0
    for obj in self.ledger:
      res += obj["amount"]
    return res

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, MSG_TRANSFERTO.format(category.name))
      category.deposit(amount, MSG_TRANSFERFROM.format(self.name))
      return True
    return False

  def check_funds(self, amount):
    return self.get_balance() >= amount
    
  def __str__(self):
    txt = self.name.center(MAX_CHAR, '*') + '\n'
    total = 0
    for obj in self.ledger:
      desc = obj["description"]
      amount = obj["amount"]
      descLen = len(desc)
      if descLen > MAX_CHAR_DESC:
        descLen = MAX_CHAR_DESC
      txt += desc[:descLen] + "{:.2f}".format(amount).rjust(MAX_CHAR-descLen) + '\n'
      total += amount
    txt += "Total: {}".format(total)
    return txt


def create_spend_chart(categories):
  txt = MSG_CHART

  spendList = calculate_spends(categories)
  total = sum(spendList)
  
  percentages = list()
  for spent in spendList:
    percentages.append(int((spent/total)*100/10)*10)

  #chart
  perc = 100
  for i in range(11):  # 100 -> ... -> 0
    value = i*10
    txt += "{}".format(perc - value).rjust(3) + "| "
    for j in range(len(percentages)):
      if perc - value <= percentages[j]:
        txt += "o  "
      else:
        txt += "   "
    txt += '\n'

  txt += "    --{}--\n".format('-'*2*len(categories))
  
  maxchar = max_category_name(categories)
  # categories names
  txt += "     "
  for i in range(maxchar):
    if i != 0:
      txt += "\n     "
    for cat in categories:
      if i >= len(cat.name):
        txt += "   "
      else:
        txt += cat.name[i] + "  "
  return txt

def calculate_spends(categories):
  res = list()
  for cat in categories:
    catSpend = 0
    for obj in cat.ledger:
      amount = obj["amount"]
      if amount < 0:
        catSpend += -amount
    res.append(catSpend)
  return res

def max_category_name(categories):
  maxchar = 0
  for cat in categories:
    catLen = len(cat.name)
    if len(cat.name) > maxchar:
      maxchar = catLen
  return maxchar

  
#Example
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))