def calculate_discount(price,discount_percent):
    disc_per = discount_percent / 100
    if (disc_per) >= 20/100:
        discounted_price = disc_per * price
        return price - discounted_price
    return price

user_price_prompt = int(input("Enter original price: "))
user_percentage_prompt = int(input("Enter discount percentage: "))
user_percentage_prompt = input(int("Enter discount percentage: "))

print(calculate_discount(user_price_prompt,user_percentage_prompt))