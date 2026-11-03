
def canShip(weights, days, capacity):
    days_needed = 1
    current_load = 0

    for weight in weights:
        if current_load + weight <= capacity:
            current_load += weight
        else:
            days_needed += 1
            current_load = weight

    return days_needed <= days


def shipWithinDays(weights, days):

    left = max(weights)
    right = sum(weights)

    while left < right:

        mid = left + (right - left) // 2

        if canShip(weights, days, mid):
            right = mid
        else:
            left = mid + 1

    return left


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(shipWithinDays(weights, days))
