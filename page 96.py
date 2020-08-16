#i used the given data which is slightly different than original data in wikipedia

#inserting data
bd_division_info = {}
bd_division_info["Barisal"] = {"district" : 6, "upazila" : 39, "union" : 333 }
bd_division_info["Chittagong"] = {"district" : 11, "upazila" : 97, "union" : 336 }
bd_division_info["Dhaka"] = {"district" : 13, "upazila" : 93, "union" : 1833 }
bd_division_info["Khulna"] = {"district" : 10, "upazila" : 59, "union" : 270 }
bd_division_info["Mymensingh"] = {"district" : 4, "upazila" : 34, "union" : 350 }
bd_division_info["Rajshahi"] = {"district" : 8, "upazila" : 70, "union" : 558 }
bd_division_info["Rangpur"] = {"district" : 8, "upazila" : 58, "union" : 536 }
bd_division_info["Shylet"] = {"district" : 4, "upazila" : 38, "union" : 334 }

#i hate writing a lot -_- 
Div = bd_division_info

#variables needed
dist = 0
upa = 0
uni = 0

#real magic happens here
for divisions in Div:
    dist += bd_division_info[divisions]['district']
for divisions in Div:
    upa += bd_division_info[divisions]['upazila']
for divisions in Div:
    uni += bd_division_info[divisions]['union']

#results
print("there are", dist, "districts in Bangladesh")
print("there are", upa, "upazilas in Bangladesh")
print("there are", uni, "unions in Bangladesh")
