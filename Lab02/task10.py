def build_message(**info):
    message = "Here is the information you provided:\n"
    for key, value in info.items():
        message += f"{key}: {value}\n"
    
    return message
if __name__ == "__main__":
    user_info = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "occupation": "Engineer"
    }
    
    result_message = build_message(**user_info)
    print(result_message)
