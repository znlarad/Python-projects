#This code reades the file of TIME'S 100 Persons of The Century and has a search engine to search names and jobs 
#This code is written by znl_arad



file=open("time.txt")
print("we have procced your file ")
search=input("search engine: ").lower()

found = False #defining found and setting it to false so we know when we have our results

while True:
    line=file.readline()#reading everyline
    if not line:
        break

    def proccess(line):
        if "," in line:
            x = line.strip().split(",")#deviding names and jobs by one specific character
            y = list(x)
            name=y[0]
            job=y[1]
            print("  name:  {}      job: {}".format(name,job))#giving results in the format of name and jobs

    for i,line in enumerate(file):
        if search in line.strip().lower():
            print("line",i+2)
            proccess(line)
            found = True 


    if not found:
        print("no result")
        file.close()
            

    































    if not line:
        break


















