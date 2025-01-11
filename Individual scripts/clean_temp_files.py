def clean_temp_files():
    try:
        temp_folder = os.getenv('TEMP')
        if os.path.exists(temp_folder):
            for root, dirs, files in os.walk(temp_folder):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception:
                        continue
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir))
                    except Exception:
                        continue
        print("Temporary files cleaned.")
    except Exception as e:
        print(f"Failed to clean temporary files: {e}")
