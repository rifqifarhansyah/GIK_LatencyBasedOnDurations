import requests
import time
from concurrent.futures import ThreadPoolExecutor

def measure(duration, num_clients):
    jsonquery = {
        "Ls": 256,
        "query_id": 1234,
        "query": [0.00407, 0.01534, 0.02498],
        "k": 10
    }

    def make_request(_):
        global i
        i = 1
        latencies = []  # List to store latency values
        start_time = time.time()
        end_time = start_time + duration
        while time.time() < end_time:
            startTimeLatency = time.time()
            response = requests.post('http://localhost:3001', json=jsonquery)
            endTimeLatency = time.time()
            latency_per_response = endTimeLatency - startTimeLatency
            latencies.append(latency_per_response)  # Append latency to the list
            print(f"Latency {i}: {latency_per_response:.6f}")
            i += 1
        
        # Write latencies to a text file
        with open("latencies.txt", "a") as file:
            for latency in latencies:
                file.write(f"{latency:.6f}\n")
                
        return latencies  # Return latencies list for average calculation


    with ThreadPoolExecutor(max_workers=num_clients) as executor:
        latency_lists = list(executor.map(make_request, range(num_clients)))
        print(f"Num Clients: {num_clients}")
        print(f"Duration: {duration} seconds")

    total_latencies = [latency for latency_list in latency_lists for latency in latency_list]
    average_latency = sum(total_latencies) / len(total_latencies)

    throughput = i / duration

    return throughput, average_latency

duration = 60  # Duration in seconds
num_clients = 3
throughput, average_latency = measure(duration, num_clients)
print(f"Throughput: {throughput:.2f} queries per second")
print(f"Average Latency: {average_latency:.6f} seconds")
