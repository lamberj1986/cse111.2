from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():

    assert extract_city('525 Center St, Rexburg, ID 83460') == "Rexburg"
    assert extract_city('123 Main St, Lowell, MI 49331') == "Lowell"
    assert extract_city('1720 E Main St, Dallas, TX 73114') == "Dallas"
    assert extract_city('5445 S Tibet St, Aurora, CO 80015') == "Aurora"

def test_extract_state():

    assert extract_state('525 Center St, Rexburg, ID 83460') == "ID"
    assert extract_state('123 Main St, Lowell, MI 49331') == "MI"
    assert extract_state('1720 E Main St, Dallas, TX 73114') == "TX"
    assert extract_state('5445 S Tibet St, Aurora, CO 80015') == "CO"

def test_extract_zipcode():

    assert extract_zipcode('525 Center St, Rexburg, ID 83460') == "83460"
    assert extract_zipcode('123 Main St, Lowell, MI 49331') == "49331"
    assert extract_zipcode('1720 E Main St, Dallas, TX 73114') == "73114"
    assert extract_zipcode('5445 S Tibet St, Aurora, CO 80015') == "80015"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])