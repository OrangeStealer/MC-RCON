import aiomcrcon
from aiomcrcon import Client
import asyncio
import time
ServerPass = ""
ServerPort = 
ServerTSNIP = ""
ServerIP = ""

async def Init(IP,Port,Pass,CMD):
    client = Client(IP,Port,Pass)
    try:
        await client.connect()
    except aiomcrcon.errors.RCONConnectionError:
        return "RCON CONNECT ERROR"
    except aiomcrcon.IncorrectPasswordError:
        return "INCORRECT PASSWORD"
    
    
    if CMD != "":
        response = await client.send_cmd(CMD)
        return response
    
    await client.close()

#asyncio.run(Init(ServerTSNIP,ServerPort,ServerPass,"list"))

def ServerCheck():
    if ServerTSNIP != "":
        print("Attempting Connection Via Tailscale Network...")
        print("IP: " + str(ServerTSNIP) + ", Port: " + str(ServerPort))
        status = asyncio.run(Init(ServerTSNIP,ServerPort,ServerPass,""))
        if (status != "INCORRECT PASSWORD" or status != "INCORRECT PASSWORD"):
            time.sleep(2)
            print("Connected Via Tailscale Network.")
            #print("IP: " + str(ServerTSNIP) + ", Port: " + str(ServerPort))
    elif ServerIP != "":
        print("Attempting Connection Via Public Network...")
        print("IP: " + str(ServerIP) + ", Port: " + str(ServerPort))
        status = asyncio.run(Init(ServerIP,ServerPort,ServerPass,""))
        if (status != "INCORRECT PASSWORD" or status != "INCORRECT PASSWORD"):
            time.sleep(2)
            print("Connected Via Public Network.")
            #print("IP: " + ServerIP + ", Port: " + ServerPort)
    else:
        print("No IP Found.")
    
    if status == "RCON CONNECT ERROR":
        print("Incorrect RCON Information. Check IP and Connection Status.")
        return "WRONG IP"
    elif status == "INCORRECT PASSWORD":
        print("Incorrect RCON Password. Check Capitals and Spelling.")
        return "WRONG PASS"
    else:
        return True
           
status = ServerCheck()

def CommandTick(Command):
    global status 
    if status == "WRONG IP":
        exit("I-R-IP")
    elif status == "WRONG PASS":
        exit("I-R-PW")
    if (status == True and ServerTSNIP != ""):
        response = asyncio.run(Init(ServerTSNIP,ServerPort,ServerPass,Command))
        if response == None:
            print("No Response...")
        else:
            print("Server: " + str(response))
    elif (status == True and ServerIP != ""):
        response = asyncio.run(Init(ServerIP,ServerPort,ServerPass,Command))
        if response == None:
            print("No Response...")
        else:
            print("Server: " + str(response))
    
while True:
    CommandTick(input())