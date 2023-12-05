import pytest


@pytest.mark.dependency(name="a")
def test_a():
    pass


@pytest.mark.dependency(name="b")
# @pytest.mark.xfail(reason="deliberate fail")
def test_b():
    assert True


@pytest.mark.dependency(name="c", depends=["a"])
def test_c():
    pass


class TestClass(object):

    @pytest.mark.dependency(name="b", depends=["c"])
    def test_b(self):
        pass
