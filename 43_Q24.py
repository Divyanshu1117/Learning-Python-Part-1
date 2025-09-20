# s = {20, 20.0, "20"}
s = set()
s.add(20)
s.add(20.0) # 20 (int) and 20.0 (float) are considered equal in Python sets, so only one will be stored
s.add("20")
print(s)
print(len(s))