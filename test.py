class A():
    def a(self):
        print('a')

class B():
    @property
    def b(self):
        print('b')


A().a()
B().b