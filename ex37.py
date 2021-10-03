def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_percent = spread / 100
    exchange_with_spread = exchange_rate + spread_percent
    percent_change = 1 / exchange_with_spread
    converted_currency = budget * percent_change
    remainder = converted_currency // denomination
    return int(remainder * denomination)