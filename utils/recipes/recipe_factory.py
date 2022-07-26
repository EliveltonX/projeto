from random import randint
from string import digits
from faker import Faker

fake = Faker('pt_br')

def rand_ratio():
    return randint(840,900),randint(473,573)

def make_recipe():
    return{
        'id': fake.random_number(digits=2, fix_len=True),
        'title':fake.sentence(nb_words=6),
        'description':fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }        
    }