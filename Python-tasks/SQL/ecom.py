import psycopg2
import json
import random

conn = psycopg2.connect(user="postgres", password = "pg@dmin", host = "localhost", port = "5432", database = "ecom")
cursor = conn.cursor()


# query = """
#     CREATE TABLE product (
#         id SERIAL PRIMARY KEY,
#         title VARCHAR(100) NOT NULL,
#         price FLOAT NOT NULL,
#         seller_id INTEGER,
#         FOREIGN KEY (seller_id) REFERENCES seller (id)
#     );

# """

# query = """
#     CREATE TABLE tag (
#         id SERIAL PRIMARY KEY,
#         title VARCHAR(100) NOT NULL
#     );

# """



# query = """
#     CREATE TABLE seller (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100) NOT NULL
#     );

# """



# query = """
#     CREATE TABLE customer (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100) NOT NULL
#     );

# """


# query = """
#     CREATE TABLE wishlist (
#         id SERIAL PRIMARY KEY,
#         customer_id INTEGER NOT NULL UNIQUE,
#         FOREIGN KEY (customer_id) REFERENCES custumer (id)
#     );

# """


# query = """
#     CREATE TABLE review (
#         id SERIAL PRIMARY KEY,
#         product_id INTEGER NOT NULL,
#         customer_id INTEGER NOT NULL,
#         rate INTEGER NOT NULL,
#         FOREIGN KEY (product_id) REFERENCES product (id),
#         FOREIGN KEY (customer_id) REFERENCES custumer (id)
#     );

# """



# query = """
#     CREATE TABLE product_tags (
#         id SERIAL PRIMARY KEY,
#         product_id INTEGER NOT NULL,
#         tag_id INTEGER NOT NULL,
#         FOREIGN KEY (product_id) REFERENCES product (id),
#         FOREIGN KEY (tag_id) REFERENCES tag (id)
#     );

# """

customer_json = [{
  "name": "Halette Milberry"
}, {
  "name": "Barby Wastell"
}, {
  "name": "Lexie Dragon"
}, {
  "name": "Rosamond Kynston"
}, {
  "name": "Christen Keyson"
}, {
  "name": "Madeline Knottley"
}, {
  "name": "Ruby Loachhead"
}, {
  "name": "Aeriel Knowlden"
}, {
  "name": "Hedy Phillipp"
}, {
  "name": "Harmonia Freckelton"
}, {
  "name": "Rossy Mustchin"
}, {
  "name": "Dulcie Higgonet"
}, {
  "name": "Kala Caldroni"
}, {
  "name": "Nessie Lavery"
}, {
  "name": "Shanta Polotti"
}, {
  "name": "Berty Dampier"
}, {
  "name": "Frans Fosdike"
}, {
  "name": "Lotty Corkhill"
}, {
  "name": "Randie Lawther"
}, {
  "name": "Husain Reye"
}, {
  "name": "Fayre McPhillimey"
}, {
  "name": "Susette Raitie"
}, {
  "name": "Sela Elsmore"
}, {
  "name": "Taddeo Enterlein"
}, {
  "name": "Valma Hutchence"
}, {
  "name": "Micki Gorelli"
}, {
  "name": "Arabelle Najera"
}, {
  "name": "Annemarie Crenage"
}, {
  "name": "Nara Whight"
}, {
  "name": "Borg Downage"
}, {
  "name": "Sheri Moreman"
}, {
  "name": "Hew Dignum"
}, {
  "name": "Jacquenette Caygill"
}, {
  "name": "Margot Cradduck"
}, {
  "name": "Adele Snassell"
}, {
  "name": "Caryl Pevsner"
}, {
  "name": "Gannon Northrop"
}, {
  "name": "Artemas Goodlip"
}, {
  "name": "Lawrence Crockatt"
}, {
  "name": "Sheelagh Cosely"
}, {
  "name": "Doralyn Tripett"
}, {
  "name": "Grove Learman"
}, {
  "name": "Rosanna Pretious"
}, {
  "name": "Earle Sapshed"
}, {
  "name": "Guido Onyon"
}, {
  "name": "Rolfe Panner"
}, {
  "name": "Hilly Dashwood"
}, {
  "name": "Orland Shutt"
}, {
  "name": "Kipp Blacksell"
}, {
  "name": "Umberto Chaman"
}]



