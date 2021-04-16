from faker import Faker

faker = Faker('pt-br')

generos_muscais = ['Axé', 'Blues', 'Country', 'Eletrônica', 'Forró', 'Funk', 'Gospel', 'Hip Hop', 'Jazz', 'MPB',
                   'Música clássica', 'Pagode', 'Pop', 'Rap', 'Reggae', 'Rock', 'Samba', 'Sertanejo']

linguagens = ['Java', 'C', 'C++', 'Python', 'C#', 'JavaScript', " Visual Basic . NET", 'R', 'PHP', 'MATLAB', 'Swift',
              'Objective-C', 'Assembly', 'Perl', 'Ruby', 'Delphi / Object Pascal', 'Go', 'Scratch', 'PL/SQL',
              'Visual Basic']

with open('dados.csv', 'w+', encoding='utf-8') as arquivo:
    arquivo.write('name,data_nasc,email,pontos,uf,linguagem,genero_musical\n')

    for linha in range(300):
        nome = faker.name()

        email = nome.replace(' ', '').lower() + '@' + faker.email().split('@')[1]
        if linha % 4 == 0:
            email = ''

        arquivo.write(
            f'{nome},'
            f'{faker.date_of_birth(minimum_age=18, maximum_age=70)},'
            f"{email},"
            f'{faker.random.randint(0, 100)},'
            f'{faker.estado_sigla()},'
            f'{faker.random.choice(linguagens)},'
            f'{faker.random.choice(generos_muscais)}\n'
        )
