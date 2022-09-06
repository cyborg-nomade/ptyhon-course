"""testing data structures"""

simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
print(simple_list)
del simple_list[0]
print(simple_list)

d = {"name": "Max"}
print(d.items())
for k, v in d.items():
    print(k, v)
del d["name"]
print(d)

t = (1, 2, 3)
print(t.index(1))


s = {"Max", "Anna", "Max"}
print(s)
