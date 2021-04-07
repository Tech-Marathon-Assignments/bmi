from main import main

# Test Case 1:
# Input: 50 160
# Output: "Normal"
def test_main_1(capfd):
    main(50, 160)
    out, err = capfd.readouterr()
    assert out == "Normal\n"

# Test Case 2:
# Input: 80 165
# Output: "Obese"
def test_main_2(capfd):
    main(80, 165)
    out, err = capfd.readouterr()
    assert out == "Obese\n"

# Test Case 3:
Input: 40 181
Output: "Normal"
def test_main_3capfd):
    main(40, 181)
    out, err = capfd.readouterr()
    assert out == "Thin\n"
