import random
from faker import Faker

fake = Faker('pt-br')

generos_muscais = ['Axé', 'Blues', 'Country', 'Eletrônica', 'Forró', 'Funk', 'Gospel', 'Hip Hop' ]

with open('data.csv', 'w',  encoding='utf-8') as arquivo:
    arquivo.write('nome,idade,email,uf,genero musical,linguagem\n')

    for item in range(40):
        linha = f'{fake.name()}, ' \
                f'{fake.random.randint(18, 100)}, ' \
                f'{fake.email()}, ' \
                f'{fake.estado_sigla()},' \
                f'{random.choice(generos_muscais)},' \
                f'{random.choice(["Python", "Java"])} \n'
        arquivo.write(linha)
