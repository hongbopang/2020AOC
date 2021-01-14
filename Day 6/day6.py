# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:35:22 2020

@author: hongb
"""


f = open("input.txt", "r")

responses = set()
all_responses = set()
newflag = True

ans = 0
all_ans = 0
for line in f:

    line=line.strip("\n")

    if line:
        new_all = set()

        if newflag:
            newflag = False

            for char in line:
                all_responses.add(char)

        for char in line:
            responses.add(char)
            if char in all_responses:
                new_all.add(char)
         all_responses = new_all
    else:
        ans += len(responses)
        responses = set()
        all_ans += len(all_responses)
        all_responses = set()
        newflag = True

print(ans+len(responses))
print(all_ans+len(all_responses))
