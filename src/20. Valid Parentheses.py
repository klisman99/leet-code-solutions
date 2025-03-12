class Solution:
	def isValid(self, s: str) -> bool:
		brackets = {
			"(": ")",
			"[": "]",
			"{": "}"
		}
		stack = []

		for c in s:
			if brackets.get(c, 0) != 0:
				stack.append(c)
			elif len(stack) == 0 or brackets.get(stack.pop()) != c:
				return False

		return len(stack) == 0