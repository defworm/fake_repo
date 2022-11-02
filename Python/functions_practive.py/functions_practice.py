def hello():
print ("Hello!")

def pack(a, b, c)
    return [a, b, c]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print("First I eat my {my_list[0]}")
            else:
                print("Next I eat my {my_list[i]")

hello()
print(pack("a", "b", "c"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple", "banana", "sandwich", "cookie"])