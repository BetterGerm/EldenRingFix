def boost_io_performance():
    try:
        result = subprocess.run("fsutil behavior set disablelastaccess 1", shell=True, check=True, capture_output=True)
        print("I/O performance optimized.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to boost I/O performance: {e.stderr.decode().strip() if e.stderr else str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred while boosting I/O performance: {e}")
