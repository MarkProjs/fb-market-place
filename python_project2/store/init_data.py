from django.contrib.auth.models import User, Group
from django.db.models import Avg
from .models import Product, Comment
from web_messaging.models import Message
import random as rnd


user_lst = [
    'Jeremy',
    'Jacky',
    'Amina',
    'Mark',
    'Charlie',
    'Manny',
    'Denis',
    'Emily',
    'Emma',
    'Frank',
]

product_lst = [
    {
        'owner': 'Jacky',
        'type': 'Electronics',
        'name': 'MSI Laptop',
        'price': 1799,
        'description': 'Laptop Used to make this website',
        'size': '17 inch',
        'image': 'default_product_img/jackylaptop.jpg',
        'address': '6940 Monkey Street',
        'status': 'Used'
    },
    {
        'owner': 'Jacky',
        'type': 'T-Shirt',
        'name': 'Monkey Shirt',
        'price': 25,
        'description': 'Limited edition Monkey Shirt by Gucci',
        'size': 'Large',
        'image': 'default_product_img/monkeyshirt.jpg',
        'address': '6940 Monkey Street',
        'status': 'New Limited Edition'
    },
    {
        'owner': 'Frank',
        'type': 'Shoes',
        'name': 'Monkey Slippers',
        'price': 19,
        'description': 'Limited edition Monkey Slippers',
        'size': 'Large',
        'image': 'default_product_img/monkeyslipper.jpg',
        'address': '2940 Avenue Pepega',
        'status': 'New'
    },
    {
        'owner': 'Frank',
        'type': 'Utilities',
        'name': 'Toilet Roll',
        'price': 2,
        'description': 'Extra Toilet roll from when I bought tons of toilet roll at the start of covid like it was stocks in the stock market',
        'size': 'Large',
        'image': 'default_product_img/toiletroll.jpg',
        'address': '2940 Avenue Pepega',
        'status': 'Refurbished'
    },
    {
        'owner': 'Emma',
        'type': 'Electronics',
        'name': 'PS3 Controller',
        'price': 14,
        'description': 'Used PS3 controller',
        'size': '',
        'image': 'default_product_img/ps3controller.jpg',
        'address': '240 Deron Street',
        'status': 'Used'
    },
    {
        'owner': 'Mark',
        'type': 'Shoes',
        'name': 'KAWS Air Force 1',
        'price': 200,
        'description': 'An all-white Air Force 1, but customized to be inspired by the company of Brian Donnelly aka KAWS.',
        'size': '9.5',
        'image': 'default_product_img/KAWS-Air-Force-1.jpg',
        'address': '159 Imaginary Street',
        'status': 'New'
    },
    {
        'owner': 'Denis',
        'type': 'Utilities',
        'name': 'Water Bottle (half-full)',
        'price': 5,
        'description': 'A water bottle to quench your thirst (someone was thirsty first).',
        'size': '',
        'image': 'default_product_img/used-water-bottle.jpg',
        'address': '199 Avenue Non-Existent',
        'status': 'Used'
    },
    {
        'owner': 'Manny',
        'type': 'Electronics',
        'name': 'Beats Studio Wireless Headphone',
        'price': 150,
        'description': 'A used Studio Beats. A bit of tear on the ear muffs.',
        'size': '',
        'image': 'default_product_img/BeatsHeadphone.jpg',
        'address': '169 Notanaddress Street',
        'status': 'Used'
    },
    {
        'owner': 'Mark',
        'type': 'Electronics',
        'name': 'Ps4 controller',
        'price': 80,
        'description': 'A used ps4 controller',
        'size': '',
        'image': 'default_product_img/ps4controller.jpg',
        'address': '159 Notreal Boulevard',
        'status': 'Used'
    },
    {
        'owner': 'Mark',
        'type': 'T-shirt',
        'name': 'Balenciaga t-shirt',
        'price': 1150,
        'description': 'Destroyed Flatground T-shirt in black and white vintage jersey.',
        'size': 'Medium',
        'image': 'default_product_img/balenciaga-tshirt.jpg',
        'address': '133 Nowhere Street',
        'status': 'New'
    },
    {
        'owner': 'Jeremy',
        'type': 'Shoes',
        'name': 'Left Blue Slippers',
        'price': 4,
        'description': 'Left Blue Slippers, Lost the other one...',
        'size': 'Medium',
        'image': 'default_product_img/leftblueslipper.jpg',
        'address': '420 Somewhere Street',
        'status': 'Used'
    },
    {
        'owner': 'Amina',
        'type': 'T-shirt',
        'name': 'Hiking t-shirt',
        'price': 50,
        'description': 'Made of soft organic cotton',
        'size': 'Medium',
        'image': 'default_product_img/hikingshirt.jpg',
        'address': '850 Lemon Street',
        'status': 'New'
    },
    {
        'owner': 'Jeremy',
        'type': 'Accessories',
        'name': 'Used Mask',
        'price': 2,
        'description': 'Mask that I used to go to school, dont worry I am triple vaxxed... You wont catch covid',
        'size': '',
        'image': 'default_product_img/usedmask.jpg',
        'address': '250 Covid Street',
        'status': 'Used'
    },
    {
        'owner': 'Charlie',
        'type': 'Electronics',
        'name': 'Old Alarm Clock',
        'price': 10,
        'description': 'Old school Alarm Clock',
        'size': '',
        'image': 'default_product_img/alarmclock.jpg',
        'address': '332 Nowhere Street',
        'status': 'Used'
    },
    {
        'owner': 'Charlie',
        'type': 'Books',
        'name': 'Cal-1 Manual',
        'price': 39,
        'description': 'Calculus 1 Manual, no notes written on it',
        'size': '',
        'image': 'default_product_img/cal1manual.jpg',
        'address': '332 Nowhere Street',
        'status': 'Refurbished'
    },
    {
        'owner': 'Denis',
        'type': 'Utilities',
        'name': 'Used Deodorant',
        'price': 9,
        'description': 'My old deodorant, I got myself some Old Spice, so Im selling this one',
        'size': '',
        'image': 'default_product_img/deodorant.jpg',
        'address': '552 IDontKnow Avenue',
        'status': 'Used'
    },
    {
        'owner': 'Emma',
        'type': 'Electronics',
        'name': '88-keys Keyboard',
        'price': 499,
        'description': 'Model Alesis, used but good as new.',
        'size': 'Medium',
        'image': 'default_product_img/piano.jpg',
        'address': '5322 Avenue Bonk',
        'status': 'Used'
    },
    {
        'owner': 'Emma',
        'type': 'Electronics',
        'name': 'Used Nintendo Switch',
        'price': 249,
        'description': 'Nintendo Switch, conditions are good as new.',
        'size': '',
        'image': 'default_product_img/nintendoswitch.jpg',
        'address': '5322 Avenue Bonk',
        'status': 'Used'
    },
    {
        'owner': 'Amina',
        'type': 'Electronics',
        'name': 'PS4',
        'price': 299,
        'description': 'Used PS4',
        'size': '',
        'image': 'default_product_img/ps4.jpg',
        'address': '850 Lemon Street',
        'status': 'New'
    },
    {
        'owner': 'Frank',
        'type': 'Electronics',
        'name': 'Piano Pedal',
        'price': 19,
        'description': 'Used piano pedal, works for any kind of electronic keyboards',
        'size': '',
        'image': 'default_product_img/pianopedal.jpg',
        'address': '2940 Avenue Pepega',
        'status': 'Used'
    },
]

