import psutil
import GPUtil

class SystemStress:
    def check_cpu_usage(self):
        usage = psutil.cpu_percent(interval=1)
        return f"{'High' if usage > 80 else 'Normal'} CPU usage ({usage}%)"

    def check_memory_usage(self):
        memory = psutil.virtual_memory()
        return f"{'High' if memory.percent > 80 else 'Normal'} memory usage ({memory.percent}%)"

    def check_gpu_usage(self):
        try:
            gpus = GPUtil.getGPUs()
            if not gpus:
                return "No GPU detected."
            usage = gpus[0].load * 100
            return f"{'High' if usage > 80 else 'Normal'} GPU usage ({usage:.2f}%)"
        except Exception as e:
            return f"GPU usage check failed: {e}"

    def check_cpu_temperature(self):
        try:
            temps = psutil.sensors_temperatures()
            for entries in temps.values():
                for entry in entries:
                    if entry.label == "Package id 0" or not entry.label:
                        temp = entry.current
                        return f"{'High' if temp > 75 else 'Normal'} CPU temperature ({temp}°C)"
            return "CPU temperature data not available."
        except Exception as e:
            return f"Temperature check failed: {e}"

    def check_disk_usage(self):
        usage = psutil.disk_usage('/').percent
        return f"{'High' if usage > 80 else 'Normal'} disk usage ({usage}%)"

    def check_battery_status(self):
        battery = psutil.sensors_battery()
        if battery:
            return f"{'Low' if battery.percent < 20 else 'Good'} battery level ({battery.percent}%)"
        return "Battery status not available."

    def check_network_usage(self):
        net = psutil.net_io_counters()
        return f"Sent: {net.bytes_sent / (1024 ** 2):.2f} MB, Received: {net.bytes_recv / (1024 ** 2):.2f} MB"

    def check_process_count(self):
        count = len(psutil.pids())
        return f"{'High' if count > 250 else 'Normal'} number of processes ({count})"

    def check_swap_usage(self):
        swap = psutil.swap_memory()
        return f"{'High' if swap.percent > 60 else 'Normal'} swap usage ({swap.percent}%)"

    def check_boot_time(self):
        boot_time = psutil.boot_time()
        return f"System boot time (epoch): {boot_time}"
