import os
import csv
import math

# folder name
folder = "temperatures"

# will hold everything
data = []

files = os.listdir(folder)
for f in files:
    if f.endswith(".csv"):
        with open(os.path.join(folder, f), "r") as file:
            rdr = csv.reader(file)
            head = next(rdr) # skip first line
            for row in rdr:
                data.append(row)

# months are columns 4 to 15
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# map month names to columns
month_col = {}
for i in range(len(months)):
    month_col[months[i]] = i+4

# =============== seasonal avg ===================
print("=== Seasonal Averages ===")

def calc_avg(monthlist):
    vals = []
    for r in data:
        for m in monthlist:
            v = r[month_col[m]]
            if v != "" and v.lower() != "nan":
                vals.append(float(v))
    s = 0.0
    for x in vals:
        s += x
    if len(vals) == 0:
        return 0
    return s/len(vals)

summer = calc_avg(["Dec","Jan","Feb"])
autumn = calc_avg(["Mar","Apr","May"])
winter = calc_avg(["Jun","Jul","Aug"])
spring = calc_avg(["Sep","Oct","Nov"])

print("Summer:", round(summer,1),"°C")
print("Autumn:", round(autumn,1),"°C")
print("Winter:", round(winter,1),"°C")
print("Spring:", round(spring,1),"°C")
print("")

# ============= largest temp range ================
print("=== Largest Temperature Range ===")

stationtemps = {}

for r in data:
    st = r[0]
    if st not in stationtemps:
        stationtemps[st] = []
    for c in range(4,16):
        val = r[c]
        if val != "" and val.lower()!="nan":
            stationtemps[st].append(float(val))

ranges = {}
for st in stationtemps:
    tlist = stationtemps[st]
    if len(tlist)>0:
        hi = max(tlist)
        lo = min(tlist)
        rng = hi-lo
        ranges[st] = (rng,hi,lo)

maxrng = -999
for s in ranges:
    if ranges[s][0]>maxrng:
        maxrng = ranges[s][0]

for s in ranges:
    if abs(ranges[s][0]-maxrng)<1e-9:
        print(s,": Range",round(ranges[s][0],1),"°C (Max:",round(ranges[s][1],1),"°C, Min:",round(ranges[s][2],1),"°C)")
print("")

# ============= temperature stability ==============
print("=== Temperature Stability ===")

stddevs = {}

for st in stationtemps:
    tlist = stationtemps[st]
    if len(tlist)>0:
        sm = 0
        for t in tlist:
            sm+=t
        avg = sm/len(tlist)
        var = 0
        for t in tlist:
            var += (t-avg)**2
        var = var/len(tlist)
        std = math.sqrt(var)
        stddevs[st]=std

minstd = 999999
maxstd = -1
for st in stddevs:
    if stddevs[st]<minstd:
        minstd = stddevs[st]
    if stddevs[st]>maxstd:
        maxstd = stddevs[st]

for st in stddevs:
    if abs(stddevs[st]-minstd)<1e-9:
        print("Most Stable:",st,": StdDev",round(stddevs[st],1),"°C")
for st in stddevs:
    if abs(stddevs[st]-maxstd)<1e-9:
        print("Most Variable:",st,": StdDev",round(stddevs[st],1),"°C")


