import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException, InvalidPaymentException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("White Burger Bun")
    for i in range(3):
        machine.handle_patty("turkey")
    machine.handle_patty("next")
    for i in range(3):
        machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    machine.handle_pay(4.75,"4.75")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("Wheat Burger Bun")
    for i in range(2):
        first_order.handle_patty("turkey")
    first_order.handle_patty("beef")
    first_order.handle_patty("next")
    first_order.handle_toppings("BBQ")
    for i in range(2):
        first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    first_order.handle_pay(5,"5")
    return first_order

@pytest.fixture
def permute_order(second_order):
    second_order.handle_bun("no bun")
    second_order.handle_patty("beef")
    second_order.handle_patty("turkey")
    second_order.handle_patty("veggie")
    second_order.handle_patty("next")
    second_order.handle_toppings("Ketchup")
    second_order.handle_toppings("Tomato")
    second_order.handle_toppings("Mayo")
    second_order.handle_toppings("done")
    second_order.handle_pay(3.75,"3.75")
    return second_order

@pytest.fixture
def third_order(second_order):
    second_order.handle_bun("lettuce wrap")
    second_order.handle_patty("turkey")
    second_order.handle_patty("turkey")
    second_order.handle_patty("turkey")
    second_order.handle_patty("next")
    second_order.handle_toppings("cheese")
    second_order.handle_toppings("cheese")
    second_order.handle_toppings("cheese")
    second_order.handle_toppings("done")
    second_order.handle_pay(10000,"10000")
    second_order.handle_bun("no bun")
    return second_order
    

# sample test case, can delete if not using
# def test_production_line(second_order):
#     for j in second_order.buns:
#         print(second_order.inprogress_burger)
#         if j.name.lower() == second_order.inprogress_burger[0].name.lower():
#             assert True
#             return

#     assert False

# add required test cases below
def test_first_selection(second_order):
    with pytest.raises(InvalidStageException) as patties_selection:
        second_order.handle_patty("turkey")
    with pytest.raises(InvalidStageException) as toppings_selection:
        second_order.handle_toppings("cheese")
    second_order.handle_bun("no bun")
    assert patties_selection.value and toppings_selection.value

# def test_toppings_instock(second_order):
#     second_order.handle_bun("no bun")

def test_patties_instock(third_order):
    
    with pytest.raises(OutOfStockException) as patties_stock:
        for i in range(3):
            third_order.handle_patty("turkey")
    third_order.handle_patty("beef")
    assert patties_stock.value

def test_toppings_instock(third_order):
    with pytest.raises(OutOfStockException) as toppings_stock:
        third_order.handle_patty("next")
        for i in range(3):
            third_order.handle_toppings("cheese")
    third_order.handle_toppings("tomato")
    assert toppings_stock.value

def test_patties_three(machine):
    machine.handle_bun("no bun")
    patties_list = ['beef','veggie','turkey']
    for patty in patties_list:
        machine.handle_patty(patty)

def test_toppings_three(machine):
    with pytest.raises(ExceededRemainingChoicesException) as patties_choices:
        machine.handle_bun("no bun")
        machine.handle_patty("next")
        for i in range(4):
            machine.handle_toppings("lettuce")

def test_cost_calculation(permute_order):
    permute_order.handle_bun("lettuce wrap")
    permute_order.handle_patty("beef")
    permute_order.handle_patty("next")      
    permute_order.handle_toppings("tomato")
    permute_order.handle_toppings("done")
    with pytest.raises(InvalidPaymentException) as invalid_payment:
        permute_order.handle_pay(2.75,"2.5")
    assert invalid_payment.value

def test_sales_calculation(permute_order):
    assert str(permute_order.total_sales) == "13.5"

def test_burgers_count(permute_order):
    permute_order.handle_bun("lettuce wrap")
    permute_order.handle_patty("beef")
    permute_order.handle_patty("next")      
    permute_order.handle_toppings("tomato")
    permute_order.handle_toppings("done")
    permute_order.handle_pay(2.75,"2.75")
    assert permute_order.total_burgers == 4