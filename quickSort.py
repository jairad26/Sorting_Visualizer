import time

def Partition(data, head, tail, drawData, tick):
	midpoint = head + (tail - head) // 2
	pivot = data[midpoint]

	done = False
	lower = head
	higher = tail

	drawData(data, getColorArray(len(data), head, tail, lower, lower))
	time.sleep(tick)

	while(done == False):
		while(data[lower] < pivot):
			
			lower = lower + 1
			drawData(data, getColorArray(len(data), head, tail, lower, higher))
			time.sleep(tick)

		while(pivot < data[higher]):
			
			higher = higher - 1
			drawData(data, getColorArray(len(data), head, tail, lower, higher))
			time.sleep(tick)

		if(lower >= higher):
			done = True
		else:
			drawData(data, getColorArray(len(data), head, tail, lower, higher, True))
			time.sleep(tick)

			data[lower], data[higher] = data[higher], data[lower]

			lower = lower + 1
			higher = higher - 1

	return higher

def quick_sort(data, head, tail, drawData, tick):
	if(head < tail):
		partition = Partition(data, head, tail, drawData, tick)
		##left partition
		quick_sort(data, head, partition, drawData, tick)

		##right partition
		quick_sort(data, partition + 1, tail, drawData, tick)

def getColorArray(dataLen, head, tail, border, curr, isSwapping = False):
	colorArray = []
	for i in range(dataLen):
		#base coloring
		if i>= head and i <= tail:
			colorArray.append('gray')
		else:
			colorArray.append('white')

		if(i == tail):
			colorArray[i] = 'blue'
		elif(i == border):
			colorArray[i] = 'red'
		elif(i == curr):
			colorArray[i] = 'yellow'

		if (isSwapping):
			if(i == border or i == curr):
				colorArray[i] = 'green'

	return colorArray

##data = [10, 20 ,4, 1, 0, 123]
##quick_sort(data, 0, len(data) - 1, 0, 0)
##print(data)