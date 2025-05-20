def solve(self, A):
        list1 = []
        for i in A:
            if i not in list1:
                list1.append(i)

            list1.sort()
            