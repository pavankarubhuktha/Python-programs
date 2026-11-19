#8. Write a program on Serialization and Deserialization?
import pickle
data = {"name": "pavan", "age": "23","city":"vizag"}
file = open("data.plk","wb")
pickle.dump(data,file)
file.close()
print("completed")

with open("data.plk","rb") as file:
    new_data = pickle.load(file)
    print("Deserialized data:")
print(new_data)