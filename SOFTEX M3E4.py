x = 8 + 6j
y = complex(4, 2)
z= complex(2, 3)

s = (x + y) + z
sub = (x - y) - z
m = (x * y) * z
d = (x / y) / z

print('soma: ', s),
print('real: ', s.real, '\n inmaginário: ', s.imag, '\n')

print('subtração: ', sub)
print('real: ', sub.real, '\n imaginário', sub.imag, '\n')

print('multiplicação: ', m)
print('real: ', m.real, '\n imaginário: ', m.imag, '\n')

print('divisão: ', d)
print('real: ', d.real, '\n imaginário: ', d.imag)
