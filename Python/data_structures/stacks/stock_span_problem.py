"""
The stock span problem is a financial problem where we have a series of n daily
price quotes for a stock and we need to calculate span of stock's price for all n days.

The span Si of the stock's price on a given day i is defined as the maximum
number of consecutive days just before the given day, for which the price of the stock
on the current day is less than or equal to its price on the given day.
"""
import doctest
import timeit
import functools

def calculate_span(price: list):
    """
    >>> calculate_span([90,80,70,60])
    [1, 1, 1, 1]
    >>> calculate_span([60,70,80,90])
    [1, 2, 3, 4]
    >>> calculate_span([50,50,50])
    [1, 2, 3]
    >>> calculate_span([10, 60, 20, 50])
    [1, 2, 1, 2]
    """
    # Create a stack and push index of fist element to it
    stack = []
    stack.append(0)

    S = [0] * len(price)
    # Span value of first element is always 1
    S[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, len(price)):

        # Pop elements from stack while stack is not
        # empty and top of stack is smaller than price[i]
        while stack and price[stack[-1]] <= price[i]:
            stack.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i]  is
        # greater than elements after top of stack
        S[i] = i + 1 if not stack else (i - stack[-1])

        # Push this element to stack
        stack.append(i)
    return S


def calculate_span_nostack(price: list):
    """
    This is a bad solution. O(n^2)
    >>> calculate_span_nostack([90,80,70,60])
    [1, 1, 1, 1]
    >>> calculate_span_nostack([60,70,80,90])
    [1, 2, 3, 4]
    >>> calculate_span_nostack([50,50,50])
    [1, 2, 3]
    >>> calculate_span_nostack([10, 60, 20, 50])
    [1, 2, 1, 2]
    """
    result = [1] * len(price)
    for i_outer in range(len(price) - 1, -1, -1):
        for i_inner in range(i_outer - 1, -1, -1):
            if price[i_inner] > price[i_outer]:
                break
            else:
                result[i_outer] += 1

    return result


if __name__ == '__main__':
    doctest.testmod(verbose=False)
    price = [10, 4, 5, 90, 120, 80]
    calculate_span(price)


    def gen_descending(exponent: int) -> list:
        return list(range(10**exponent, -1, -1))
    def gen_ascending(exponent: int) -> list:
        return list(range(0,10**exponent))
    for gen_input in (gen_descending, gen_ascending):
        for exponent in range(1, 5):
            testlist = gen_input(exponent)
            test_calculate_span = functools.partial(calculate_span, testlist)
            test_calculate_span_nostack = functools.partial(calculate_span_nostack, testlist)

            time_stack = timeit.timeit(test_calculate_span, number=3)
            time_nostack = timeit.timeit(test_calculate_span_nostack, number=3)

            print(f"{gen_input.__name__}, {exponent=}: {time_stack=}, {time_nostack=}")

    # gen_descending, exponent = 1: time_stack = 1.2099999999959365e-05, time_nostack = 1.3100000000099143e-05
    # gen_descending, exponent = 2: time_stack = 7.679999999998799e-05, time_nostack = 9.179999999986421e-05
    # gen_descending, exponent = 3: time_stack = 0.0009198000000001372, time_nostack = 0.0010684000000000804
    # gen_descending, exponent = 4: time_stack = 0.008911299999999844, time_nostack = 0.01351239999999998
    # gen_ascending, exponent = 1: time_stack = 2.2200000000083264e-05, time_nostack = 2.4400000000035504e-05
    # gen_ascending, exponent = 2: time_stack = 0.00019910000000011863, time_nostack = 0.0016370000000001106
    # gen_ascending, exponent = 3: time_stack = 0.0015912000000000148, time_nostack = 0.18107410000000002
    # gen_ascending, exponent = 4: time_stack = 0.018721699999999952, time_nostack = 18.254447

    # Notice that the ascending input is always slower. This is also where the stack solution
    # shines. Intuition 1:
    # [1, 2, 3, 2, 1, 2, 3, 2, 1] (imagine a sine wave)
    # when going down the slope, we push to the stack
    # when going up the slope, we pop the stack, because the popped values should never
    # be checked again (this is why the stack method is faster).