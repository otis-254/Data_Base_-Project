import csv

with open("data.csv") as file: 
    reader = csv.reader(file)
    # print(list(reader))

    for row in reader: #This reads items on rows
        print(row)
    # reader.writerow(["user_id", "first_name", "last_name", "phone", "altar"])
    # reader.writerow([1, "Caleb", "Otis", +254714531574, "Kiwanja" ])
    # reader.writerow([2, "Mike", "Kip", +254714531574, "Juja" ])
    # writer.writerow([3, "Wilson", "Doe", +254714531574, "Gith 45" ])
    # writer.writerow([4, "Jonh", "Doe", +254714531574, "KU" ])
    # writer.writerow([5, "Lifty", "Williams", +254714531574, "Wangige" ])
    # writer.writerow([6, "Alice", "Wahome", +254714531574, "Roysambu" ])
    # writer.writerow([7, "Janet", "Atieno", +254714531574, "Mwiki" ])
    # writer.writerow([8, "Bonface", "Kip", +254714531574, "Tatu City" ])
    # writer.writerow([9, "Mikla", "Kip", +254714531574, "Juja" ])


