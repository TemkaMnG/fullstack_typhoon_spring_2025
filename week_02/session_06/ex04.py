total_purchase = float(input("Hudaldan avaltiin dun: "))
is_member = input("Ta gishuun uu? (Tiim/Vgvi)").lower() == "tiim"

if total_purchase >= 100:
    if is_member:
        discount = 0.2 # 20% hungulult
    else:
        discount = 0.1 # 10% hungulult
elif total_purchase >= 50:
    if is_member:
        discount = 0.1  # 10% hungulult
    else:
        discount = 0.5  # 5% hungulult
else:
    if is_member:
        discount = 0.05 # 5% hungulult
    else:
        discount = 0    # hungulult

final_price = total_purchase * (1 - discount)
print(f"Tanii tuluh dun: {final_price:2f}")