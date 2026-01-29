
# "messy" string:
raw_data = " nAmE, AgE, LoCaTiOn, PhOnE_nUmBeR "
new_data = raw_data.strip().lower().split(", ")
cap_data = []
for data in new_data:
    cap_data.append(data.capitalize().replace("_"," "))
print(cap_data)
