from collections import deque


class Bunch:
    def __init__(self, K, V, LeftKid=None, RightKid=None, Parent=None):
        self.K = K
        self.V = V
        self.LeftKid = LeftKid
        self.RightKid = RightKid
        self.Parent = Parent


class Tree:
    def __init__(self):
        self.tree_root = None
        self.Nodes_dict = {}

    def add(self, K, V):
        if K in self.Nodes_dict:
            raise Exception('error')
        if self.tree_root is None:
            self.tree_root = Bunch(K, V)
            self.Nodes_dict[K] = self.tree_root
        else:
            x = self.tree_root
            while x is not None:
                x_par = x
                if K > x.K:
                    x = x.RightKid
                elif K < x.K:
                    x = x.LeftKid
                else:
                    raise Exception('error')

            new_vertice = Bunch(K, V, Parent=x_par)
            self.Nodes_dict[K] = new_vertice
            if K > x_par.K:
                x_par.RightKid = new_vertice
            else:
                x_par.LeftKid = new_vertice

    def search(self, K, x=None):
        return self.Nodes_dict.get(K, None)

    def set(self, K, V):
        desired_vertice = self.search(K)
        if desired_vertice is not None:
            desired_vertice.V = V
        else:
            raise Exception('error')

    def minmax(self, command):
        x = self.tree_root
        if x is None:
            raise Exception('error')

        if command == "min":
            while x.LeftKid is not None:
                x = x.LeftKid
        else:
            while x.RightKid is not None:
                x = x.RightKid
        return x

    def delete(self, K):
        desired_vertice = self.search(K)
        if desired_vertice is None:
            raise Exception('error')

        del self.Nodes_dict[K]

        Right = desired_vertice.RightKid
        Left = desired_vertice.LeftKid

        if Left is None and Right is None:
            if desired_vertice == self.tree_root:
                self.tree_root = None
            elif desired_vertice == desired_vertice.Parent.LeftKid:
                desired_vertice.Parent.LeftKid = None
            else:
                desired_vertice.Parent.RightKid = None

        elif Left is not None and Right is None:
            if desired_vertice == self.tree_root:
                self.tree_root = Left
            elif desired_vertice == desired_vertice.Parent.LeftKid:
                desired_vertice.Parent.LeftKid = Left
            else:
                desired_vertice.Parent.RightKid = Left
            Left.Parent = desired_vertice.Parent

        elif Left is None and Right is not None:
            if desired_vertice == self.tree_root:
                self.tree_root = Right
            elif desired_vertice == desired_vertice.Parent.LeftKid:
                desired_vertice.Parent.LeftKid = Right
            else:
                desired_vertice.Parent.RightKid = Right
            Right.Parent = desired_vertice.Parent

        else:
            x = Left
            while x.RightKid is not None:
                x = x.RightKid
            desired_vertice.K = x.K
            desired_vertice.V = x.V
            self.Nodes_dict[desired_vertice.K] = desired_vertice

            if x.LeftKid is None:
                if x.Parent.LeftKid == x:
                    x.Parent.LeftKid = None
                else:
                    x.Parent.RightKid = None
            else:
                if x.Parent == desired_vertice:
                    desired_vertice.LeftKid = x.LeftKid
                else:
                    x.Parent.RightKid = x.LeftKid
                x.LeftKid.Parent = x.Parent

    def printing(self, cur_queue=None, out=''):

        if cur_queue is None:
            cur_queue = deque()
            cur_queue.append(self.tree_root)

        NQ = deque()
        cur_lvl = ''
        is_next = False

        while len(cur_queue) != 0:
            x = cur_queue.popleft()
            if x == '_':
                NQ.append('_')
                NQ.append('_')
                cur_lvl += '_ '
                continue
            else:
                if x.Parent is not None:
                    cur_lvl += '[' + str(x.K) + ' ' + \
                        str(x.V) + ' ' + str(x.Parent.K) + '] '
                else:
                    cur_lvl += '[' + str(x.K) + ' ' + str(x.V) + '] '
            if x.LeftKid is not None:
                is_next = True
                NQ.append(x.LeftKid)
            else:
                NQ.append('_')
            if x.RightKid is not None:
                is_next = True
                NQ.append(x.RightKid)
            else:
                NQ.append('_')

        out += cur_lvl[:-1]
        if not is_next:
            return out
        out += '\n'
        return self.printing(NQ, out)


if __name__ == '__main__':
    tree = Tree()

    while True:
        try:
            line = input()
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
                    elif command in ["min", "max"] and len(parts) == 1:
                        result = tree.minmax(command)
                        print(result.K, result.V)
                    elif command == "search" and len(parts) == 2:
                        result = tree.search(int(parts[1]))
                        print(f"1 {result.V}" if result else "0")
                    elif command == "print" and len(parts) == 1:
                        print(tree.printing() if tree.tree_root else '_')
                    else:
                        raise Exception('error')
                except Exception as e:
                    print(e)
        except EOFError:
            break
