# There’s a function called bool knows(int a, int b) that returns a boolean value, indicating whether person 'a' knows person 'b'. The integers range from 1 to N. The task is to identify the prime minister, defined as a person who is known by everyone else (from 1 to N) but does not know anyone else.

# The conditions are as follows:

# bool knows(any number, prime minister) = true

# bool knows(prime minister, any number) = false

# It’s important to note that the specific boolean values returned by the knows function are uncertain and can be random, but the two conditions mentioned above must be satisfied.

# For example, if we have an array arr = [1,2,3,4,5] and designate 4 as the prime minister, the boolean function knows(4,1), knows(4,2), knows(4,3), and knows(4,5) would all return false because the prime minister knows no one. On the other hand, knows(1,4), knows(2,4), knows(3,4), and knows(5,4) would all return true since everyone else knows the prime minister.
def knows(a, b):
    return False
def is_prime_minister(person, knows):
    # Check if the person is known by everyone else
    for i in range(1, person):
        if not knows(i, person):
            return False
        # Check if the person does not know anyone else
        return True

    