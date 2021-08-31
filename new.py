a = "[{'names': 'django'}, {'names': 'test'}, {'names': 'it was a last one'}]"
b = a.split("[")[1]
c = b.split("]")[0]
v = c.replace("'names': ", "")
g = v.replace("'}", "")
n = g.replace("{'", "")
j = n.replace(", ", "\n")
print(j)