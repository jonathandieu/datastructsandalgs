def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
    """
    Returns the number of car fleets that will arrive at the destination.
    """
    # 1. Sort the vehicles by (position, velocity) pair
    # 2. Use a stack to keep track of each vehicle
    # 3, The stack should contain the arrival times of the fleets