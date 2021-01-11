class Orcamento(object):
    def __init__(self):
        self._items = []
    
    @property
    def total_itens(self):
        return len(self._items)
    
    
    def obter_itens(self):
        return tuple(self._items)
    
    @property
    def value(self):
        total = 0
        for item in self._items:
            total += item.value
        return total
    

    def add_item(self, item):
        self._items.append(item)


class Item(object):
    def __init__(self, name, value):
        self._name = name
        self._value = value


    @property
    def name(self):
        return self._name


    @property
    def value(self):
        return self._value
    

