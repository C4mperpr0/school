with open("Veranstaltungen.html", "r") as file:
    data = file.read()
data = data.split("<h1>Veranstaltungen</h1>")[1]
data = data.split('<div id="footer">')[0]
data = data.split("Admin: Bearbeiten</a>")
print(len(data))

def filter(string):
    if "sport" in string.lower():
        return True

accepted = []
for i in range(len(data)):
    if filter(data[i]):
        accepted.append(data[i])

print(f"Found {len(accepted)}")
with open("results.txt", "w+") as file:
    for d in data:
        file.write(d+"\n\n\n\n\n")
