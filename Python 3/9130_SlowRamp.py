import time
import visa
rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])

print(vi.query("*idn?"))

vi.write("outp on")
vi.write("inst first")
for lev in range(100):
    cmd = "volt " + str(lev*0.005) + "V"
    #print(cmd)
    vi.write(cmd)
    time.sleep(1)
time.sleep(1)
vi.write("outp off")
