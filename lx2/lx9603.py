import csv

with open("tt.csv","w",encoding='utf-8') as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["Top Gun",
                "Risky Business",
                "Minority Report"])
    w.writerow(["Titanic",
                "The Revenant",
                "Inception"])
    w.writerow(["Titanic",
                "The Revenant",
                "Inception"])
