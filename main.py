"""
Домашнее задание для лекции "Задачки на собеседованиях для продвинутых,
с тонкостями языка"

Решение
    1. Сделано
    2. Cложность алгоритма: O(n) - линейная функция от каждого элемента списка,
    потребление памяти: O(1) - вставка слева в связанный список, новых переменных внутри цикла не создается
    3. Для массива: сложность O(n), память O(1) - ничего не изменилось, так как нам все еще нужно перебрать
    все элементы массива; работа с памятью осуществляется по аналогии со списком

Примечание
    Проверить работоспособность решения можно при помощи тестов,
    которые можно запустить следующей командой:

    python3 -m unittest main.py
"""

import unittest

from typing import Iterable


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None  # type: LinkedListNode


class LinkedList:

    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def reverse(self):
        last = None
        while self.head:
            self.head.next, last, self.head = last, self.head, self.head.next
        self.head = last


class LinkedListTestCase(unittest.TestCase):

    def test_reverse(self):
        cases = dict(
            empty = dict(
                items = [],
                expected_items = [],
            ),
            single = dict(
                items = [1],
                expected_items = [1],
            ),
            double = dict(
                items = [1, 2],
                expected_items = [2, 1],
            ),
            triple = dict(
                items = [1, 2, 3],
                expected_items = [3, 2, 1],
            ),
        )
        for case, data in cases.items():
            with self.subTest(case = case):
                linked_list = LinkedList(data['items'])
                linked_list.reverse()
                self.assertListEqual(
                    data['expected_items'],
                    list(linked_list),
                )
