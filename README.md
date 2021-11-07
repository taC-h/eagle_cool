

https://api.eagle.cool/

```python
from eagle_cool import Eagle
eagle = Eagle()

#https://api.eagle.cool/application/info
res = eagle.application_info()
assert res["status"] == "success"

#https://api.eagle.cool/item/add-from-url
data = {
    "url": "https://cdn.dribbble.com/users/674925/screenshots/12020761/media/" +
        "6420a7ec85751c11e5254282d6124950.png",
    "name": "Work",
    "website": "https://dribbble.com/shots/12020761-Work",
    "tags": ["Illustration", "Design"],
    "modificationTime": 1591325171766,
    "headers": {
        "referer": "dribbble.com"
    }
}
res = eagle.item_addFromURL(json=data)
assert res["status"] == "success"

#https://api.eagle.cool/folder/list
res = eagle.folder_list()
assert isinstance(res["data"], list)
assert isinstance(res["data"]["imageCount"], int)
```