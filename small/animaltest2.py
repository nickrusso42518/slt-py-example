import dog, cat
my_animals = [
    dog.Dog('friendly', 'big'),
    cat.Cat('meow', 'tiny')
]
for my_animal in my_animals:
    print(my_animal.get_info())
