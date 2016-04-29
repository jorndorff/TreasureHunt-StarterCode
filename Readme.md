Big Idea
--------
The main component of this project is the count_treasure function which takes a list representing the contents of a treasure chest, and returns the total amount of treasure found in the chest. 

Counting the Contents
---------------------
There are several types of objects that you can find in a treasure chest, and must treat them appropriately. Different items will be handled according to their data type.
- **ints and floats** represent treasure. The value values should be added together and ultimately returned as the answer.
- **strings and bools** represent junk. This random junk such as lobsters, seaweed, etc should just be thrown back into the ocean. It has no value.
- **lists** are smaller treasure chests found within the bigger chest. They should be opened and tallied as well. Chests can be found within chests withing chests arbitrarily deeply.

### Treasure debt
Negative ints or floats represent promisory notes (debts) found in the chest. By default the debts should be thrown back into the ocean, but ethical pirates may choose to repay them (by adding the negative value onto the total treasure) by passing True to the optional payDebts argument.

Usage
-----
Run the program from a command line by CDing into the project directory an executing:
`python3 treasure-main.py`

The program will generate a random treasure chest and ask whether you'd like to repay your debts.
Then it will tell you how rich you got.

Author Info
-----------
Solution implemented by <your name here>

Project details written by Josh Orndorff
