import time

lst = []
st = set()

for i in range(10**6):
    lst.append(i)
    st.add(i)

# Measure list lookup
start = time.time()
if 10**5 in lst:
    print("Found in list")
print("List check took:", time.time() - start, "seconds")

# Measure set lookup
start = time.time()
if 10**5 in st:
    print("Found in set")
print("Set check took:", time.time() - start, "seconds")










