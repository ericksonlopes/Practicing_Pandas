import random
from faker import Faker

fake = Faker('pt-br')

generos_muscais = ['Axé', 'Blues', 'Country', 'Eletrônica', 'Forró', 'Funk', 'Gospel', 'Hip Hop', 'Jazz', 'MPB',
                   'Música clássica', 'Pagode', 'Pop', 'Rap', 'Reggae', 'Rock', 'Samba', 'Sertanejo']

with open('data_inicial.csv', 'w', encoding='utf-8') as arquivo:
    arquivo.write('nome,idade,email,uf,genero_musical,linguagem\n')

    for item in range(40):
        linha = f'{fake.name()},' \
                f'{fake.random.randint(18, 70)},' \
                f'{fake.email()},' \
                f'{fake.estado_sigla()},' \
                f'{random.choice(generos_muscais)},' \
                f'{random.choice(["Python", "Java"])}\n'
        arquivo.write(linha)
