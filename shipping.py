import random

weight = random.randint(1, 15)
cost_ground_premium = 125.00

print("Your package weight is: ", weight)
if weight <= 2:
  cost_ground = weight * 1.50 + 20
  cost_drone = weight * 4.50 + 125

elif weight >= 2 and weight <= 6:
  cost_ground = weight * 3 + 20
  cost_drone = weight * 9 + 125

elif weight >= 6 and weight <= 10:
  cost_ground = weight * 4 + 20
  cost_drone = weight * 12 + 125

else:
  cost_ground = weight * 4.75 + 20
  cost_drone = weight * 14.25 + 125

print("Ground Shipping Cost: $", cost_ground)
print("Ground Shipping Premium $", cost_ground_premium)
print("Done Shipping Cost: $", cost_drone )
