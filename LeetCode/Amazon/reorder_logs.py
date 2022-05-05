
def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Return final order of the logs such that:
        # Letter logs come before digit logs
        # Letter logs are sorted by their contents: if they're the same, then sort by identifier
        # Digit logs must maintain their relative ordering


        # Separate logs into letters and digits
        letter_logs = []
        number_logs = []

        for log in logs:
            if log.split(" ")[1].isdigit():
                number_logs.append(log)
            else:
                letter_logs.append(log)

        # Sort by letters before digits
        # Sort by contents of the letter logs
        # Sort by identifier if contents are the same
        letter_logs.sort(key= lambda (log.split()[1:], log.split()[0])) # Sort with multiple criteria, descending priority: first is contents, second is identifier

        sorted_logs = letter_logs + number_logs
        return sorted_logs