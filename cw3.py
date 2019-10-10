#3
format1='{:^111}'.format('lubie')
print(format1)

format2='{:.8}'.format('placki')
print(format2)

from datetime import datetime
format3='{:%Y-%m-%d %H:%M}'.format(datetime(2019, 10, 10, 18, 25))
print(format3)

format4='{:=+5d}'.format(666)
print(format4)

format5='{:{prec}} = {:{prec}}'.format('AveSzatan', 6.666666666666666, prec='.5')
print(format5)


