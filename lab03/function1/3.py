def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbit = numheads - chickens
        if chickens*2+rabbit*4==numlegs:
            print(rabbit, chickens)
            return 0
    print("No Solution")

a = input()
b = input()
solve(int(a),int(b))
