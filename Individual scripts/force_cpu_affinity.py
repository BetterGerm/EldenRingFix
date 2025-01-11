def force_cpu_affinity(pid):
    try:
        process = psutil.Process(pid)
        cpu_count = os.cpu_count()
        if cpu_count > 1:
            affinity_mask = list(range(cpu_count))
            process.cpu_affinity(affinity_mask[:max(1, cpu_count // 2)])
        print(f"CPU affinity adjusted for optimal performance (pid={pid}).")
    except psutil.AccessDenied:
        print(f"Failed to set CPU affinity: Access is denied (pid={pid}).")
    except psutil.NoSuchProcess:
        print(f"Failed to set CPU affinity: Process with PID {pid} does not exist.")
    except Exception as e:
        print(f"Unexpected error while setting CPU affinity: {e}")
