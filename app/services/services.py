from fastapi import HTTPException

class ExampleService:
    def __init__(self):
        self.data = []

    def create_item(self, item: dict):
        if not item.get("name"):
            raise HTTPException(status_code=400, detail="Item must have a name")
        self.data.append(item)
        return item

    def get_items(self):
        return self.data

    def get_item(self, item_id: int):
        if item_id < 0 or item_id >= len(self.data):
            raise HTTPException(status_code=404, detail="Item not found")
        return self.data[item_id]

    def update_item(self, item_id: int, item: dict):
        if item_id < 0 or item_id >= len(self.data):
            raise HTTPException(status_code=404, detail="Item not found")
        if not item.get("name"):
            raise HTTPException(status_code=400, detail="Item must have a name")
        self.data[item_id] = item
        return item

    def delete_item(self, item_id: int):
        if item_id < 0 or item_id >= len(self.data):
            raise HTTPException(status_code=404, detail="Item not found")
        return self.data.pop(item_id)