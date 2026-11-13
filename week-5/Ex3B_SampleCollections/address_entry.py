contact_info = {"name": "Jacob Murray", 
                "address": "1100 Maxwell Ct.", 
                "city": "Philadelphia", 
                "state": "PA", 
                "zip": "45302"}

#2
print(f"{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

#3
contact_info.pop("name")

#4
full_name = {
    "first name": "Jacob",
    "last name": "Murray"
}

#5
full_name.update({"honorific": "Mr."})

#6
contact_info.update(full_name)

#7
print(f"{contact_info['honorific']} {contact_info['first name']} {contact_info['last name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

