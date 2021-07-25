import requests as r
import time
import shutil
from tqdm import tqdm
from PIL import Image
import os
import mongoengine

mongoengine.register_connection(alias='flyff', name='flyff', host='localhost', port=27017)

import mongoengine

class Item(mongoengine.Document):
    itemId = mongoengine.IntField(required=True)
    name = mongoengine.StringField(required=True)
    description = mongoengine.StringField(required=True)
    icon = mongoengine.StringField(required=True)
    icon_url = mongoengine.StringField(required=True)
    category = mongoengine.StringField(required=True)
    subcategory = mongoengine.StringField()
    rarity = mongoengine.StringField(required=True)
    jobClass = mongoengine.IntField()
    level = mongoengine.IntField(required=True)
    sex = mongoengine.StringField()
    stack = mongoengine.IntField(required=True)
    buyPrice = mongoengine.IntField(required=True)
    sellPrice = mongoengine.IntField(required=True)
    consumable = mongoengine.BooleanField(required=True)
    premium = mongoengine.BooleanField(required=True)
    deletable = mongoengine.BooleanField(required=True)
    tradable = mongoengine.BooleanField(required=True)
    shining = mongoengine.BooleanField(required=True)
    element = mongoengine.StringField(required=True)
    durationRealTime = mongoengine.BooleanField(required=True)
    cooldown = mongoengine.IntField()
    casting = mongoengine.IntField()
    duration = mongoengine.IntField()
    flightSpeed = mongoengine.IntField()
    attackSpeed = mongoengine.StringField()
    attackRange = mongoengine.IntField()
    twoHanded = mongoengine.BooleanField()
    minAttack = mongoengine.IntField()
    maxAttack = mongoengine.IntField()
    additionalSkillDamage = mongoengine.IntField()
    consumedMP = mongoengine.IntField()
    consumedItem = mongoengine.StringField()
    triggerSkill = mongoengine.IntField()
    triggerSkillProbability = mongoengine.IntField()
    minDefense = mongoengine.IntField()
    maxDefense = mongoengine.IntField()
    blinkwingTarget = mongoengine.DictField()
    abilities = mongoengine.ListField()
    spawns = mongoengine.ListField(default=[])
    meta = {
        'db_alias': 'flyff',
        'collection': 'items'
    }



item_list = Item.objects()

npc_list_req = r.get("https://flyff-api.sniegu.fr/item")
npc_list = npc_list_req.json()

for item in tqdm(item_list):
    if "icon" in item:
        npc_image = r.get(item.icon_url, stream=True)
        file = None
        if not os.path.isdir(f"./Item Images/{item['category']}/"):
            os.mkdir(f"./Item Images/{item['category']}/")
        if 'subcategory' in item:
            if not os.path.isdir(f"./Item Images/{item['category']}/{item['subcategory']}/"):
                os.mkdir(f"./Item Images/{item['category']}/{item['subcategory']}/")
            file = f"./Item Images/{item['category']}/{item['subcategory']}/{str(item['itemId'])}-{item['name']}.png"
        else:
            file = f"./Item Images/{item['category']}/{str(item['itemId'])}-{item['name']}.png"
        with open(file, 'wb') as f:
            shutil.copyfileobj(npc_image.raw, f)
        print(f"Saved {item['icon']}")
    time.sleep(1)
#

# blank_image = Image.new("RGB", (4*256, 4*256))
# #blank_image = Image.open("map.png")
# for x in range(0,5):
#     for y in range(0,5):
#         print(f"{str(x)}:{str(y)}")
#         image_req = r.get(f"https://flyff-api.sniegu.fr/image/world/wdkebaras{str(x)}-{str(y)}-0.png", stream=True)
#         img = Image.open(image_req.raw)
#         blank_image.paste(img, (x*256, y*256))
#         blank_image.save("KebarasTileMap.png")
#         time.sleep(1.1)
# blank_image.save("map.png")
