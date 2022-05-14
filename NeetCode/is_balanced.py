# Return whether or not the binary search tree is balanced.
def is_balanced(root):
	# Helper function that returns -1 if not balanced
	def check(root):
		if not root:
			return 0
		else:
			left = check(root.left)
			right = check(root.right)
			if left == -1 or right == -1 or abs(left - right) > 1:
				return -1

			return 1 + max(left, right)

		return check(root) != 1