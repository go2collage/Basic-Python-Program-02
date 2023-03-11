# Basic Python Program

# bits => MB, GB, TB

bits = float(input("Enter bits: "))
print("Bits converted into: ")

mb = bits * 125 * (10**-9)      # bits => mb formula
gb = bits * 125 * (10**-11)    # bits => gb
tb = bits * 125 * (10**-13)     # bits => tb

print("Megabytes: ", mb)
print("Gigabytes: ", gb)
print("Terabytes: ", tb)
