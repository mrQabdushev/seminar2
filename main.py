from myclass import Jic
from mybox import Task2

# a = Jic(15, "Ertik")
# a.monkeys()
# a.E_group()
#
# b = Jic(10, "Vasya")
# b.monkeys()
# b.E_group()


bag = Task2()
bag.add('salam')
bag.add(1)
bag.add(', ')
bag.add(True)
bag.add('bob')
bag.remove(True)

if (1 in bag) and (len(bag)>0):
    bag.remove(1)

msg = ''
for bg in bag:
    msg += bg

print(msg)