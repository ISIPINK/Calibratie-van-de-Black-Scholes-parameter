from scipy.stats import norm

'''
chatgpt prompt :
    write a program that calculates implied volatility

answer:
    Here is a simple program that calculates the implied volatility of
    an option using the Newton-Raphson method:
'''


# Calculate the cumulative distribution function (CDF) of a standard normal random variable
def cdf(x):
    return norm.cdf(x)

# Calculate the probability density function (PDF) of a standard normal random variable
def pdf(x):
    return norm.pdf(x)

def implied_volatility(
        option_price, underlying_price, strike_price, time_to_expiration, interest_rate, call_or_put):

    MAX_ITERATIONS = 100
    PRECISION = 0.00001

    # Initialize the starting point for the Newton-Raphson method
    implied_vol = 0.1

    # Implement the Newton-Raphson method to find the implied volatility
    for i in range(0, MAX_ITERATIONS):
        option_value = black_scholes(
                underlying_price, strike_price, time_to_expiration, 
                interest_rate, implied_vol, call_or_put)

        vega = black_scholes_vega(
                underlying_price, strike_price, time_to_expiration, interest_rate, implied_vol)

        diff = option_value - option_price

        if (abs(diff) < PRECISION):
            break

        implied_vol = implied_vol - diff/vega

    return implied_vol


def black_scholes(underlying_price, strike_price, time_to_expiration, interest_rate, implied_vol, call_or_put):
    d1 = (log(underlying_price / strike_price) + (interest_rate + implied_vol *
          implied_vol / 2.0) * time_to_expiration) / (implied_vol * sqrt(time_to_expiration))
    d2 = d1 - implied_vol * sqrt(time_to_expiration)

    if call_or_put == "call":
        option_value = underlying_price * \
            cdf(d1) - strike_price * \
            exp(-interest_rate * time_to_expiration) * cdf(d2)
    else:  # call_or_put == "put"
        option_value = strike_price * \
            exp(-interest_rate * time_to_expiration) * \
            cdf(-d2) - underlying_price * cdf(-d1)

    return option_value


# Calculate the vega of a call or put option using the Black-Scholes model
def black_scholes_vega(underlying_price, strike_price, time_to_expiration, interest_rate, implied_vol):
    d1 = (log(underlying_price / strike_price) + (interest_rate + implied_vol *
          implied_vol / 2.0) * time_to_expiration) / (implied_vol * sqrt(time_to_expiration))

    vega = underlying_price * sqrt(time_to_expiration) * pdf(d1)
    return vega
