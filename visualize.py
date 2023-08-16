import matplotlib.pyplot as plt

throughput = [26.17, 49.85, 73.07, 94.35, 114.47, 133.52, 150.5, 166.78, 180.35, 180.37]

latency = [0.03823, 0.040034, 0.040924, 0.042172, 0.043409, 0.044666, 0.046224, 0.047644, 0.049897, 0.055383]

# Plotting
plt.figure(figsize=(8, 6))

plt.plot( throughput, latency, label='num_client: 1..10')


plt.xlabel('Throughput (query/second)')
plt.ylabel('Latency (second)')
plt.title('Throughput vs Latency (Duration 60 s)')
plt.legend()

plt.grid(True)
plt.show()
