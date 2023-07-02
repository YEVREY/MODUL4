def func(text):
    reversed_text = text[::-1]
    if reversed_text == text:
        return True
    return False


print(func("лепсспел"))
print(func("helloworld"))