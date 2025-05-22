from boxplot import *

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8]
z = []

def test_mediana():
    assert boxplot.mediana(x) == 5
    assert boxplot.mediana(y) == 4.5
    assert boxplot.mediana(z) == 0

# def test_quartis():
#     assert boxplot.quartis(x) == 0
#     assert boxplot.quartis(y) == 0
#     assert boxplot.quartis(z) == 0
