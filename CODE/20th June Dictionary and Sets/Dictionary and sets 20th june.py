meaning = {
              "car": "a vehicle",  #add comma "," after every meaning.
              "bullet": "a projectile",
              "values": [1,2,3,4],
              "TrueFalse": (14>=15) #you can use this for integers, floats, or booleans.
}

print(meaning["bullet"])
print(meaning["values"])
print(meaning["TrueFalse"])
print(meaning.get("sudhir")) #here key sudhir isnt present but .get funtion will return "none" as an output instead of giving an error