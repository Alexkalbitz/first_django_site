items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

for this in items:
    print((this.replace(" (", "").replace(")", "")))
