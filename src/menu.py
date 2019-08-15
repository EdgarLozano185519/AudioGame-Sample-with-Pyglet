class Menu:
    def __init__(self):
        self.items = []
        self.click_exists = 0
        self.current = 0

    def add_item(self, mystring):
        self.items.append(str(mystring))

    def add_click(self, soundstring):
        self.click = soundstring
        self.click_exists += 1
        return self.click

    def get_click_exists(self):
        return self.click_exists

    def get_next(self):
        temp = self.current + 1
        if temp < len(self.items):
            self.current = temp
        return self.current

    def get_previous(self):
        temp = self.current - 1
        if temp >= 0:
            self.current = temp
        return self.current

    def current_as_string(self):
        return self.items[self.current]

    def get_current(self):
        return self.current
