def non_overlapping_intervals(intervals) -> int:
	end = float('-inf')
	removed_intervals = 0
	for interval_start, interval_end in sorted(intervals, key=lambda x: x[1]):
		if interval_start >= interval_end:
			end = interval_end
		else:
			removed_intervals += 1
	return removed_intervals += 1
