

raw = []

def get_pr(data, pr):
    return data[int(len(data) * (pr / 100))]

compensate = 0.65
f = open("rise_percent.txt", "r")
for line in f.readlines():
    raw.append(float(line) - compensate)
f.close()

raw.sort()
#print(raw)
minus_sigma_2 = get_pr(raw, 2)
minus_sigma_1 = get_pr(raw, 16)
mean = get_pr(raw, 50)
plus_sigma_1 = get_pr(raw, 84)
plus_sigma_2 = get_pr(raw, 98)
print(minus_sigma_2)
print(minus_sigma_1)
print(mean)
print(plus_sigma_1)
print(plus_sigma_2)

# we need is (sigma_1 - mean)

