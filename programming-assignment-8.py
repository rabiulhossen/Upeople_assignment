import json

def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if isinstance(value, list):
            for v in value:
                if v not in inverted_dict:
                    inverted_dict[v] = [key]
                else:
                    inverted_dict[v].append(key)
        else:
            if value not in inverted_dict:
                inverted_dict[value] = [key]
            else:
                inverted_dict[value].append(key)
    return inverted_dict

# Read from the input file
try:
    with open("input_file.json", "r") as file:
        original_dict = json.load(file)

    # Invert the dictionary
    inverted_dict = invert_dictionary(original_dict)

    # Write to the output file
    with open("output_file.json", "w") as file:
        json.dump(inverted_dict, file, indent=4)

    print("Dictionary inverted successfully!")

except FileNotFoundError:
    print("Input file not found.")
except json.JSONDecodeError:
    print("Error decoding JSON from the input file.")
except Exception as e:
    print(f"An error occurred: {e}")