group_member = Group.objects.get(name="Members")
obj_lst = []


def update_ratings(prod):
    avg_rating = Comment.objects.filter(product=prod).aggregate(Avg('rating'))
    prod.rate = avg_rating['rating__avg']
    prod.save()


def init_data():
    # Initialize Members
    for user in user_lst:
        new_user = User.objects.create_user(username=user, password='123')
        group_member.user_set.add(new_user)

    for product in product_lst:
        product = Product.objects.create(
            owner=User.objects.get(username=product['owner']),
            type=product['type'],
            name=product['name'],
            price=product['price'],
            description=product['description'],
            size=product['size'],
            image=product['image'],
            address=product['address'],
            status=product['status']
        )

        obj_lst.append(product)

    obj_lst[0].likes.add(User.objects.get(username='Frank'))
    obj_lst[0].likes.add(User.objects.get(username='Emma'))
    obj_lst[0].likes.add(User.objects.get(username='Amina'))
    obj_lst[0].likes.add(User.objects.get(username='Mark'))
    obj_lst[0].likes.add(User.objects.get(username='Jeremy'))

    Comment.objects.create(
        product=obj_lst[0],
        name=User.objects.get(username='Frank'),
        body='Thats a nice laptop, what are the specs ?',
        rating=3
    )

    Comment.objects.create(
        product=obj_lst[0],
        name=User.objects.get(username='Emma'),
        body='Very nicee',
        rating=4
    )

    update_ratings(obj_lst[0])

    obj_lst[1].likes.add(User.objects.get(username='Jeremy'))
    obj_lst[1].likes.add(User.objects.get(username='Mark'))
    obj_lst[1].likes.add(User.objects.get(username='Denis'))

    Comment.objects.create(
        product=obj_lst[1],
        name=User.objects.get(username='Denis'),
        body='Thats a cool shirt',
        rating=4
    )

    Comment.objects.create(
        product=obj_lst[1],
        name=User.objects.get(username='Mark'),
        body='I need this',
        rating=5
    )

    update_ratings(obj_lst[1])

    obj_lst[3].likes.add(User.objects.get(username='Jeremy'))
    obj_lst[3].flags.add(User.objects.get(username='Manny'))
    obj_lst[3].flags.add(User.objects.get(username='Frank'))
    obj_lst[3].flags.add(User.objects.get(username='Emma'))

    Comment.objects.create(
        product=obj_lst[3],
        name=User.objects.get(username='Jeremy'),
        body='Id like to order all your stocks bro',
        rating=5
    )

    Comment.objects.create(
        product=obj_lst[3],
        name=User.objects.get(username='Manny'),
        body='What in the worldd is this',
        rating=1
    )

    update_ratings(obj_lst[3])

    Message.objects.create(
        sender=User.objects.get(username='Jeremy'),
        receiver=User.objects.get(username='nasr'),
        message='Hello Sir'
    )

    Message.objects.create(
        sender=User.objects.get(username='Jeremy'),
        receiver=User.objects.get(username='Jacky'),
        message='Yo Slide me your stocks bruh, I need them for my collection'
    )

    Message.objects.create(
        sender=User.objects.get(username='Denis'),
        receiver=User.objects.get(username='Jacky'),
        message='Hello, I would like to negotiate the price for the laptop'
    )

    Message.objects.create(
        sender=User.objects.get(username='Manny'),
        receiver=User.objects.get(username='Jacky'),
        message='I would like to inquire on the specs of your laptop that you are selling'
    )




