import pytest
import math
from MyCalcy import MyCalcy

c = MyCalcy()

@pytest.fixture
def num_op_num_data():
    #id - pr457, date - 2/27/23
    # data for testing num op num. contains 2 inputs and result with key as operator and result of that as value
    return [{
        "a":"2",
        "b":"2",
        "+":"4",
        "-":"0",
        "/":"1.0",
        "*":"4",
        "x":"4",
    },
    {
        "a":"2.3",
        "b":"4",
        "+":"6.3",
        "-":"-1.7",
        "/":"0.575",
        "*":"9.2",
        "x":"9.2",
    },
    {
        "a":"-1",
        "b":"1",
        "+":"0",
        "-":"-2",
        "/":"-1.0",
        "*":"-1",
        "x":"-1"
    },
    {
        "a":"10",
        "b":"3",
        "+":"13",
        "-":"7",
        "/":"3.333335",
        "*":"30",
        "x":"30"

    }
    ]

@pytest.fixture
def ans_op_num_data():
    #id - pr457, date - 2/27/23
    # data for testing ans op num. contains 2 inputs and result with key as operator and result of that as value
    return [{
        "a":"ans",
        "b":"2",
        "+":"3",
        "-":"-1",
        "/":"0.5",
        "*":"2",
        "x":"2",
    },
    {
        "a":"ans",
        "b":"4",
        "+":"7",
        "-":"-5",
        "/":"0.125",
        "*":"8",
        "x":"8",
    },
    {
        "a":"ans",
        "b":"-1",
        "+":"6",
        "-":"-4",
        "/":"-0.125",
        "*":"-8",
        "x":"-8"
    },
    {
        "a":"ans",
        "b":"3",
        "+":"9",
        "-":"-7",
        "/":"-0.04166664",
        "*":"-24",
        "x":"-24"

    }
    ]

def test_addition_num(num_op_num_data):
    #id - pr457, date - 2/27/23
    #using fixtures to provide the data for testing num+num
    for d in num_op_num_data:
        if "+" in d:
            c.addition(d['a'],d['b']) 
            assert c.ans == (d['+'])
    # c.addition('2', '+', '5')
    # assert c.ans == 7

def test_addition_ans(ans_op_num_data):
    #id - pr457, date - 2/27/23
    #using fixtures to provide the data for testing ans+num
    c.ans = '1'
    for d in ans_op_num_data:
        if "+" in d:
            c.addition("ans",d['b']) 
            assert c.ans == (d['+'])

def test_subtraction_num(num_op_num_data):
    #id - pr457, date - 2/27/23
    #using fixtures to provide the data for testing num-num
    #math.isclose is used for the comparision of possible float values
    for d in num_op_num_data:
        if "-" in d:
            c.substraction(d['a'],d['b']) 
            assert math.isclose(MyCalcy._as_number(c.ans),MyCalcy._as_number(d['-']))

def test_subtraction_ans(ans_op_num_data):
    #id - pr457, date - 2/27/23
    #using fixtures to provide the data for testing ans-num
    #math.isclose is used for the comparision of possible float values
    c.ans = '1'
    for d in ans_op_num_data:
        if "-" in d:
            c.substraction("ans",d['b']) 
            assert math.isclose(MyCalcy._as_number(c.ans),MyCalcy._as_number(d['-']))

def test_multiplication_num(num_op_num_data):
    #using fixtures to provide the data for testing num*num
    #math.isclose is used for the comparision of possible float values
    #id - pr457, date - date - 2/27/23
    for d in num_op_num_data:
        if "*" in d:
            c.multiplication(d['a'],d['b']) 
            assert math.isclose(MyCalcy._as_number(c.ans),MyCalcy._as_number(d['*']))


def test_multiplication_ans(ans_op_num_data):
    #using fixtures to provide the data for testing ans*num
    #math.isclose is used for the comparision of possible float values
    #id - pr457, date - 2/27/23
    c.ans = '1'
    for d in ans_op_num_data:
        if "*" in d:
            c.multiplication("ans",d['b']) 
            assert math.isclose(MyCalcy._as_number(c.ans),MyCalcy._as_number(d['*']))

    
def test_division_num(num_op_num_data):
    #using fixtures to provide the data for testing num/num
    #math.isclose is used for the comparision of possible float values
    #id - pr457, date - 2/27/23
    for d in num_op_num_data:
        if "/" in d:
            c.division(d['a'],d['b']) 
            assert math.isclose(MyCalcy._as_number(c.ans),MyCalcy._as_number(d['/']),abs_tol = 0.5e-1)

def test_division_ans(ans_op_num_data):
    #id - pr457, date - 2/27/23
    #using fixtures to provide the data for testing ans/num
    #math.isclose is used for the comparision of possible float values
    c.ans = '1'
    for d in ans_op_num_data:
        if "/" in d:
            c.division("ans",d['b']) 
            assert math.isclose(MyCalcy._as_number(c.ans),MyCalcy._as_number(d['/']), abs_tol = 0.5e-1)