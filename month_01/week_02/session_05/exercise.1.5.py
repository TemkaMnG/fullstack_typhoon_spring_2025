# Дасгал 1.5: Олон Мөрийн Оролт
# Зорилго: Хэрэглэгч олон мөр теĸст оруулах боломжтой програм үүсгэх

# Заавар:
# Хэрэглэгч шинэ мөрөнд "ДУУСАВ" гэж бичих хүртэл олон мөр теĸст оруулах боломжийг олгоно
# Оролт дууссаны дараа мөрийн дугаартай бүх теĸстийг харуулна

# Санал болгох алхамууд:
# Тэмдэглэлээ оруулахыг хэрэглэгчээс хүсэх
# Тэмдэглэлийн мөрүүдийг нэг нэгээр авах
# "ДУУСАВ" гэсэн оролт ирэх хүртэл үргэлжлүүлэх
# Цуглуулсан тэмдэглэлийг мөрийн дугаартай хамт харуулах


#bagshaas asuuh

print("Текстээ оруулна уу. Зогсоохдоо 'ДУУСАВ' гэж бичнэ үү:")
lines = []
while True:
    line = input()
    if line.lower() == "ДУУСАВ":  # Зогсоох команд
        break
    lines.append(line)

# Оруулсан текстийг хэвлэх
print("\nТаны оруулсан текст:")
for text in lines:
    print(text)
