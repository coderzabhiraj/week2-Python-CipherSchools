# def user_info(first_name,last_name,age=23):
def user_info(first_name,last_name='unknown',age='none'):#only last parameter can be made default or other can also be made default if and only if last parameter is also made default
    print(f"your First name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info('yash','tripathi')


