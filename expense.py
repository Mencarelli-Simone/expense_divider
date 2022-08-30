##%

def dictionalizer(ll):
    price = input(" insert price in dollars or 'quit' to stop adding stuff or del to correct last entry")
    if price == 'quit' \
            :
        return -1
    if price == 'del':
        del ll[-1]
        return 1
    buyers = str(input("insert buyer initials eg SACL, order doesn't matter"))
    if buyers == '' or price == '':
        return 1
    dict = {'price': float(eval(price)), 'buyers': buyers}
    ll.append(dict)
    return 1


def filler(lista):
    a = 1
    while a == 1:
        a = dictionalizer(lista)


def total(lista):
    total = 0
    for item in lista:
        total += item['price']
    return total


def partials(lista):
    buyers = []
    partial = {}
    totals = 0
    for item in lista:
        bu = list(item['buyers'].lower())
        # every char is a buyer
        for ii in range(len(bu)):
            if not (bu[ii] in buyers):
                buyers.append(bu[ii])  # add new buyer to the list
                partial[str(bu[ii])] = 0  # create a new entry in the dictionary as well
            partial[str(bu[ii])] += item['price'] / len(bu)
            totals += item['price'] / len(bu)
    return partial, totals


##%
lista = []
filler(lista)
total()
partials(lista)
## to do uneven quutas just input more characters for the same buyer
## e.g llla = 3/4 to l, and 1/4 to a
