# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""
import string


f = open("input.txt", "r")


class passport:
    def __init__(self):
        self.fields = dict()

    def check_valid(self):

        if len(self.fields) == 8 or (len(self.fields)==7 and "cid" not in self.fields):

            if int(self.fields["byr"]) < 1920 or int(self.fields["byr"]) > 2002:
                return 1,0

            if int(self.fields["iyr"]) < 2010 or int(self.fields["iyr"]) > 2020:

                return 1,0
            if int(self.fields["eyr"]) < 2020 or int(self.fields["eyr"]) > 2030:

                return 1,0

            units = self.fields["hgt"][-2:]
            hgt = self.fields["hgt"][:-2]
            if units != "cm" and units != "in":
                return 1,0
            if units == "cm":
                if int(hgt) < 150 or int(hgt) > 193:

                    return 1,0
            elif units == "in":
                if int(hgt) < 59 or int(hgt) > 76:
                    return 1,0


            if self.fields["hcl"][0] != "#"  or not all(c in string.hexdigits for c in self.fields["hcl"][1:]) or len(self.fields["hcl"]) != 7:
                return 1,0

            if self.fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return 1,0

            if self.fields["pid"].isnumeric() and len(self.fields["pid"])  == 9:

                return 1,1
        return 0,0


holder = passport()
ans1 = 0
ans2 = 0

for line in f:
    data = line[:-1]
    if data:
        fields = data.split(" ")
        for entry in fields:
            field_id, field_val = entry.split(":")
            holder.fields[field_id] = field_val


    elif not data:
        ans = holder.check_valid()
        ans1 += ans[0]
        ans2 += ans[1]
        holder = passport()
print(ans1,ans2)


