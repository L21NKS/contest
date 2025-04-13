from collections import deque


class Bunch:
    def __init__(self, K, V, Left=None, Right=None, Parant=None):
        self.Left = Left
        self.Right = Right
        self.Parant = Parant
        self.K = K
        self.V = V


class Tree:
    def __init__(self):
        self.root = None

    def RotateR(self, bunch):
        bunch.Parant.Left = bunch.Right
        if bunch.Right is not None:
            bunch.Right.Parant = bunch.Parant
        bunch.Right = bunch.Parant
        if bunch.Right.Parant is not None:
            if bunch.Right.Parant.Left == bunch.Right:
                bunch.Right.Parant.Left = bunch
            else:
                bunch.Right.Parant.Right = bunch
        bunch.Parant = bunch.Right.Parant
        bunch.Right.Parant = bunch
        return bunch

    def RotateL(self, bunch):
        bunch.Parant.Right = bunch.Left
        if bunch.Left is not None:
            bunch.Left.Parant = bunch.Parant
        bunch.Left = bunch.Parant
        if bunch.Left.Parant is not None:
            if bunch.Left.Parant.Left == bunch.Left:
                bunch.Left.Parant.Left = bunch
            else:
                bunch.Left.Parant.Right = bunch
        bunch.Parant = bunch.Left.Parant
        bunch.Left.Parant = bunch
        return bunch

    def Splay(self, bunch):
        while bunch.Parant is not None:

            if bunch.Parant.Parant is None:
                if bunch == bunch.Parant.Left:
                    bunch = self.RotateR(bunch)
                else:
                    bunch = self.RotateL(bunch)

            elif bunch == bunch.Parant.Left and bunch.Parant == bunch.Parant.Parant.Left:
                bunch.Parant = self.RotateR(bunch.Parant)
                bunch = self.RotateR(bunch)

            elif bunch == bunch.Parant.Right and bunch.Parant == bunch.Parant.Parant.Right:
                bunch.Parant = self.RotateL(bunch.Parant)
                bunch = self.RotateL(bunch)

            elif bunch == bunch.Parant.Right and bunch.Parant == bunch.Parant.Parant.Left:
                bunch = self.RotateL(bunch)
                bunch = self.RotateR(bunch)

            else:
                bunch = self.RotateR(bunch)
                bunch = self.RotateL(bunch)

        if bunch.Parant is None:
            self.root = bunch

    def set(self, K, V):
        if self.root is None:
            raise Exception('error')
        desired_vertice = self.search(K)
        if desired_vertice is not None:
            desired_vertice.V = V
        else:
            raise Exception('error')

    def add(self, K, V):
        x = Bunch(K, V)
        the_root = self.root
        Parant = None

        if self.root is None:
            self.root = x
            return

        while the_root is not None:
            Parant = the_root
            if K > the_root.K:
                the_root = the_root.Right
            elif K < the_root.K:
                the_root = the_root.Left
            else:
                if self.search(K) is not None:
                    raise Exception('error')

        if x.K > Parant.K:
            Parant.Right = x
        else:
            Parant.Left = x

        x.Parant = Parant
        self.Splay(x)

    def search(self, K):  # В конце Splay()
        if self.root is None:
            return None
        else:
            x = self.root
            x_par = None
            while x is not None:
                x_par = x
                if x.K == K:
                    self.Splay(x)
                    return x
                else:
                    if K < x.K:
                        x = x.Left
                    else:
                        x = x.Right
            self.Splay(x_par)
            return None

    def delete(self, K):  # И тут в конце Splay()
        if self.root is None:
            raise Exception('error')
        if self.search(K) is not None:
            if self.root.Left is None and self.root.Right is None:
                self.root = None

            elif self.root.Left is not None and self.root.Right is None:
                self.root.Left.Parant = None
                self.root = self.root.Left

            elif self.root.Left is None and self.root.Right is not None:
                self.root.Right.Parant = None
                self.root = self.root.Right

            else:
                self.MM(self.root.Left, "max")
                self.root.Right.Parant = None
                self.root.Right = self.root.Right.Right
                self.root.Right.Parant = self.root
        else:
            raise Exception('error')

    def MM(self, x, command):
        if self.root is None:
            raise Exception('error')
        else:
            if command == "min":
                while x.Left is not None:
                    x = x.Left
            else:
                while x.Right is not None:
                    x = x.Right
            self.Splay(x)
            return x

    def Valid(Input):
        return Input.isalnum()


def PrintT(tree):
    if tree.root:
        queue = deque()
        queue.append(tree.root)
        while queue:
            next_lvl = False
            out = ''
            NewQ = deque()
            for i in queue:
                if isinstance(i, int):
                    if len(NewQ) > 0:
                        if isinstance(NewQ[-1], int):
                            out += '_ ' * i
                            NewQ[-1] += 2 * i
                        else:
                            NewQ.append(0)
                            out += '_ ' * i
                            NewQ[-1] += 2 * i
                    else:
                        NewQ.append(0)
                        out += '_ ' * i
                        NewQ[-1] += 2 * i
                else:
                    next_lvl = True
                    if i.Parant is None:
                        out += '[' + str(i.K) + ' ' + i.V + '] '
                    else:
                        out += '[' + str(i.K) + ' ' + i.V + \
                            ' ' + str(i.Parant.K) + '] '
                    if i.Left is not None:
                        NewQ.append(i.Left)
                    else:
                        if len(NewQ) > 0:
                            if isinstance(NewQ[-1], int):
                                NewQ[-1] += 1
                            else:
                                NewQ.append(1)
                        else:
                            NewQ.append(1)
                    if i.Right is not None:
                        NewQ.append(i.Right)
                    else:
                        if len(NewQ) > 0:
                            if isinstance(NewQ[-1], int):
                                NewQ[-1] += 1
                            else:
                                NewQ.append(1)

            queue = NewQ
            if not next_lvl:
                break
            else:
                print(out[0:-1])


if __name__ == '__main__':
    tree = Tree()

    while True:
        try:
            line = input()
            if not line.strip():
                print("error")
                continue
            if line:
                parts = line.split(" ")
                command = parts[0]
                try:
                    if command == "add" and len(parts) == 3:
                        tree.add(int(parts[1]), parts[2])

                    elif command == "set" and len(parts) == 3:
                        tree.set(int(parts[1]), parts[2])

                    elif command == "delete" and len(parts) == 2:
                        tree.delete(int(parts[1]))

                    elif command == "search" and len(parts) == 2:
                        desired_vertice = tree.search(int(parts[1]))
                        if desired_vertice is not None:
                            print('1' + ' ' + desired_vertice.V)
                        else:
                            print('0')

                    elif command in ["min", "max"] and len(parts) == 1:
                        try:
                            print(tree.MM(tree.root, command).K,
                                tree.MM(tree.root, command).V)
                        except:
                            raise Exception('error')
                    elif command == "print" and len(parts) == 1:
                        if tree.root is None:
                            print('_')
                            continue
                        PrintT(tree)

                    else:
                        raise Exception('error')
                except Exception as some_error:
                    print(some_error)

        except EOFError:
            break
