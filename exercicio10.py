width = float(input('Largura da parede: '))
height = float(input('Altura da parede: '))
area = width*height # calcula a area
tinta = area/2  # calcula a quantidade de tinta para a parede
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.' .format(width, height, area))
print('Para pintar essa paredem você precisa de {}l de tinta.' .format(tinta))