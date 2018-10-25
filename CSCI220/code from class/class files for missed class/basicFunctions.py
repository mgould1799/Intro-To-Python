#Input: name
#Output: prints the banana song to the monitor
def bananaSong():
    name = "Katie"
    nameEnd = name[1:].lower()
    print(name + ", " + name + ", " + "bo-b" + nameEnd)
    print("Bananan-fana fo-f" + nameEnd)
    print("Fee-fy-mo-m" + nameEnd)
    print(name + "!")
    
def main():

    bananaSong()

main()
