'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    
            ("12 eggs in 1 carton", [{ 'eggs' : 12}, {'carton' : 1}]),
            ("6 bars in 1 pack / 12 packs in 1 carton", [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]),
            ("20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box", [{ 'pieces' : 20}, {'packs' : 10}, {'cartons' : 4}, {'box' : 1}]),
            ("2 foo in 1 bar / 3 bars in 1 baz / 4 baz in 1 qux / 2 qux in 1 biz ", [{ 'foo' : 2}, {'bars' : 3}, {'baz' : 4}, {'qux' : 2}, {'biz' : 1}]),
            ("25 balls in 1 bucket / 4 buckets in 1 bin", [{'balls' : 25}, {'buckets' : 4}, {'bin' : 1}]),
    '''
    package_list = []
    phrases = packaging_data.strip().split(' / ')
    for i, phrase in enumerate(phrases):
        parts = phrase.strip().split(' in ')
        if len(parts) != 2:
            continue  # Skip if the phrase is not in the expected format
        first_part, second_part = parts
        try:
            number1_str, item1 = first_part.strip().split(' ', 1)
            number1 = int(number1_str)
            number2_str, item2 = second_part.strip().split(' ', 1)
            number2 = int(number2_str)
        except ValueError:
            continue  # Skip if the numbers are not integers
        # Add the first item
        package_list.append({item1.strip(): number1})
        # Add the second item only if it's the last phrase
        if i == len(phrases) - 1:
            package_list.append({item2.strip(): number2})
    return package_list


def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''
    total = 1
    for item in package:
        total *= list(item.values())[0]
    return total


def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    return list(package[0].keys())[0]

# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")

