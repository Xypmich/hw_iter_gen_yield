class FlatIterator:

    def __init__(self, raw_list):
        self.raw_list = raw_list

    def __iter__(self):
        self.count_list = 0
        self.count_list_items = 0
        return self

    def __next__(self):
        if self.count_list_items == len(self.raw_list[self.count_list]):
            self.count_list += 1
            self.count_list_items = 0
            if self.count_list == len(self.raw_list):
                raise StopIteration
        list_item = self.raw_list[self.count_list][self.count_list_items]
        self.count_list_items += 1
        return list_item


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print('-' * 7)
    print(flat_list)
