import math
import sys

class Memory:
    def __init__(self, size):
        self.size = size
        self.array = [0] * ((size + 7) // 8)

    def Space(self, position):
        if position < 0 or position >= self.size:
            return False
        index = position // 8
        bit = position % 8
        self.array[index] |= (1 << bit)
        return True

    def Clear(self):
        self.array = [0] * len(self.array)

    def Confirm(self, position):
        if position < 0 or position >= self.size:
            return False
        index = position // 8
        bit = position % 8
        return (self.array[index] & (1 << bit)) != 0

    def Conversion(self):
        bits = ""
        for i in range(self.size):
            byte_index = i // 8
            bit_index = i % 8
            bits += '1' if (self.array[byte_index] & (1 << bit_index)) else '0'
        return bits

    def SetBits(self):
        return sum(bin(byte).count('1') for byte in self.array)


class BloomFilter:
    def __init__(self, expected_units, false_prob):
        if expected_units <= 0 or false_prob <= 0 or false_prob >= 1:
            self.valid = False
            return

        self.quantity = expected_units
        self.probability = false_prob
        self.measure = round(-(self.quantity *
                             math.log(self.probability)) / (math.log(2) ** 2))
        self.HQ = round(-math.log(self.probability) / math.log(2))

        if self.measure < 1 or self.HQ < 1:
            self.valid = False
            return

        self.bits = Memory(self.measure)
        self.Primes = self.GenerateNumbersPRIME(self.HQ)
        self.mod = 2147483647
        self.valid = True

    def GenerateNumbersPRIME(self, count):
        primes = [2]
        candidate = 3

        while len(primes) < count:
            is_prime = True
            sqrt = math.sqrt(candidate)
            for prime in primes:
                if prime > sqrt:
                    break
                if candidate % prime == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(candidate)
            candidate += 2

        return primes

    def Get(self):
        if not self.valid:
            return ""
        return self.bits.Conversion()

    def Res(self):
        if self.valid:
            self.bits.Clear()

    def H(self, meaning):
        Hash = []
        for i in range(self.HQ):
            prime = self.Primes[i]
            HVall = (((i + 1) * meaning + prime) % self.mod) % self.measure
            Hash.append(HVall)
        return Hash

    def GetBit(self):
        if self.valid:
            return self.bits.SetBits()
        return 0

    def add(self, unit):
        if not self.valid:
            return False
        Hash = self.H(unit)
        for position in Hash:
            self.bits.Space(position)
        return True

    def Draw(self, unit):
        if not self.valid:
            return False
        Hash = self.H(unit)
        for position in Hash:
            if not self.bits.Confirm(position):
                return False
        return True


class Commands:
    def __init__(self):
        self.bloom = None
        self.output = []

    def Proc(self, lines):
        for line in lines:
            if not line.strip():
                continue

            parts = line.strip().split()
            command = parts[0]

            try:
                if command == "set":
                    if len(parts) != 3 or self.bloom is not None:
                        self.output.append("error")
                        continue
                    quantity = int(parts[1])
                    probability = float(parts[2])
                    new_bloom = BloomFilter(quantity, probability)
                    if not new_bloom.valid:
                        self.output.append("error")
                    else:
                        self.bloom = new_bloom
                        self.output.append(
                            f"{self.bloom.measure} {self.bloom.HQ}")

                elif command == "add":
                    if len(parts) != 2 or not self.bloom or not self.bloom.valid:
                        self.output.append("error")
                        continue
                    key = int(parts[1])
                    self.bloom.add(key)

                elif command == "search":
                    if len(parts) != 2 or not self.bloom or not self.bloom.valid:
                        self.output.append("error")
                        continue
                    search = int(parts[1])
                    search_result = self.bloom.Draw(search)
                    self.output.append("1" if search_result else "0")

                elif command == "print":
                    if len(parts) != 1 or not self.bloom or not self.bloom.valid:
                        self.output.append("error")
                        continue
                    bit_string = self.bloom.Get()
                    self.output.append(bit_string)

                elif command == "Res":
                    if len(parts) != 1 or not self.bloom or not self.bloom.valid:
                        self.output.append("error")
                        continue
                    self.bloom.Res()

                elif command == "count":
                    if len(parts) != 1 or not self.bloom or not self.bloom.valid:
                        self.output.append("error")
                        continue
                    count = self.bloom.GetBit()
                    self.output.append(str(count))

                else:
                    self.output.append("error")

            except Exception:
                self.output.append("error")

    def result(self):
        return "\n".join(self.output)


def Manual():
    input_data = sys.stdin.read()
    lines = input_data.split("\n")
    processor = Commands()
    processor.Proc(lines)
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'w') as outfile:
            outfile.write(processor.result() + "\n")
    else:
        print(processor.result())


if __name__ == "__main__":
    Manual()