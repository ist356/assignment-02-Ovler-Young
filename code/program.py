import json

def parse_packaging(package_desc):
    # Implement parsing logic
    # Example return format: [{'eggs': 12}, {'carton': 1}]
    items = package_desc.split(" / ")
    parsed = []
    for item in items:
        parts = item.split(" in ")
        amount, unit = parts[0].split(' ', 1)
        parsed.append({unit: int(amount)})
    return parsed

def calc_total_units(parsed_items):
    total = 1
    for item in parsed_items:
        for _, amount in item.items():
            total *= amount
    return total

def get_unit(parsed_items):
    # Assume the unit to be the first item's key
    return list(parsed_items[0].keys())[0]

def main():
    with open('data/packaging.txt', 'r') as f:
        lines = f.readlines()
    
    all_packages = []

    for line in lines:
        package_desc = line.strip()
        parsed_items = parse_packaging(package_desc)
        total_units = calc_total_units(parsed_items)
        unit = get_unit(parsed_items)
        print(f"{package_desc} => total units: {total_units} {unit}")
        all_packages.append(parsed_items)

    with open('data/packaging.json', 'w') as json_file:
        json.dump(all_packages, json_file, indent=4)

if __name__ == "__main__":
    main()
