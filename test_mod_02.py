import pytest


@pytest.mark.dependency(name="a")
# @pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert True


@pytest.mark.dependency(name="e",
                        depends=["a", "c"],
                        scope='session'
                        )
def test_e():
    pass


@pytest.mark.dependency(name="f",
                        depends=["b", "e"],
                        scope='session'
                        )
def test_f():
    pass


@pytest.mark.dependency(name="g",
                        depends=["b"],
                        scope='session'
                        )
def test_g():
    pass
