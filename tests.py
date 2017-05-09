from treasure_counter import count_treasure

# Chest 1
chest1 = ["lobster",
          5,
          "seaweed",
          6.5]
print("Chest 1. Actual: 11.5 Calculated: {}".format(count_treasure(chest1)))

# Chest 2
chest2 = [True, False, 1, ["lobster"]]
print("Chest 2. Actual: 1 Calculated: {}".format(count_treasure(chest2)))

# Chest 3
chest3 = [1, 1, 1, True, "",
         ["salt water", "fools gold", 1,
         [1, "1", False]]]
print("Chest 3. Actual: 5 Calculated: {}".format(count_treasure(chest3)))

# These tests are meant to be helpful, but not exhaustive. You should add your
# own teses and be sure to consider edge cases.
