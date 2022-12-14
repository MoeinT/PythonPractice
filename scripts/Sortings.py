class MySorting:
    def __init__(self, arr: list) -> None:
        self.arr = arr

    def BubbleSort1(self) -> list:
        l = self.arr
        for i in range(0, len(l) - 1):
            for j in range(i + 1, len(l)):
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]
        return l

    def BubbleSort(self) -> list:
        l = self.arr
        swap = True
        while swap:
            swap = False

            for i in range(0, len(l) - 1):
                if l[i] > l[i + 1]:
                    swap = True
                    l[i], l[i + 1] = l[i + 1], l[i]
        return l

    def SelectionSort(self) -> list:
        l = self.arr
        index = 0
        swap = True
        while swap:
            swap = False
            for i in range(index, len(l)):
                if l[i] < l[index]:
                    swap = True
                    l[i], l[index] = l[index], l[i]
            index += 1

        return l

    def InsertionSort(self) -> list:
        l = self.arr
        swap = True
        while swap:
            swap = False
            for i in range(1, len(l)):
                if l[i] < l[i - 1]:
                    swap = True
                    l[i], l[i - 1] = l[i - 1], l[i]
        return l


# Divide and conquer:
# Breaks the problem into two or more sub-problems of the same type
# In lon(n), n refers to the size of the problem
# and the result refers to the number of times we need to break the problem in half
# algorithms that follow the log(n) pattern are the best ones in terms of performance.

if __name__ == "__main__":
    l = [1, 9, 0, 2, 7, 5, 8, 3, 0, 3, 11, 5, 2, 8, 4]
    print(MySorting(l).BubbleSort())
    print(MySorting(l).SelectionSort())
    print(MySorting(l).InsertionSort())
