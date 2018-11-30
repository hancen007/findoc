
def test(number):
    def test_in(number2):
        print(number +number2)
    return test_in

ret = test(10)
print(ret(1))
