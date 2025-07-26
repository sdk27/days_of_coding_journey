class Heap:
    def __init__(self):
        self.ar = ["None"]

    def insert(self, key):

        if self.ar == ["None"]:
            self.ar.append(key)
            print("array is ", self.ar)
            return

        self.ar.append(key)
        l = len(self.ar) - 1
        key_index = l
        parent_index = l // 2

        while parent_index > 0:
            if self.ar[parent_index] < self.ar[key_index]:
                self.ar[parent_index], self.ar[key_index] = key, self.ar[parent_index]
                print("array during insertion stage - ", self.ar)
                key_index = parent_index
                parent_index = parent_index // 2
            else:
                return

    def display(self):
        print("FINAL Max heap ->", self.ar[1:])
        print()

    def delete(self):
        if len(self.ar) == 1:
            print("Heap is Empty Now ")
            return
        self.ar[1] = self.ar[-1]
        self.ar.pop()
        print("deletion first stage - putting last leafnode in root node ", self.ar)
        length = len(self.ar) - 1
        i = 1
        while 2 * i < length:
            leftchild_index = 2 * i
            rightchild_index = 2 * i + 1
            if self.ar[leftchild_index] >= self.ar[rightchild_index]:
                self.ar[leftchild_index], self.ar[i] = (
                    self.ar[i],
                    self.ar[leftchild_index],
                )
                i = leftchild_index
            else:
                self.ar[rightchild_index], self.ar[i] = (
                    self.ar[i],
                    self.ar[rightchild_index],
                )
                i = rightchild_index


h = Heap()
h.insert(30)
h.display()

h.insert(20)

h.display()

h.insert(15)

h.display()
h.insert(5)
h.display()
h.insert(10)
h.display()
h.display()
h.insert(12)
h.display()
h.insert(6)
h.display()

h.insert(40)
h.display()
h.delete()
h.display()
h.delete()
h.display()
h.delete()
h.display()
h.delete()
h.display()
h.delete()
h.display()
h.delete()
h.display()
h.delete()
h.display()
h.delete()
h.display()
h.delete()
h.display()
