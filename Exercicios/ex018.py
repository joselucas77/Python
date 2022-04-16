from multiprocessing.spawn import import_main_path


import math
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo {:.2f} tem:\nseno:{:.2f}\ncoseno:{:.2f}\ntangente:{:.2f}'.format(an,sen,cos,tan))