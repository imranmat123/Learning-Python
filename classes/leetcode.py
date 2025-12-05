class Solution:
	def countPartitions(self, nums: List[int]) -> int:
		even = 0
		subArrayLeft = []
		subArrayRight = []
		for i in range(len(nums)):
			left = 0
			right = 0
			subArrayLeft = nums[0:i + 1]
			subArrayRight = nums[i + 1:]

			for j in subArrayLeft:
				left = left + j

			for a in subArrayRight:
				right = right + a

			if not subArrayRight:
				continue
			elif not subArrayRight:
				continue
			elif (left - right) % 2 == 0:
				even = even + 1

		return even


