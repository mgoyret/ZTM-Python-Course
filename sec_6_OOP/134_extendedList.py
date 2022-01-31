from typing import List


class SuperList(list):
    def __len__(self):
        return 1000

superList1 = SuperList();

superList1.append(4)
superList1.append(3)
superList1.append(34)
print(superList1)
print(len(superList1))
