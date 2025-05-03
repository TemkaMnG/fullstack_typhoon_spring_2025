# Python -d temdegt muruud uurchlugdushgvi
s= "hello" #unmodifiable
print(s)
# s[0] = "H" Ene type error uusgene

# orond n shine temdegt mur vvsgeh
s = "H" + s[1:] # "Hello"
print(s)

# Temdegt muriin uildluudiig oilgoh
s1 = "hello"
s2 = s1.upper()
print(s1) #"hello"
print(s2) #"Hello"

# sanah oi nuluulnu
id_before = id(s1)
s1 = s1 +"world"    # shine temdegt muriin obiekt uusgene
id_after = id(s1)
print(id_before == id_after) # False - uur obiektuud

