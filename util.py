from pathlib import Path
from json import dumps, loads
from typing import Any

# * ################## LÓGICA DE LEITURA E ESCRITA ##################


class JSONDatabase:
    def __init__(self, name):
        self.name = name
        self.path = Path(name)

        if not self.path.exists() or self.path.read_text() == "":
            self.path.write_text("{}")

    def truncate(self):
        self.path.unlink()
        self.path.write_text("{}")

    def read(self) -> dict[str, Any]:
        return loads(self.path.read_text())

    def write(self, data):
        self.path.write_text(dumps(data, indent=4, ensure_ascii=False))


# * ################## LÓGICA DO MENU ##################
class ANOTHER_PAGE:
    ...


class EXIT_MENU:
    ...


class MenuManager:
    def __init__(self):
        self.menus = {}
        self.title = None
        self.list = []

        self.print_title = lambda title: f"{title}\n"
        self.print_option = lambda index, option: f"{index} {option}\n"
        self.print_input = lambda: ">>> "
        self.print_sequence = lambda s: " > ".join(s) + "\n"
        self.print_back = lambda index: f"{index}. Back"

    def add(self, menus):
        self.menus.update(menus)
        self.title = list(menus.keys())[0]

    def to(self, title):
        def foo():
            if title in self.menus:
                self.title = title
            return ANOTHER_PAGE

        return foo

    def format_option(self, s):
        self.print_option = s

    def format_title(self, s):
        self.print_title = s

    def format_input(self, s):
        self.print_input = s

    def format_sequence(self, s):
        self.print_sequence = s

    def format_back(self, s):
        self.print_back = s

    def close(self):
        return EXIT_MENU

    def show(self):
        while True:
            print("\n")
            title = self.title
            menu = self.menus[title]
            self.list.append(title)

            is_main_menu = len(self.list) == 1

            print(self.print_title(title))
            print(self.print_sequence(self.list))

            for index, option in enumerate(menu.keys(), 1):
                print(self.print_option(index, option))

            if not is_main_menu:
                print(self.print_back(len(menu) + 1))

            try:
                op = int(input(self.print_input()))
            except ValueError:
                self.list.pop()
                print("Write a number!")
                continue

            fns = list(menu.values())

            try:
                r = fns[op - 1]()

                if r == EXIT_MENU:
                    break

                if r != ANOTHER_PAGE:
                    self.list.pop()
            except IndexError:
                if not is_main_menu and op - 1 == len(menu):
                    self.list.pop()
                    self.title = self.list.pop()
                else:
                    print("Select a valid option!")


# * ################## LÓGICA DA LISTA ##################


class StaticList:
    def __init__(self, max_size, content=[]):
        self.max_size = max_size
        self.l = content[:]

    def __str__(self):
        return f'[{", ".join(map(str, self.l))}]'

    def add(self, i):
        as_list = i if isinstance(i, list) else [i]
        extra_items_size = (len(as_list) + len(self)) - self.max_size

        if extra_items_size > 0:
            return StaticList(len(self) + extra_items_size, list(iter(self)) + as_list)

        self.l += as_list
        return self

    def remove(self, i):
        self.l.remove(i)

    def __iter__(self):
        return iter(self.l)

    def __len__(self):
        return len(self.l)

    def find(self, fn):
        for i in self:
            if fn(i):
                return i

    def has(self, v):
        for i in self:
            if v == i:
                return True

    def get_index(self, i):
        return self.l[i]

    def get(self, s):
        return self.find(lambda i: i == s)
