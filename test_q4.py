from q4 import (
    Stock,
    get_best_margin,
    get_sell_timing_price
)


def test_stock():
    st = Stock()
    assert st.stock == 0 and st.margin == 0

    st.buy(10)
    assert st.stock == 1 and st.margin == -10

    st.buy(30)
    assert st.stock == 2 and st.margin == -40

    st.buy(20)
    assert st.stock == 3 and st.margin == -60

    st.sell(50, 1)
    assert st.stock == 2 and st.margin == -10

    st.sell(5)
    assert st.stock == 0 and st.margin == 0


def test_get_best_margin():
    stocks1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    margin1 = 0
    assert get_best_margin(stocks1) == margin1

    stocks2 = [1, 1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2]
    margin2 = 27
    assert get_best_margin(stocks2) == margin2


def test_get_sell_timing_price():
    test_stock = [1, 2, 3, 4, 5, 4, 3, 2, 3, 2, 1]

    t1, p1 = get_sell_timing_price(test_stock)
    assert t1 == 4 and p1 == 5

    t2, p2 = get_sell_timing_price(test_stock, t1)
    assert t2 == 5 and p2 == 4

    t3, p3 = get_sell_timing_price(test_stock, t2)
    assert t3 == 6 and p3 == 3

    t4, p4 = get_sell_timing_price(test_stock, t3)
    assert t4 == 8 and p4 == 3

    t5, p5 = get_sell_timing_price(test_stock, t4)
    assert t5 == 9 and p5 == 2

    t6, p6 = get_sell_timing_price(test_stock, t5)
    assert t6 == 10 and p6 == 1
