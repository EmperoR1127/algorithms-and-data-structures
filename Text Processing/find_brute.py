def find_brute(t, p):
    """Return the lowest index of T at which substring P begins (or else -1)"""
    if len(t) > len(p):
        for i in range(len(t) - len(p) + 1):
            if t[i:i + len(p)] == p:
                return i
    return -1

if __name__ == "__main__":
    print(find_brute("abacaabaccabacabaabb","abacab"))




























    
