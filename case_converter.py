def convert_to_snake_case(pascal_or_camel_cased_string):
    # Make a list with '_' before uppercase letters, and lowercase them
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join list to make a string, remove starting or ending '_'
    return ''.join(snake_cased_char_list).strip('_')

def main():
    user_input = input("Enter a CamelCase or PascalCase string: ")
    print(convert_to_snake_case(user_input))

main()