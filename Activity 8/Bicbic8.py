class Dog():
    Color = ""
    Breed = ""
    Size = ""

Marmar = Dog()
Marmar.Color = "Dark Brown"
Marmar.Breed = "Burmese"
Marmar.Size = "Mediumly Large"

Marbe = Dog()
Marbe.Color = "Tan"
Marbe.Breed = "Golden Retriever"
Marbe.Size = "Petite"

Margo = Dog()
Margo.Color = "Brownish Yellow"
Margo.Breed = "Lion"
Margo.Size = "Medium"

print("Here are some of the available dogs for ADOPTION!")
print("")
print("Marmar: " + "Color: " + Marmar.Color + "   Breed: " + Marmar.Breed + "   Size: " + Marmar.Size)
print("Marbe: " + "Color: " + Marbe.Color + "   Breed: " + Marbe.Breed + "   Size: " + Marbe.Size)
print("Margo: " + "Color: " + Margo.Color + "   Breed: " + Margo.Breed + "   Size: " + Margo.Size)

Marmar.Color = "Purple"
Marbe.Breed = "Maltese"
Margo.Size = "Extra Large"

print("")
print("Here are some of the MODIFIED dogs for adoption!")
print("")
print("Marmar: " + "Color: " + Marmar.Color + "   Breed: " + Marmar.Breed + "   Size: " + Marmar.Size)
print("Marbe: " + "Color: " + Marbe.Color + "   Breed: " + Marbe.Breed + "   Size: " + Marbe.Size)
print("Margo: " + "Color: " + Margo.Color + "   Breed: " + Margo.Breed + "   Size: " + Margo.Size)