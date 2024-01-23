from water_flow import pressure_loss_from_fittings
from pytest import approx

test1 = pressure_loss_from_fittings(0.00,3)
test2 = pressure_loss_from_fittings(1.65,0)
test3 = pressure_loss_from_fittings(1.65,2)
test4 = pressure_loss_from_fittings(1.75,2)
test5 = pressure_loss_from_fittings(1.75,5)

# print(test1)
# print(test2)
# print(test3)
# print(test4)
# print(test5)

print()
print(approx(test3,0.001))
print(approx(-0.109,0.001))
print(test3==approx(-0.109,0.001))
print()
print(approx(test4,0.001))
print(approx(-0.122,0.001))
print(test4==approx(-0.122,0.001))
print()
print(approx(test5,0.01))
print(approx(-0.306,0.001))
print(test5==approx(-0.306,0.001))
print()
# print(0 == -0)