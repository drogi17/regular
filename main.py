from regular import Regular


regul = Regular()
regul.add(11, "asdasd", 10, 123, 2)

print(regul, '\n')
print('Element 3: ', regul[3])

regul[3] = 27
print('Element 3: ', regul[3])
print('len: ', len(regul))

# regul[123]

regul.sort()
print(regul)
regul.delete(4)
print(regul)
regul.insert(2, "asd")
print(list(regul))
