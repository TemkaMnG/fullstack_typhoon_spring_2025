def greeting(response):

    parts = response.split()

    name = parts[0]
    hobby = parts[2]

    return f"Hello, {name}! I also enjoy {hobby}!"


print(greeting("Jose 17 hockey"))
print(greeting("Cindy 14 robotics"))
