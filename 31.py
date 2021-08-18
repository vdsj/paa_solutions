def turn(a, biggest_pancake):
	top = 0
	while top < biggest_pancake:
		aux = a[top]
		a[top] = a[biggest_pancake]
		a[biggest_pancake] = aux
		top = top +1
		biggest_pancake = biggest_pancake -1

def biggest_pancake_id(a, size):
	id = 0
	for i in range(size):
		if a[i] > a[id]:
			id = i
	return id

def sorting(a):
    size_p = len(a)
    while size_p > 1:
        biggest_pancake = biggest_pancake_id(a, size_p)
        print("\na: ", a, "Current biggest pancake: ", a[biggest_pancake],"\tId of biggest pancake: [", biggest_pancake, "]")
        if biggest_pancake == size_p-1:
            size_p = size_p - 1
            print("not turn.")
        else:
            if size_p != 2:
                turn(a, biggest_pancake)
                print("Turned to the top", pancakes)
            turn(a, size_p - 1)
            print("Turned to base", pancakes)
            size_p = size_p - 1


pancakes = [2, 4, 6, 1, 3, 7, 5]
print(pancakes)
print(len(pancakes))
sorting(pancakes)
print("\nFinal: ", pancakes)
