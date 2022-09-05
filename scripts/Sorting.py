class MySorting:
    def __init__(self, arr: list) -> None:
        self.arr = arr

    def BubbleSort(self) -> list:
        l = self.arr
        for i in range(0, len(l) - 1):
            for j in range(i + 1, len(l)):
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]
        return l

    def BubbleSort1(self) -> list:
        l = self.arr
        swap = True
        while swap:
            swap = False

            for i in range(0, len(l) - 1):
                if l[i] > l[i + 1]:
                    swap = True
                    l[i], l[i + 1] = i[i + 1], l[i]

        return l


if __name__ == "__main__":
    l = [1, 9, 0, 2, 7, 5, 8, 3, 0, 3, 11, 5, 2, 8, 4]
    print(MySorting(l).BubbleSort())
    print(MySorting(l).BubbleSort1())
