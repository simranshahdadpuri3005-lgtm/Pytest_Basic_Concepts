import pytest
#fixture will provide ability to any method to trigger before each and every function
#scope of fixture can be function, class, module(module is py file) and session (total execution lifecycle)
#@pytest.fixture(scope="function", autouse=True) if auto use is true, we need call the fixture as the parameter, it will be executed for all funcs by default

@pytest.fixture(scope="session", autouse=True)
def firstfixture():
   print("enter code for login before yield in session")
   yield
   print("enter code for logout after yield in session")

@pytest.fixture(scope="function", autouse=True)
def secondfixture():
    print("enter code for login before yield in function")
    yield
    print("enter code for logout after yield in function")

@pytest.fixture(scope="module", autouse=True)
def thirdfixture():
   print("enter code for login before yield in module")
   yield
   print("enter code for logout after yield in module")
