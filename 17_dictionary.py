
capitals = {"Pakistan":"Islamabad",
            "India":"New Delhi",
            "Germany":"Berlin",
            "Russia":"Moscow",
            "Turkey":"Istanbul"}

#print(capitals.get("Russia"))
#print(capitals.get("Japan"))
#capitals.update({"India":"Mumbai"})
#capitals.pop("India")
#capitals.popitem()
#capitals.clear()

#for key in capitals.keys():
 #   print(key)
#for value in capitals.values():
  #  print(value)
for key, value in capitals.items():
    print(f"{key} : {value}")

#print(capitals)