# for info in customer_json:
#     cursor.execute("INSERT INTO customer (name) VALUES (%s)", (info['name'],))
#     conn.commit()


seller_json = [{
  "name": "Si Friary"
}, {
  "name": "Scotty Ludlem"
}, {
  "name": "Randa Ifill"
}, {
  "name": "Vanessa Fay"
}, {
  "name": "Tamarra Tossell"
}, {
  "name": "Kennett Dumper"
}, {
  "name": "Jessika Stienham"
}, {
  "name": "Perry Branscombe"
}, {
  "name": "Salaidh Schultz"
}, {
  "name": "Nicolis Stonman"
}, {
  "name": "Michale Brecknock"
}, {
  "name": "Marian Withinshaw"
}, {
  "name": "Lynea Benit"
}, {
  "name": "Cale Giacometti"
}, {
  "name": "Ave Jahnisch"
}, {
  "name": "Aurelea Adshed"
}, {
  "name": "Pavlov Borham"
}, {
  "name": "Lamont McCanny"
}, {
  "name": "Rustie Troyes"
}, {
  "name": "Ivory Vina"
}]



# for info in seller_json:
#     cursor.execute("INSERT INTO seller (name) VALUES (%s)", (info['name'],))
#     conn.commit()



tag_json = [
    {
        "title": "Cheese"
    },
    {
        "title": "Chocolate"
    },
    {
        "title": "Vanillia"
    },
    {
        "title": "Vegetable"
    },
    {
        "title": "Vegan"
    },
    {
        "title": "Healthy"
    },
    {
        "title": "Fit"
    },
    {
        "title": "Meal"
    },
    {
        "title": "Fast Food"
    }
]

# for info in tag_json:
#     cursor.execute("INSERT INTO tag (title) VALUES (%s)", (info['title'],))
#     conn.commit()


