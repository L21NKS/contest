import sys

class Authentication:
    def __init__(self):
        self.NTry = 0
        self.BedTimeM = 0
        self.PSpacing = 0
        self.Unix = 0
        self.Try = []  # O(n)
        self.CurrentUnix = 0
        self.BedTime = 0

    def ReadInput(self):
        # Считывание данных с stdin (и по времени и по памяти O(n)  для списка)
        evidence = sys.stdin.read().strip().split('\n')
        try:
            args = list(map(int, evidence[0].split()))
            self.NTry, self.PSpacing, self.BedTime, self.BedTimeM, self.Unix = args# O(n) памяти для хранения поппыток
        except ValueError:
            raise ValueError("Error")
        self.Try = []
        for line in evidence[1:]:
            try:
                self.Try.append(int(line))
            except ValueError:
                continue
        self.CurrentUnix = min(self.BedTime, self.BedTimeM)

    def EndBlock(self):
        # Основной алгоритм проверки блокировки (O(n) времени)
        if len(self.Try) < self.NTry:
            return None
        ending = 0
        index1 = 0
        CurrentUnix = self.CurrentUnix
        while index1 <= len(self.Try) - self.NTry:
            index2 = index1 + self.NTry - 1
            if self.Try[index2] - self.Try[index1] < self.PSpacing:
                block_end = self.Try[index2] + CurrentUnix
                if block_end > ending:
                    ending = block_end
                    # по памяти O(1)|
                    # <--------------
                    CurrentUnix = min(CurrentUnix * 2, self.BedTimeM)
                index1 = index2 + 1
            else:
                index1 += 1
        if ending <= self.Unix:
            return None
        return ending

    def Merge(self, arr):
        # Сортировка слиянием по времени(O(n log n) ,по памяти O(n) )
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.Merge(arr[:mid])
        right = self.Merge(arr[mid:])
        return self.MAlgorithm(left, right)

    def MAlgorithm(self, left, right):
        # Слияние двух отсортированных массивов и по времени и по памяти (O(n) )
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])# O(n)
        result.extend(right[j:])# O(n)
        return result

    def Filter(self):
        # Фильтр и сортировка попыток работает за  (O(n log n) времени, O(n) памяти)
        limit = self.Unix - 2 * self.BedTimeM
        # временя O(n) так как нужно пройтись по каждым значениям
        self.Try = [entrance for entrance in self.Try if entrance >= limit]
        self.Try = self.Merge(self.Try)# временя  O(n log n)

    def print_result(self, block_end):
        print("ok" if block_end is None else block_end)

    def Perform(self):
        # Итог: по времени O(n log n) по памяти O(n) )
        self.ReadInput()
        self.Filter()
        result = self.EndBlock()
        if len(sys.argv) > 1:
            with open(sys.argv[1], 'w') as outfile:
                outfile.write("ok\n" if result is None else f"{result}\n")
        else:
            self.print_result(result)


if __name__ == "__main__":
    blocker = Authentication()
    blocker.Perform()


