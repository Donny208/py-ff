import requests as r
import time
import shutil
from tqdm import tqdm

npc_list_req = r.get("https://flyff-api.sniegu.fr/item")
npc_list = npc_list_req.json()

for npc_id in tqdm(npc_list[2470::]):
    npc_req = r.get("https://flyff-api.sniegu.fr/item/"+str(npc_id))
    if "icon" in npc_req.json():
        image_name = npc_req.json()["icon"]
        npc_image = r.get(f"https://flyff-api.sniegu.fr/image/item/{image_name}", stream=True)
        with open(f"./Item Images/{str(npc_id)}-{npc_req.json()['name']['en']}.png", 'wb') as f:
            shutil.copyfileobj(npc_image.raw, f)
        print(f"Saved {image_name}")
    time.sleep(1.1)

