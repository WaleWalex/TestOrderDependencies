import pytest


@pytest.mark.dependency(name="a")
# @pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert True


@pytest.mark.dependency(name="e",
                        depends=["TestOrderDependencies/test_mod_01.py::a",
                                 "TestOrderDependencies/test_mod_01.py::c"],
                        scope='session'
                        )
def test_e():
    pass


@pytest.mark.dependency(name="f",
                        depends=["TestOrderDependencies/test_mod_01.py::b",
                                 "TestOrderDependencies/test_mod_02.py::e"],
                        scope='session'
                        )
def test_f():
    pass


@pytest.mark.dependency(name="g",
                        depends=["TestOrderDependencies/test_mod_01.py::TestClass::b"],
                        scope='session'
                        )
def test_g():
    pass
