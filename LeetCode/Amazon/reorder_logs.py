
def reorder_logs(logs: list) -> list:
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
        letter_logs.sort(key= lambda log: (log.split()[1:], log.split()[0])) # Sort with multiple criteria, descending priority: first is contents, second is identifier

        sorted_logs = letter_logs + number_logs
        return sorted_logs

if __name__ == "__main__":
    test_list = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(reorder_logs(test_list) == ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])