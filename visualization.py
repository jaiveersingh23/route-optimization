import matplotlib.pyplot as plt

def plot_results(results):
    algorithms = [result["algorithm"] for result in results]
    distances = [result["distance"] for result in results]

    # Create a bar chart
    bars = plt.bar(algorithms, distances)

    # Display the y values (distances) on the bars
    for bar in bars:
        yval = bar.get_height()  # Get the height of the bar, which represents the distance
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

    plt.xlabel("Algorithms")
    plt.ylabel("Total Distance (meters)")
    plt.title("Comparison of Route Optimization Algorithms")
    plt.show()
