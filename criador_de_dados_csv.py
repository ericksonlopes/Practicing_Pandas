from faker import Faker

fake = Faker('pt-br')

for item in dir(fake):
    print(item)
print(fake.estado_sigla())

print()

# with open('data.csv', encoding='utf-8') as arquivo:
#     arquivo.write('nome,idade,email,telefone,uf,genero musical,')
