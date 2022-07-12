def merge(arr, lf, mid, rg):
	result = []
	left = arr[lf:mid]
	right = arr[mid:rg]
	ileft = iright = 0
	while len(result) < len(left) + len(right):
		if left[ileft] <= right[iright]:
			result.append(left[ileft])
			ileft += 1
		else:
			result.append(right[iright])
			iright += 1
		if iright == len(right):
			result += left[ileft:]
			break
		if ileft == len(left):
			result += right[iright:]
			break
	return result


def merge_sort(arr, lf, rg):
	if rg - lf >= 2:
		mid = (lf + rg) // 2
		merge_sort(arr, lf, mid)
		merge_sort(arr, mid, rg)
		arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0, 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected


if __name__ == '__main__':
	test()
