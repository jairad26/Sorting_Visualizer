import time

def bubble_sort(data, drawData, tick):
	for _ in range(len(data)-1):
		for j in range(len(data)-1):
			if(data[j] > data[j+1]):
				data[j], data[j+1] = data[j+1], data[j]
				drawData(data, ['red' if x == j or x == j + 1 else 'gray' for x in range(len(data))])
				time.sleep(tick)


##data = [10, 20 ,4, 1, 0, 123]
##bubble_sort(data, 0, len(data) - 1, 0, 0)
##print(data)