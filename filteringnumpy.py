#filtering refers to selecting elements from an array based on a condition.
import numpy as np
ages=np.array([[21,7,19,20,16,30,18,65],
               [25,35,45,55,65,75,85,95]])
teenagers=ages[(ages<18)]
adults=ages[(ages>=18) & (ages<65)]
seniors=ages[ages>=65]
evens=ages[ages%2==0]
odds=ages[ages%2!=0]
print(f"Even ages: {evens}, \nOdd ages: {odds}")
print(f"Teenagers: {teenagers}, \nAdults: {adults}, \nSeniors: {seniors}")
adults =np.where(ages>=18,ages,0) #sets all values less than 18 to 0
print(adults)
