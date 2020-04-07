from regular import Regular


regul = Regular()
regul.add(11, "asdasd", 10, 123, 2).add(1,2,3,4,1,2,3,1,4,4,1,2,"asd",3,4)

print(regul, '\n')
print('Element 3: ', regul[:4])

regul[:3] = 27
print('Element 3: ', regul[:4])
print('len: ', len(regul))

# regul[123]

regul.sort()
regul.delete(4)
print(regul)
regul.insert(2, "asd")
print(list(regul))
