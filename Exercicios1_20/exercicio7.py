metragem = float(input('Digite um valor: '))
cm = metragem * 100 
mm = metragem * 1000
km = metragem / 1000
hm = metragem / 100
dam = metragem / 10
dm = metragem * 10

print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm\n' .format(metragem, km, hm, dam, dm, cm, mm))