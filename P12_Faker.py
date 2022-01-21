from faker import Faker

fake = Faker()
name = fake.name()
print(name)
address = fake.address()
print(address)
text = fake.text()
print(text)