product_json = [
   {
      "title": "M&M Food Market",
      "price": "17.0616609356653"
   },
   {
      "title": "Soprole",
      "price": "11.6234613464323"
   },
   {
      "title": "Kinder",
      "price": "2.62073436454904"
   },
   {
      "title": "Andy Capp's fries",
      "price": "14.6864611770429"
   },
   {
      "title": "Bewley's",
      "price": "7.01804420073426"
   },
   {
      "title": "Vitta Foods",
      "price": "4.5093621385793"
   },
   {
      "title": "Taco Bell",
      "price": "19.1318949810843"
   },
   {
      "title": "Sun-Pat",
      "price": "9.6603184191791"
   },
   {
      "title": "Baskin robbins",
      "price": "16.105171543595"
   },
   {
      "title": "Wendy's",
      "price": "5.43620887838128"
   },
   {
      "title": "Cobblestone",
      "price": "7.22419333514953"
   },
   {
      "title": "Wonder Bread",
      "price": "14.6278888390529"
   },
   {
      "title": "Lavazza",
      "price": "10.305469252777"
   },
   {
      "title": "Kinder",
      "price": "19.4697343713929"
   },
   {
      "title": "Soprole",
      "price": "16.3448767300439"
   },
   {
      "title": "Nabisco",
      "price": "2.48867588838966"
   },
   {
      "title": "Tic Tac",
      "price": "2.60812248457601"
   },
   {
      "title": "Magnum",
      "price": "19.4421954995218"
   },
   {
      "title": "Papadopoulos",
      "price": "19.4472127819654"
   },
   {
      "title": "Wonder Bread",
      "price": "12.7520409541913"
   },
   {
      "title": "Papadopoulos",
      "price": "1.811215852765"
   },
   {
      "title": "Olymel",
      "price": "7.34511601847835"
   },
   {
      "title": "Domino",
      "price": "7.64364533249459"
   },
   {
      "title": "Pizza Hut",
      "price": "12.6648227300797"
   },
   {
      "title": "Red Lobster",
      "price": "10.0007594130005"
   },
   {
      "title": "Andy Capp's fries",
      "price": "18.5981898673802"
   },
   {
      "title": "Secret Recipe",
      "price": "18.6991437984161"
   },
   {
      "title": "Sun-Pat",
      "price": "3.15631274094633"
   },
   {
      "title": "Magnum",
      "price": "10.3542353042188"
   },
   {
      "title": "Heinz",
      "price": "17.7369680049536"
   },
   {
      "title": "Olymel",
      "price": "19.9154627821015"
   },
   {
      "title": "Taco Bell",
      "price": "10.9514749045258"
   },
   {
      "title": "Dunkin' Donuts",
      "price": "11.479457990024"
   },
   {
      "title": "Applebee's",
      "price": "15.7718961763996"
   },
   {
      "title": "Knorr",
      "price": "10.4961827092321"
   },
   {
      "title": "KFC",
      "price": "12.4794360452702"
   },
   {
      "title": "Domino",
      "price": "17.0641279993877"
   },
   {
      "title": "Knorr",
      "price": "2.66790023197788"
   },
   {
      "title": "Kits",
      "price": "18.8862874209351"
   },
   {
      "title": "Dunkin' Donuts",
      "price": "7.84475450163929"
   },
   {
      "title": "Applebee's",
      "price": "13.4456292886499"
   },
   {
      "title": "Nutella",
      "price": "4.63776473637566"
   },
   {
      "title": "Bewley's",
      "price": "13.0057596485157"
   },
   {
      "title": "Kits",
      "price": "1.38640394266062"
   },
   {
      "title": "Nesquik",
      "price": "6.1496629436266"
   },
   {
      "title": "KFC",
      "price": "15.6723103028128"
   },
   {
      "title": "Andy Capp's fries",
      "price": "17.8805946269448"
   },
   {
      "title": "Tic Tac",
      "price": "7.01679017348997"
   },
   {
      "title": "Andy Capp's fries",
      "price": "7.87038087466284"
   },
   {
      "title": "Bel Group",
      "price": "10.6127773935966"
   }
]



# cursor.execute("SELECT id FROM seller")
# seller_id_list = []
# seller_ids = cursor.fetchall()
# for seller_id in seller_ids:
#     seller_id_list.append(seller_id[0])


# for product_info in product_json:
#     random_seller_id = random.choice(seller_id_list)
#     cursor.execute("INSERT INTO product (title, price, seller_id) VALUES (%s, %s, %s)", (product_info['title'], product_info['price'], random_seller_id))
#     conn.commit()



# cursor.execute("SELECT id FROM customer")
# customer_ids = cursor.fetchall()
# for customer_id in customer_ids:
#     cursor.execute("INSERT INTO wishlist (customer_id) VALUES (%s)", (customer_id[0],))
#     conn.commit()


cursor.execute("SELECT id FROM customer")
customer_id_list = []
customer_ids = cursor.fetchall()
for customer_id in customer_ids:
    customer_id_list.append(customer_id[0])


cursor.execute("SELECT id FROM product")
product_id_list = []
product_ids = cursor.fetchall()
for product_id in product_ids:
    product_id_list.append(product_id[0])

for product_id in product_id_list:

    for i in range(1,5):
        rate = random.randint(1,5)
        random_customer_id = random.choice(customer_id_list)
        cursor.execute("INSERT INTO review (product_id, customer_id, rate) VALUES (%s, %s, %s)", (product_id, random_customer_id, rate))
        conn.commit()


