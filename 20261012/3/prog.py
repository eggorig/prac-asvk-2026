s, s1 = input(), ''
a = [s]
while s1 != s:
    s1 = input()
    a.append(s1)
height, width = len(a), len(a[0])
gas = sum(row.count('.') for row in a[1:-1])
water = sum(row.count('~') for row in a[1:-1])

height1, width1 = width, height
water_slide = (water + (width1 - 2) - 1) // (width1 - 2) if width1 - 2 else 0
gas_slide = height1 - 2 - water_slide

print('#' * width1)
for _ in range(gas_slide):
    print(f"#{'.' * (width1 - 2)}#")
for _ in range(water_slide):
    print(f"#{'~' * (width1 - 2)}#")
print('#' * width1)


max_val = max(gas, water)
gas_len = round(gas / max_val * 20) if max_val else 0
water_len = round(water / max_val * 20) if max_val else 0
d_gas = f'{gas}/{gas + water}'
d_water = f'{water}/{gas + water}' 
max_d = max(len(d_gas), len(d_water))


print(f"{'.' * gas_len:<20} {d_gas:>{max_d}}")
print(f"{'~' * water_len:<20} {d_water:>{max_d}}")
