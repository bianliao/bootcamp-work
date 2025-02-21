# 可迭代資料（Iterable）：字串、列表、集合、字典

# for loop ============================================================
#list
for x in [3,5,2]: 
    print("list:", x)

#string
for y in "Amy":
    print("string:", y)

#set
for z in {"a", "text", 4, 34}:
    print("set:", z)

#dict-key
for key in {"A":3, "B":4}:
    print("dict-key:", key)

#dict-value
dic={"A":3, "B":4}
for key in dic:
    print("dict-key:", key)
    print("dict-value:", dic[key])

# built-in function ============================================================
# max(iterable)
max_li=[10,3,43,12]
result2_li = max(max_li)
print("max_li:", result2_li)

max_string="amazon"
result2_string = max(max_string)
print("max_string:", result2_string)

max_set={6, 344, 4, 34}
result2_set = max(max_set)
print("max_set:", result2_set)

max_dic={"A":3, "B":4, "Z":23}
result2_dic = max(max_dic)
print("max_dic_key:", result2_dic)


# sorted(iterable)
sorted_li=[10,3,43,12]
result2_li = sorted(sorted_li)
print("sorted_li:", result2_li)

sorted_string="amazon"
result2_string = sorted(sorted_string)
print("sorted_string:", result2_string)

sorted_set={6, 344, 4, 34}
result2_set = sorted(sorted_set)
print("sorted_set:", result2_set)

sorted_dic={"A":3, "B":4, "Z":23}
result2_dic = sorted(sorted_dic)
print("sorted_dic_key:", result2_dic)