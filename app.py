
import csv
from dataclasses import dataclass

@dataclass
class Spool:
    barcode: str
    manufacturer: str
    material: str
    color: str
    full_weight: int
    empty_weight: int

@dataclass
class Inventory:
    barcode: str
    manufacturer: str
    material: str
    color: str
    loose_weight: int
    full_spools: int
    total_weight: int

spoolList = []
inventoryList = []


def load_data():
    try:
        with open("spools.csv", newline="") as file:
            for row in csv.DictReader(file):
                spoolList.append(
                    Spool(
                        barcode=row["barcode"],
                        manufacturer=row["manufacturer"],
                        material=row["material"],
                        color=row["color"],
                        full_weight=int(row["full_weight"]),
                        empty_weight=int(row["empty_weight"]),
                    )
                )
    except FileNotFoundError:
        pass

    try:
        with open("inventory.csv", newline="") as file:
            for row in csv.DictReader(file):
                inventoryList.append(
                    Inventory(
                        barcode=row["barcode"],
                        manufacturer=row["manufacturer"],
                        material=row["material"],
                        color=row["color"],
                        loose_weight=int(row["loose_weight"]),
                        full_spools=int(row["full_spools"]),
                        total_weight=int(row["total_weight"]),
                    )
                )
    except FileNotFoundError:
        pass


def save_data():
    with open("spools.csv", "w", newline="") as file:
        fields = ["barcode", "manufacturer", "material", "color", "full_weight", "empty_weight"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for spool in spoolList:
            writer.writerow(spool.__dict__)

    with open("inventory.csv", "w", newline="") as file:
        fields = [
            "barcode",
            "manufacturer",
            "material",
            "color",
            "loose_weight",
            "full_spools",
            "total_weight",
        ]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for inventory in inventoryList:
            writer.writerow(inventory.__dict__)

def find_type(barcode) -> Spool | None:
    for spool in spoolList:
        if spool.barcode == barcode:
            return spool
    return None

def add_spool(spool: Spool):
    spoolList.append(spool)

def find_inventory(barcode) -> Inventory | None:
    for inventory in inventoryList:
        if inventory.barcode == barcode:
            return inventory
    
    spool_type = find_type(barcode)
    if spool_type is None:
        print("Spool type not found. Please add the spool type first.")
        return None
    
    new_inventory = Inventory(
        barcode=barcode,
        manufacturer=spool_type.manufacturer,
        material=spool_type.material,
        color=spool_type.color,
        loose_weight=0,
        full_spools=0,
        total_weight=0
    )
    inventoryList.append(new_inventory)
    return new_inventory

def main():
    load_data()

    while True:
        barcode = input("Barcode: ")

        spool_type = find_type(barcode)
        if spool_type is None:
            beep_error()
            manufacturer = input("Manufacturer: ")
            material = input("Material: ")
            color = input("Color: ")
            full_weight = int(input("Full weight: "))
            empty_weight = int(input("Empty weight: "))

            new_spool = Spool(
                barcode=barcode,
                manufacturer=manufacturer,
                material=material,
                color=color,
                full_weight=full_weight,
                empty_weight=empty_weight
            )
            add_spool(new_spool)
            spool_type = new_spool
        
        inv = find_inventory(barcode)

        amount_input = input("Amount: ")
        if amount_input == "s" or amount_input == barcode:
            inv.total_weight += spool_type.full_weight
            inv.full_spools += 1
        else:
            amount = int(amount_input)
            inv.loose_weight += amount - spool_type.empty_weight
            inv.total_weight += amount - spool_type.empty_weight
        beep_ok()
        save_data()


if __name__ == "__main__":
    main()
