#- Import the `string` library.
#- Create a variable `alphabet` that consists of the lowercase and uppercase letters in the English alphabet using the `ascii_letters` data attribute of the `string` library.
def counter(input_string):
    import string
    alphabet = string.ascii_letters

    count_letters = {}
    for letter in input_string:

        if letter in alphabet:

            if letter in count_letters:

                count_letters[letter] += 1

            else:

                count_letters[letter] = 1
    return count_letters


sentence = 'mamadou ndiaye'
print(counter(sentence))
address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. 
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- 
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add 
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so 
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of 
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""

# Write your code here!
address_count = counter(address)
print(address_count)
import math

m = max(address_count.values())


def find_key(v):
    for k, val in address_count.items():  # parcourir par deux k et val
        if v == val:
            return k
    return "Clé n'existe pas"


print(find_key(m))

# sing random.uniform(), create a function rand() that generates a single float between  −1  and  1 .
# all rand() once. For us to be able to check your solution, we will use random.seed() to fix the seed value of the random number generator.


import random

random.seed(1)  # Fixes the see of the random number generator.


def rand():
    # define `rand` here!
    return random.uniform(-1, 1)


print(rand())


# fonction pour calculer la distance entre deux vecteurs
def distance(x, y):
    # define your function here!
    return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)


print(distance((0, 0), (1, 1)))
print(distance((0.5, 1), (1, 0.5)))


def in_circle(x, origin=(0, 0)):
    if distance(x, origin) < 1:
        return True
    else:
        return False


print(in_circle((1, 1)))

random.seed(1)
R = 10000
inside = []
for i in range(R):
    point = [rand(), rand()]
    inside.append(in_circle(point))
print(inside)
print(sum(inside) / R)

print(0.779 - 0.785398)


def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors * 2 + 1
    x = [x[0]] * n_neighbors + x + [x[-1]] * n_neighbors

    return [sum(x[i:(i + width)]) / width for i in range(n)]


x = [0, 10, 5, 3, 1, 5]
print(moving_window_average(x, 1))
print(sum(moving_window_average(x,1)))

def rand():
    # define `rand` here!
    return random.uniform(-1, 1)


random.seed(1)  # This line fixes the value called by your function,
R = 1000
x = [random.random() for index in range(R)]
n_neighbors = [n_ for n_ in range(1, 10)]
Y = []
for n_neig in range(len(n_neighbors)):
    Y.append(moving_window_average(x, n_neig))
new_list = []
for y in range(len(n_neighbors)):
    new_list.append(max(Y[y]) - min(Y[y]))
print(new_list)
print(Y[5][10]) # parcourir liste dans liste
######enfin j'ai souffert
print(counter('Jim quickly realized that the beautiful gowns are expensive'))
print(math.pi / 4)
