from boxplot import *

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8]
z = [1,5]

def test_mediana():
    assert boxplot.mediana(x) == 5
    assert boxplot.mediana(y) == 4.5
    assert boxplot.mediana(z) == 3

def test_quartis():
    assert boxplot.quartis(x, raw=True) == "min: 1.00, q1: 2.50, q2: 5.00, q3: 7.50, max: 9.00"
    assert boxplot.quartis(y, raw=True) == "min: 1.00, q1: 2.50, q2: 4.50, q3: 6.50, max: 8.00"
    assert boxplot.quartis(z, raw=True) == "min: 1.00, q1: 1.00, q2: 3.00, q3: 5.00, max: 5.00"
