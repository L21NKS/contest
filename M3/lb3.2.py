import sys


class BinaryMinHeap:
    def __init__(self):
        self.heap = []
        self.index_map = {}

    def _Parent(self, I):
        return (I - 1) // 2

    def _Left(self, I):
        return 2 * I + 1

    def _Right(self, I):
        return 2 * I + 2

    def _Swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.index_map[self.heap[i][0]] = i
        self.index_map[self.heap[j][0]] = j

    def _HeapifyU(self, I):
        while I > 0:
            parent = self._Parent(I)
            if self.heap[I][0] < self.heap[parent][0]:
                self._Swap(I, parent)
                I = parent
            else:
                break

    def _HeapifyD(self, I):
        size = len(self.heap)
        while True:
            left, right = self._Left(I), self._Right(I)
            smallest = I

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest != I:
                self._Swap(I, smallest)
                I = smallest
            else:
                break

    def set(self, K, V):
        if K in self.index_map:
            index = self.index_map[K]
            self.heap[index] = (K, V)
            self._HeapifyU(index)
            self._HeapifyD(index)
        else:
            return "error"

    def add(self, K, V):
        if K in self.index_map:
            return "error"
        self.heap.append((K, V))
        self.index_map[K] = len(self.heap) - 1
        self._HeapifyU(len(self.heap) - 1)

    def search(self, K):
        if K in self.index_map:
            index = self.index_map[K]
            return (1, index, self.heap[index][1])
        return "0"

    def delete(self, K):
        if K in self.index_map:
            index = self.index_map[K]
            last_index = len(self.heap) - 1
            if index != last_index:
                self._Swap(index, last_index)
            self.heap.pop()
            del self.index_map[K]
            if index < len(self.heap):
                self._HeapifyU(index)
                self._HeapifyD(index)
        else:
            return "error"

    def min(self):
        if not self.heap:
            return "error"
        K, V = self.heap[0]
        return (K, 0, V)

    def max(self):
        if not self.heap:
            return "error"
        max_element = max(self.heap, key=lambda x: x[0])
        index = self.heap.index(max_element)
        return (max_element[0], index, max_element[1])

    def extract(self):
        if not self.heap:
            return "error"
        K, V = self.heap[0]
        self.delete(K)
        return (K, V)

    def print(self):
        if not self.heap:
            return "_"
        levels = []
        size = len(self.heap)
        level = 0
        while (1 << level) - 1 < size:
            level += 1
        full_tree = []
        for i in range(1 << level):
            if i < size:
                full_tree.append(self.heap[i])
            else:
                full_tree.append(None)

        index = 0
        for i in range(level):
            start, end = (1 << i) - 1, (1 << (i + 1)) - 1
            line = []
            for j in range(start, end):
                if j < len(full_tree):
                    if full_tree[j] is not None:
                        K, V = full_tree[j]
                        if j == 0:
                            line.append(f"[{K} {V}]")
                        else:
                            ParentK = full_tree[self._Parent(
                                j)][0] if full_tree[self._Parent(j)] is not None else "_"
                            line.append(f"[{K} {V} {ParentK}]")
                    else:
                        line.append("_")
            levels.append(" ".join(line))
        return "\n".join(levels)


def main(input_lines, output_file=None):
    heap = BinaryMinHeap()
    output = []

    for line in input_lines:
        if not line.strip():
            continue

        parts = line.split()
        command = parts[0]

        try:
            if command == "add":
                K, V = int(parts[1]), parts[2]
                res = heap.add(K, V)
                if res == "error":
                    output.append(res)
            elif command == "set":
                K, V = int(parts[1]), parts[2]
                res = heap.set(K, V)
                if res == "error":
                    output.append(res)
            elif command == "delete":
                K = int(parts[1])
                res = heap.delete(K)
                if res == "error":
                    output.append(res)
            elif command == "search":
                K = int(parts[1])
                res = heap.search(K)
                if res == "0":
                    output.append("0")
                else:
                    output.append(f"{res[0]} {res[1]} {res[2]}")
            elif command == "min":
                res = heap.min()
                if res == "error":
                    output.append("error")
                else:
                    output.append(f"{res[0]} {res[1]} {res[2]}")
            elif command == "max":
                res = heap.max()
                if res == "error":
                    output.append("error")
                else:
                    output.append(f"{res[0]} {res[1]} {res[2]}")
            elif command == "extract":
                res = heap.extract()
                if res == "error":
                    output.append("error")
                else:
                    output.append(f"{res[0]} {res[1]}")
            elif command == "print":
                output.append(heap.print())
            else:
                output.append("error")
        except Exception:
            output.append("error")

    results = [str(result) if not isinstance(result, str)
               else result for result in output]

    if output_file:
        with open(output_file, "w") as f:
            f.write("\n".join(results) + "\n")
    else:
        sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    input_lines = sys.stdin.readlines()
    main(input_lines)
