class Team():
    def __init__(self, list):
        self.csapat = list[0]
        self.helyezes = int(list[1])
        self.valtozas = int(list[2])
        self.pontszam = int(list[3])

def makingObjects():
    list = []
    temp = importFromTXT()
    for i in range(1, len(temp), 1):
        list.append(Team(temp[i].split(";")))
    return list

def importFromTXT():
    f = open("fifa.txt", "r", encoding="UTF8").read()
    lines = f.split("\n")
    return lines

def formatVM(txt):
    temp = str(txt)[1:-1]
    temp = temp.replace("'", '')
    temp = temp.split(",")
    for i in temp:
        v = int(i.split(":")[0].strip())
        db =  int(i.split(":")[1].strip())
        if db > 1:
            print(f"\t{v} helyet változott: {db} csapat")

def feladat4(list):
    összes_pontszam = 0
    for i in list:
        összes_pontszam += i.pontszam
    return round(összes_pontszam/len(list), 2)  

def feladat5(list):
    max_index = 0
    for i in range(len(list)):
        if list[i].valtozas > list[max_index].valtozas:
            max_index = i
    print(f"\tHelyezés: {list[max_index].helyezes}\n\tCsapat: {list[max_index].csapat}\n\tCsapat: {list[max_index].pontszam}")

def feladat6(list):
    for i in list:
        if i.csapat == "Magyarország":
            return "van"
    return "nincs"

def feladat7(list):
    vmap = dict()
    for i in list:
        if i.valtozas in vmap:
            vmap[i.valtozas] += 1
        else:
            vmap[i.valtozas] = 1
    formatVM(vmap)

def main():
    main_list = makingObjects()
    print(f"3. feladat: A világranglistán {len(main_list)} csapat szerepel")
    print(f"4. feladat: A csapatok átlagos pontszáma: {feladat4(main_list)} pont")
    print(f"5. feladat: A legtöbbet javító csapat:")
    feladat5(main_list)
    print(f"6. feladat: A csapatok között {feladat6(main_list)} Magyarország")
    print(f"7. feladat: Statiszkia")
    feladat7(main_list)

main()