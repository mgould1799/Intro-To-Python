def hourly(infileN, outfileN):
    infile = open(infileN, "r")
    outfile = open(outfileN, "w")

    for line in infile:
        lineSplit = line.split("\n")
        for elements in lineSplit:
            elSplit = elements.split()
            print(elSplit)


hourly("infile.txt", "outfile.txt")
    
