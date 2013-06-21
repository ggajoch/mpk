import re
import fileinput



def changeLoop(R, G):
    kol = "%02x%02x" % (R, G)
    global part
    global file
    tmp = part
    tmp = re.sub("fill:((#[0-9a-f]{6})|none)","fill:#" + kol + "00",tmp)
    file = re.sub(part,tmp,file)
#    print("\n-------------------\n" + part + "\n\n" + tmp + "\n-----------------------\n")


def nothingLoop():
    global part
    global file
    tmp = part
    tmp = re.sub("fill:","fill-opacity:0;fill:",tmp)
    file = re.sub(part,tmp,file)



def changeStroke(R, G, width):
    kol = "%02x%02x" % (R, G)
 #   print(kol)

    global part
    global file
    #print(part)
    tmp = part
    tmp = re.sub("stroke:#[0-9a-f]{6}","stroke:#" + kol + "00",tmp)
    tmp = re.sub("stroke-width:[0-9]{0,3};","stroke-width:" + str(width) + ";",tmp)
    #print(tmp)
    file = re.sub(part,tmp,file)





def strokeOpacity():
    kol = "%02x%02x" % (R, G)
 #   print(kol)

    global part
    global file
    #print(part)
    tmp = part
    tmp = re.sub("strokeOpacity:[\S]{0,10};","stroke:0;",tmp)
    #print(tmp)
    file = re.sub(part,tmp,file)


file = open('map.svg','r');
file = file.read()



def changeIt(No):
    global part    
    res = 0
    now = 10
    while res == 0:
        reg = re.compile("id=\"" + str(No) + "\"[^>]*?style[\s\S]*?/>|style=[\s\S]{1," + str(now)+ "}?id=\"" + str(No)+"\"")
        tmp = reg.findall(file)
        if len(tmp) > 0:
            res = 1
            part = tmp[0]
        if now > 5000:
            part = ""
            break;
        now += 10

#    print(part)


for line in fileinput.input():
    inp = line.split()
    
    No = str(inp[0])
    changeIt(No)

    if No[len(No)-1] == 'p':
        if int(inp[1]) == -1:
            nothingLoop()
        else:
            changeLoop(int(inp[1]),int(inp[2]));


    else:    
        R = int(inp[1])
        if R == -1:
            strokeOpacity()

        else:
            G = int(inp[2])
            W = float(inp[3])
        
            changeStroke(R,G,W)

print(file)
