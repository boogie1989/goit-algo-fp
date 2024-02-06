class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def merge_sorted_lists(list1, list2):
        merged_list = LinkedList()  # Створюємо новий зв'язаний список для злиття результатів

        # Вказівники для ітерації через два вхідних списки
        current1 = list1.head
        current2 = list2.head

        # Проходимо обидва списки і порівнюємо їх елементи
        while current1 is not None and current2 is not None:
            if current1.data <= current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next

        # Якщо один зі списків ще має елементи, додаємо їх до об'єднаного списку
        while current1 is not None:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next

        while current2 is not None:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

        return merged_list

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None  # Ініціалізуємо змінну для збереження попереднього вузла
        current = self.head  # Починаємо з головного вузла списку

        while current:
            next_node = current.next  # Зберігаємо наступний вузол тимчасово
            current.next = prev  # Змінюємо посилання next на попередній вузол
            prev = current  # Переміщаємо попередній вузол на поточний
            current = next_node  # Переходимо до наступного вузла в початковому списку

        self.head = prev

    def sort(self):
        if not self.head or not self.head.next:
            return  # Список порожній або містить лише один елемент; він вже відсортований

        sorted_head = None  # Ініціалізуємо новий зв'язаний список для відсортованих елементів

        current = self.head  # Починаємо з першого вузла в початковому списку

        while current:
            next_node = current.next  # Зберігаємо наступний вузол тимчасово

            if not sorted_head or current.data <= sorted_head.data:
                # Якщо відсортований список порожній або дані поточного вузла менше
                # першого елемента в відсортованому списку, додаємо в початок.
                current.next = sorted_head
                sorted_head = current
            else:
                # В іншому випадку знаходимо правильне місце для вставки поточного вузла.
                prev_sorted = sorted_head
                while prev_sorted.next and prev_sorted.next.data < current.data:
                    prev_sorted = prev_sorted.next

                # Вставляємо поточний вузол між prev_sorted і prev_sorted.next
                current.next = prev_sorted.next
                prev_sorted.next = current

            current = next_node  # Переходимо до наступного вузла в початковому списку

        # Оновлюємо голову зв'язаного списку на відсортований список
        self.head = sorted_head
