"""
Simple Hospital Queue Simulation Demo

This script demonstrates basic queue behavior modeling.
It is a mock analytical simulation and not intended for real medical use.
"""

import random

def simulate_queue(arrival_rate=8, service_rate=10, hours=8):
    """
    Arrival Rate = patients per hour entering system
    Service Rate = patients processed per hour
    """

    queue_length = 0
    waiting_records = []

    for hour in range(hours):
        arrivals = random.randint(arrival_rate - 3, arrival_rate + 3)
        services = random.randint(service_rate - 2, service_rate + 2)

        queue_length += arrivals
        processed = min(queue_length, services)
        queue_length -= processed

        waiting_records.append({
            "hour": hour + 1,
            "arrivals": arrivals,
            "services": services,
            "queue_remaining": queue_length
        })

    return waiting_records

if __name__ == "__main__":
    result = simulate_queue()

    for record in result:
        print(record)