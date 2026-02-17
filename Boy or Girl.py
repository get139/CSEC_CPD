user_name = input()
empty = (user_name == "")
distinct_count = len(set(user_name))

if user_name == user_name.lower() and not empty and len(user_name) <= 100 and distinct_count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
