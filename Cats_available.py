from CatsOnline import Cat

cats = [
{
     "name": "Феликс",
     "gender": "Мальчик",
     "age": "2",
    },
{
     "name": "Сэм",
     "gender": "Мальчик",
     "age": "2",
    },
]

print('Коты в наличии')
print('^^^^^^^^^^^^^^^')

for pet in cats:
    unit = Cat(name=pet.get("name"), gender=pet.get("gender"), age=pet.get("age"))
    print(unit.name)
    print(unit.gender)
    print(unit.age)
    print()

print('^^^^^^^^^^^^^^^')
