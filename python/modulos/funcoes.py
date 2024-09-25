def somar():
    print("Essa função vai somar dois valores")

def multi():
    print("Essa função vai multiplicar dois valores")

def find_index(to_fnid, item):
    for i, valor in enumerate(to_fnid):
        if valor == item:
            return i
    return valor