class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.cursor = 0
        self.inner_cursor = -1
        return self

    def __next__(self):
        self.inner_cursor += 1
        if self.inner_cursor >= len(self.nested_list[self.cursor]):
            self.cursor += 1
            self.inner_cursor = 0
        if self.cursor >= len(self.nested_list):
            raise StopIteration
        return self.nested_list[self.cursor][self.inner_cursor]


def flat_generator(nested_list):
    outer_index = 0
    inner_index = 0
    while True:
        yield nested_list[outer_index][inner_index]
        inner_index += 1
        if inner_index >= len(nested_list[outer_index]):
            outer_index += 1
            inner_index = 0
        if outer_index >= len(nested_list):
            break

def super_flat_generator(very_nested_list):
    for element in very_nested_list:
        if isinstance(element, list):
            yield from super_flat_generator(element)
        else:
            yield element

if __name__ == '__main__':

    '''Задание 1'''

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    '''Задание 2'''

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None]
    ]

    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)

    '''Задание 4'''

    super_nested_list = [
        'a', [2, False],
        [[[True], None], 3,
        ['b',['c', ['i']]]]
    ]
    for element in super_flat_generator(super_nested_list):
        print(element)

    flat_list = [item for item in super_flat_generator(super_nested_list)]
    print(flat_list)