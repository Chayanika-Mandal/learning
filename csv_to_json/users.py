import csv
import json

with open("users.csv") as u:
    users_dict = csv.DictReader(
        u, fieldnames=["name", "age", "city", "username", "password"]
    )
    users = []
    for user in users_dict:
        user['age'] = int(user['age'])
        # user.update({"age": int(user["age"])})
        users.append(user)

with open("users.json", "w") as j:
    json.dump(users, j, indent=4)
