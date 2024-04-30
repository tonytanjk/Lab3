import Lab2.bmi as bmi

    def test_bmi_normal_weight():
    result = bmi.bmi_range(20)
    assert (result == "0")

def test_bmi_over_weight():
    result = bmi.bmi_range(26)
    assert (result == 1)

def test_bmi_under_weight():
    result = bmi.bmi_range(17)
    assert (result == -1)
