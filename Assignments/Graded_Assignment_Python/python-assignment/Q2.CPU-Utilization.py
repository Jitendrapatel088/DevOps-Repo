import psutil
import time

def monitor_cpu(threshold):
    try:
        while True:
            # Get the current CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)

            # Display the CPU usage
            print(f"Current CPU Usage: {cpu_usage}%")

            # Check if CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert: CPU Usage exceeds {threshold}%!")

            # Sleep for a short duration before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring interrupted. Exiting...")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set the predefined threshold (e.g., 80%)
    threshold = 80

    # Start monitoring the CPU
    monitor_cpu(threshold)