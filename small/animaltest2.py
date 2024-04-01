import dog, cat
cartoons = [
    cat.Cat(" ren  ", True),
    dog.Dog("stimpy", 25)
]
for cartoon in cartoons:
    print(cartoon.feed())
