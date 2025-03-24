
class Thing:
    def __init__(self, I, W, P):
        self.I = I
        self.W = W
        self.P = P


class List:
    def __init__(self):
        self.Arr = []

    def Add(self, I, W, P):
        self.Arr.append(Thing(I, W, P))

    def Repay(self):
        return self.Arr

    def SearchM(self):
        return max((elem.P for elem in self.Arr), default=0)

    def Quantity(self):
        return len(self.Arr)

    def TotalWeight(self):
        return sum(elem.W for elem in self.Arr)

    def TotalProfit(self):
        return sum(elem.P for elem in self.Arr)


class Parameters:
    def __init__(self, Ep, WM, L):
        self.Ep = Ep
        self.WM = WM
        self.list = L


class Сounting:
    def __init__(self, property):
        self.property = property
        self.ChooseI = []
        self.SM = 0
        self.SP = 0

    def Alloow(self):
        Ep, WM, L = self.property.Ep, self.property.WM, self.property.list
        products = L.Repay()
        amount = L.Quantity()

        if amount == 0:
            return

        PM = L.SearchM()
        dimension = (1 if Ep == 0 else (Ep * PM) / (amount * (1 + Ep)))
        Scaled = [
            {"ScaledP": (p.P if Ep == 0 else p.P // dimension),
             "W": p.W,
             "PersonalID": p.I}
            for p in products
        ]

        table = {0: {"W": 0, "items": []}}

        for current in Scaled:
            current_entries = list(table.items())
            for c, data in current_entries:
                new_cost = c + current["ScaledP"]
                new_W = data["W"] + current["W"]

                if new_W > WM:
                    continue

                if new_cost not in table or table[new_cost]["W"] > new_W:
                    table[new_cost] = {
                        "W": new_W, "items": data["items"] + [current["PersonalID"]]}

        ScP = max(
            (k for k, v in table.items() if v["W"] <= WM), default=0)
        result = table[ScP]
        self.ChooseI = sorted(result["items"])
        self.SM = sum(products[idx - 1].W for idx in self.ChooseI)
        self.SP = sum(products[idx - 1].P for idx in self.ChooseI)

    def DetailedOutput(self):
        return {
            "Total Weight": self.SM,
            "Total Profit": self.SP,
            "Selected Items": self.ChooseI
        }

    def debug(self):
        return {
            "Total Items": self.list.Quantity(),
            "Total Weight": self.list.TotalWeight(),
            "Total Profit": self.list.TotalProfit()
        }

    def exit(self):
        return {
            "W": self.SM,
            "P": self.SP,
            "items": self.ChooseI
        }


class SolveChallenge:
    def __init__(self):
        self.Ep = 0
        self.WM = 0
        self.list = List()
        self.result = {"W": 0, "P": 0, "items": []}

    def СountingChallenge(self):
        property = Parameters(self.Ep, self.WM, self.list)
        Calkul = Сounting(property)
        Calkul.Alloow()
        self.result = Calkul.exit()

    def input(self, lines):
        self.Ep = float(lines[0])
        self.WM = int(lines[1])
        for idx, line in enumerate(lines[2:], start=1):
            W, P = map(int, line.split())
            self.list.Add(idx, W, P)

    def FormaEX(self):
        result = f"{self.result['W']} {self.result['P']
                                       }\n" + "\n".join(map(str, self.result["items"]))
        return result


def main():
    import sys
    lines = sys.stdin.read().strip().split("\n")
    processor = SolveChallenge()
    processor.input(lines)
    processor.СountingChallenge()
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'w') as outfile:
            outfile.write(processor.FormaEX() + "\n")
    else:
        print(processor.FormaEX())
# def Allow: Внешний цикл проходит по каждому элементу массива Scaled (количество элементов — n).Внутренний цикл зависит от максимального веса W => O(n*w)
# это самая ьольшая фйнкция по времени(все остальные затрачивают по времени O(n) по этому итоговая сложность будет
# :O(n*w)
# таблица table хранит вес w и так же есть arr котрый хранит n элементов поэтому общая сложность алгоритма по памяти ьудет O(n+w)


if __name__ == "__main__":
    main()
