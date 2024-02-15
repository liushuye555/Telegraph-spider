
def log(urls,url,dirname,data):
    with open("log",'a') as f:
        f.writelines(url+"  |   "+dirname +"\n")
    i=0
    file = str(data.content)
    for z in urls:
        i+=1
        name = str(i) + ".jpg"
        #print(name)
        #print(z)
        file = file.replace(z, name)


    #print(file)
    with open(dirname + '/' + dirname + '.html',"w") as f:
        f.write(file)