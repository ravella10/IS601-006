import pytest
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException, InvalidPaymentException
#this is an example test showing how to cascade fixtures to build up state
# UCID - pr457, date - 03/20/2023
@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# UCID - pr457, date - 03/20/2023
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

# UCID - pr457, date - 03/20/2023
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

# UCID - pr457, date - 03/20/2023
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

# UCID - pr457, date - 03/20/2023
@pytest.fixture
def third_order(second_order):
    second_order.handle_bun("lettuce wrap")
    for i in range(3):
        second_order.handle_patty("turkey")
    second_order.handle_patty("next")
    for i in range(3):
        second_order.handle_toppings("cheese")
    second_order.handle_toppings("done")
    second_order.handle_pay(10000,"10000")
    second_order.handle_bun("no bun")
    return second_order

# add required test cases below
# UCID - pr457, date - 03/20/2023
def test_first_selection(second_order):
    with pytest.raises(InvalidStageException) as patties_selection:
        second_order.handle_patty("turkey")
    with pytest.raises(InvalidStageException) as toppings_selection:
        second_order.handle_toppings("cheese")
    second_order.handle_bun("no bun")
    assert patties_selection.value and toppings_selection.value

# UCID - pr457, date - 03/20/2023
def test_patties_instock(third_order):
    with pytest.raises(OutOfStockException) as patties_stock:
        for i in range(3):
            third_order.handle_patty("turkey")
    third_order.handle_patty("beef")
    assert patties_stock.value

# UCID - pr457, date - 03/20/2023
def test_toppings_instock(third_order):
    with pytest.raises(OutOfStockException) as toppings_stock:
        third_order.handle_patty("next")
        for i in range(3):
            third_order.handle_toppings("cheese")
    third_order.handle_toppings("tomato")
    assert toppings_stock.value

# UCID - pr457, date - 03/20/2023
def test_patties_three(machine):
    machine.handle_bun("no bun")
    patties_list = ['beef','veggie','turkey']
    for patty in patties_list:
        machine.handle_patty(patty)
    with pytest.raises(ExceededRemainingChoicesException) as patties_choices:
        machine.handle_patty("beef")
        machine.handle_patty('next')
        machine.handle_toppings('done')
        machine.handle_pay(machine.calculate_cost(),str(machine.calculate_cost()))

# UCID - pr457, date - 03/20/2023
def test_toppings_three(machine):
    toppings_list = [('Lettuce','Tomato','Pickles'),('Cheese','Ketchup','Mayo'),('Mustard','BBQ','Lettuce')]
    for topping_combination in toppings_list:
        machine.handle_bun("no bun")
        machine.handle_patty('beef')
        machine.handle_patty('next')
        for toppings in topping_combination:
            machine.handle_toppings(toppings)
        machine.handle_toppings('done')
        machine.handle_pay(machine.calculate_cost(),str(machine.calculate_cost()))
    with pytest.raises(ExceededRemainingChoicesException) as patties_choices:
        machine.handle_bun("no bun")
        machine.handle_patty("next")
        for i in range(4):
            machine.handle_toppings("lettuce")

# UCID - pr457, date - 03/20/2023
def test_cost_calculation(machine):
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")      
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    assert str(machine.calculate_cost()) == "2.75"
    machine.handle_pay(machine.calculate_cost(),str(machine.calculate_cost()))
    machine.handle_bun("no bun")
    machine.handle_patty("turkey")
    machine.handle_patty("beef")
    machine.handle_patty("next")      
    machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    assert str(machine.calculate_cost()) == "2.25"
    machine.handle_pay(machine.calculate_cost(),str(machine.calculate_cost()))
    machine.handle_bun("white burger bun")
    machine.handle_patty("turkey")
    machine.handle_patty("beef")
    machine.handle_patty("next")      
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    assert str(machine.calculate_cost()) == "3.25"
    machine.handle_pay(machine.calculate_cost(),str(machine.calculate_cost()))
    # permute_order.handle_pay(2.75,"2.5")

# UCID - pr457, date - 03/20/2023
def test_sales_calculation(permute_order):
    assert str(permute_order.total_sales) == "13.5"

# UCID - pr457, date - 03/20/2023
def test_burgers_count(permute_order):
    permute_order.handle_bun("lettuce wrap")
    permute_order.handle_patty("beef")
    permute_order.handle_patty("next")      
    permute_order.handle_toppings("tomato")
    permute_order.handle_toppings("done")
    permute_order.handle_pay(2.75,"2.75")
    assert permute_order.total_burgers == 4