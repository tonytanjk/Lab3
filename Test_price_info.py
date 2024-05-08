import price_info as pf

#test_price_info.py

quantity_list= {'apple': 7, 'orange':2, 'watermelon': 3, 'pineapple': 5, 'pear' : 4, 'papaya': 13, 'pomegranate': 2}

def test_total_CS(): #Test Case for total_cost_shopping
    ex_test_result = 96.05000000000001
    result = pf.total_cost_shopping(quantity_list)

    assert (result == ex_test_result)

def test_cost_OF():
    
    result = pf.cost_of_fruits("orange", 5)
    ex_test_result = 7

    assert (result == ex_test_result)