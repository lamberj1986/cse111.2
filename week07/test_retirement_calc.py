"""Verify that the future value, current shortfall, and projected spend functions work correctly."""

from retirement_calc import get_future_value, calculate_current_shortfall, \
    calculate_projected_spend, calculate_monthly_deposit

import pytest
from pytest import approx

def test_future_value():
    """Verify that the get_future_value function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the get_future_value function and verify that it returns a float.
    future = get_future_value(25, 70, 35000, 0.09)
    assert isinstance(future, float), "get_future_value function must return a float"

    # Call the get_future_value function ten times and use an assert
    # statement to verify that the string returned by the
    # get_future_value function is correct each time.

    assert get_future_value(25, 70, 35000, 0.09) == approx(1691455.014 , abs=0.001)
    assert get_future_value(25, 70, 35000, 0.06) == approx(481761.379 , abs=0.001)
    assert get_future_value(25, 70, 35000) == approx(481761.379 , abs=0.001)
    assert get_future_value(25, 70, 55000, 0.09) == approx(2658000.736 , abs=0.001)
    assert get_future_value(35, 70, 75000, 0.08) == approx(1108900.822 , abs=0.001)

def test_current_shortfall():
    """Verify that the calculate_current_shortfall function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the calculate_current_shortfall function and verify that it returns a float.
    short = calculate_current_shortfall(25, 72, 35000, 2500)
    assert isinstance(short, float), "calculate_current_shortfall function must return a float"

    # Call the calculate_current_shortfall function ten times and use an assert
    # statement to verify that the string returned by the
    # calculate_current_shortfall function is correct each time.

    assert calculate_current_shortfall(25, 72, 35000, 2500) == approx(208692.915 , abs=0.001)
    assert calculate_current_shortfall(45, 72, 35000, 2500) == approx(581217.892 , abs=0.001)
    assert calculate_current_shortfall(45, 72, 250000, 2500) == approx(-455586.485 , abs=0.001)
    assert calculate_current_shortfall(35, 72, 35000, 3500) == approx(747736.951 , abs=0.001)
    assert calculate_current_shortfall(35, 72, 75000, 2500) == approx(102293.466 , abs=0.001)
    assert calculate_current_shortfall(35, 72, 75000, 1500) == approx(-197706.534 , abs=0.001)
    assert calculate_current_shortfall(35, 70, 75000, 2500) == approx(173543.491 , abs=0.001)


def test_projected_spend():
    """Verify that the calculate_projected_spend function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the calculate_projected_spend function and verify that it returns a float.
    spend = calculate_projected_spend(1200000)
    assert isinstance(spend, float), "calculate_projected_spend function must return a float"

    # Call the calculate_projected_spend function ten times and use an assert
    # statement to verify that the string returned by the
    # calculate_projected_spend function is correct each time.
    assert calculate_projected_spend(1200000) == approx(4000 , abs=0.001)
    assert calculate_projected_spend(750000) == approx(2500 , abs=0.001)
    assert calculate_projected_spend(576456.509) == approx(1921.522 , abs=0.001)
    assert calculate_projected_spend(297881.980) == approx(992.940 , abs=0.001)
    assert calculate_projected_spend(3500000) == approx(11666.667 , abs=0.001)

def test_monthly_deposit():
    """Verify that the calculate_projected_spend function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the calculate_monthly_deposit function and verify that it returns a float.
    deposit = calculate_monthly_deposit(35, 70, 750000, 0.08)
    assert isinstance(deposit, float), "calculate_monthly_deposit function must return a float"

    # Call the calculate_monthly_deposit function ten times and use an assert
    # statement to verify that the string returned by the
    # calculate_monthly_deposit function is correct each time.
    assert calculate_monthly_deposit(35, 70, 750000, 0.08) == approx(308.935 , abs=0.001)
    assert calculate_monthly_deposit(35, 70, 1750000, 0.08) == approx(720.848 , abs=0.001)
    assert calculate_monthly_deposit(35, 70, 750000) == approx(463.929 , abs=0.001)
    assert calculate_monthly_deposit(25, 70, 750000, 0.06) == approx(254.990 , abs=0.001)
    assert calculate_monthly_deposit(25, 75, 750000, 0.06) == approx(189.043 , abs=0.001)
    assert calculate_monthly_deposit(35, 70, 350000, 0.09) == approx(114.670 , abs=0.001)
    assert calculate_monthly_deposit(35, 70, 550000, 0.06) == approx(340.214 , abs=0.001)
    assert calculate_monthly_deposit(35, 70, 1250000, 0.03) == approx(1097.727 , abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
