# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:13:35 2022

Fall 2022 Projects

@author: c.s.francis
"""

import Animal as a

fluf = a.Animal("Fluffy", 5, 9, "meow")
spark = a.Animal("Sparky", 1, 28, "woof")
fish = a.Animal("Fishy", 3, 1, "splash")


print(fluf)
print(spark)
print(fish)

print(spark.makeSound())


print(fluf == spark)

spark.setAge(5)

print(fluf == spark)




















