from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    x=donuts.count(0)
    global_list = []
    print(f'default donuts = {donuts}')
    print(x)
    l=len(donuts)
    print(f'start = {donuts}')
    print(len(donuts))
    i=0
    while(i<l):
        print(f'lenght i = {i}')
        if donuts[i]==0:
            print(f'global list start = {global_list}')
            global_list.append(0)
            global_list.append(0)
            print(f' global list end = {global_list}')
            i+=1
        else:
            global_list.append(donuts[i])
            i+=1
    print(f'global list return {global_list}')
    donuts.clear()
    donuts = global_list
    print(donuts)
    return donuts
print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))
