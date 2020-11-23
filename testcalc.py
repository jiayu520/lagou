from Calc.calc import Calc


class Testadd():
    def setup(self):
        self.ca = Calc()

    #有效等价类
    def test_add1(self):
        assert self.ca.add(1,2) == 3

    #无效等价类
    def test_add2(self):
        assert self.ca.add(0.5,'jia') == 1

class Testadd3():

    #有效等价类
    def test_add(self):
        assert Calc.add3(1,2) == 3

    #无效等价类
    def test_add2(self):
        assert Calc.add3(0.5,'jia') == 2.5

class TestAddStatic():
    # 有效等价类
    def test_add(self):
        assert Calc.add_static(1, 2) == 3

    # 无效等价类
    def test_add2(self):
        assert Calc.add_static(0.5, 'jia') == 2.5

class Testadd2():
    def setup(self):
        self.ca = Calc()

    # 有效等价类
    def test_add1(self):
        assert self.ca.add2((0,1)) == 1

    # 无效等价类
    def test_add2(self):
        assert self.ca.add2(0.5, 'jia') == 1

class Testdiv():
    def setup(self):
        self.ca = Calc()

    #有效等价类
    def test_div1(self):
        assert self.ca.div(1,2) == 0.5

    #无效等价类
    def test_div1(self):
        try:
            assert self.ca.div(1,0) == 0
        except ZeroDivisionError:
            print('除数不能为0')



