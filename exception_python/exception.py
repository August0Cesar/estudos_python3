class TestException(Exception):
    def __init__(self, message='', param1=None, param2=None, *args, **kwargs):
        self.param1 = param1
        self.param2 = param2
        msg = 'Test exception ' \
                        f'parametro 1 {self.param1} parametro 2 {self.param2}'
        super(TestException, self).__init__(message or msg, *args, **kwargs)


def test_esception():
    par1 = 2
    par2 = 'Augusto'
    raise TestException("ola", par1, par2, "test") 


if __name__ == '__main__':
    test_esception()