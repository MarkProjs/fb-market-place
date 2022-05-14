from django.contrib.auth.models import User, Group
from .models import Product
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
        'address': '6940 Monkey Street',
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
]


group_member = Group.objects.get(name="Members")


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
