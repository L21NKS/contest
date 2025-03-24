import sys

tag_size = False  
tag_error = False  

def set_size(N):
    global arr, head, tail, size, a, tag_size, tag_error
    if tag_error:  
        sys.stdout.write("error\n")
    elif tag_size:  
        sys.stdout.write("error\n")
    elif N < 0:  
        sys.stdout.write("error\n")
        tag_error = True  
    else:
        arr = [None] * N  
        head = 0
        tail = 0
        size = N
        a = 0  
        tag_size = True  

def print_d():
    if a == 0:
        sys.stdout.write("empty\n")
    else:
        if head < tail:
            sys.stdout.write(" ".join(arr[head:tail]) + "\n")
        else:
            sys.stdout.write(" ".join(arr[head:] + arr[:tail]) + "\n")

def pushf(x):
    global head, size, a
    if a == size:
        sys.stdout.write("overflow\n")
    else:
        head = (head - 1 + size) % size
        arr[head] = x
        a += 1

def pushb(x):
    global tail, size, a
    if a == size:
        sys.stdout.write("overflow\n")
    else:
        arr[tail] = x
        tail = (tail + 1) % size
        a += 1

def popf():
    global head, size, a
    if a == 0:
        sys.stdout.write("underflow\n")
    else:
        sys.stdout.write(f"{arr[head]}\n")
        arr[head] = None
        head = (head + 1) % size
        a -= 1

def popb():
    global tail, size, a
    if a == 0:
        sys.stdout.write("underflow\n")
    else:
        tail = (tail - 1 + size) % size
        sys.stdout.write(f"{arr[tail]}\n")
        arr[tail] = None
        a -= 1

deque_dict = {
    "set_size": set_size,
    "print": print_d,
    "pushb": pushb,
    "pushf": pushf,
    "popf": popf, 
    "popb": popb
}

def space(s):
    tokens = s.split()
    reconstructed = ' '.join(tokens)
    return s != reconstructed


input_data = sys.stdin.read().splitlines()

for line in input_data:
    line = line.rstrip('\n')
    if space(line):  
        sys.stdout.write("error\n")
        continue

    line = line.strip()
    if line:
        parts = line.split()
        command = parts[0]

        if tag_error:
            sys.stdout.write("error\n")
            continue

        if not tag_size and command != "set_size":
            sys.stdout.write("error\n")
            continue

        if command == "set_size":
            if len(parts) == 2:
                try:
                    deque_dict[command](int(parts[1]))
                except ValueError:
                    sys.stdout.write("error\n")
            else:
                sys.stdout.write("error\n")

        elif command in ["pushb", "pushf"]:
            if len(parts) != 2:
                sys.stdout.write("error\n")
                continue
            deque_dict[command](parts[1])

        elif command in ["popb", "popf", "print"]:
            if len(parts) != 1:
                sys.stdout.write("error\n")
                continue
            deque_dict[command]()

        else:
            sys.stdout.write("error\n")