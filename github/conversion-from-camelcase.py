def from_camel_case(name):
    us_name = ''
    for i in name[1:]:
        if i.isupper():
            us_name += '_' + i.lower()
        else:
            us_name += i
    return name[0].lower() + us_name

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")