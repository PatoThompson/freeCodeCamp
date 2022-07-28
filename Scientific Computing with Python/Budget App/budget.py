class Category:
    # Category functions are self-explanatory. For more info, search the link in README.md
    name = ''
    def __init__(self, nam):
            self.name = nam
            self.ledger = []
            self.balance = 0
            self.spent = 0

    
    def deposit(self, amount, description=None):
        if description == None: description = ''
        item = {}
        item["amount"] = amount
        item["description"] = description
        self.ledger.append(item)
        self.balance += amount

  
    def withdraw(self, amount, description=None):
        if self.check_funds(amount):
            if description == None: description = ''
            item = {}
            item["amount"] = -amount
            item["description"] = description
            self.ledger.append(item)
            self.balance -= amount
            self.spent += amount
            return True
        else: return False

    
    def get_balance(self):
        return self.balance

    
    def transfer(self, amount, destination):
        description_to = f'Transfer to {destination.name}'
        destination_from = f'Transfer from {self.name}'
        if self.check_funds(amount):
            self.withdraw(amount, description_to)
            destination.deposit(amount,destination_from)
            return True
        else: return False

    
    def check_funds(self, amount):
        if (self.balance - amount) < 0: return False
        else: return True


    # We create the table that will appear when we print the category
    def __str__(self):
        text = ''
        filler = int((30 - len(self.name)) / 2)
        text += '*'*filler + self.name + '*'*filler
        for item in self.ledger:
            show_amount = "{:.2f}".format(item["amount"])
            text += f'\n{item["description"][:23]:<23}{show_amount:>7}'
        text += f'\nTotal: {self.balance}'
        return text


def create_spend_chart(categories):
    # First, we create the base string
    text = 'Percentage spent by category'
    # Then we separate category names and amounts
    spent = []
    categories_names = []
    for category in categories:
        spent.append(float(category.spent))
        categories_names.append(category.name)
    # After that, we calculate the proportion of spending by category
    total = sum(spent)
    for i in range(len(spent)):
        spent[i-1] = int(((spent[i-1]/total)*100)//10)*10
    # And finally we construct the graphic, starting with the data
    x = 100
    length = 3*(len(spent)) + 1
    for i in range(11):
        text += f'\n{x:>3}| '
        for item in spent:
            if item >= x: text += 'o  '
            else: text += '   '
        x -= 10
    # We add the lines ox the X axis
    text += '\n    ' + '-'*length
    # And the labels in vertical format
    max_length = max(categories_names,key=len)
    for i in range(len(max_length)):
        text += '\n     '
        for name in categories_names:
            try: text += f'{name[i]}  '
            except IndexError: text += '   '
    # All done!
    return text