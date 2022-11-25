#format convert to: user:pass@ip:port
fileout = open("FILE/PATH","w") #outfile
with open("FILE/PATH","r") as file: #read in file normal format of ip:port:user:pass
    for line in file:
        string = line.strip()
        result = string.split(':')
        newproxy = result[2] + ":" + result[3] + "@" + result[0] + ":" + result[1] + "\n"
        fileout.write(newproxy)
print("Completed.")
fileout.close()
file.close()
