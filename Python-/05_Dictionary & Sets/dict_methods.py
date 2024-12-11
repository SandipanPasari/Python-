marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Renuka": 100})
print(marks)

print(marks.get("Harry"))
print(marks.get("Rohan"))
# print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error

game = {
    "Free Fire": 99,
    "BGMI": 34,
    "COD": 90
}
print(game["Free Fire"])

print(game.items())
print(game.keys()) 
print(game.values())
game.update({"COD": 377})
print(game)
print(game.get("Free Fire"))
print(game.get("BGMI"))