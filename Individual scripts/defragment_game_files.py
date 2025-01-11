def defragment_game_files():
    try:
        game_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\ELDEN RING\\Game"
        if not os.path.exists(game_dir):
            print("Game directory not found. Would you like to specify the path manually? (Y/N): ")
            choice = input().strip().lower()
            if choice == 'y':
                game_dir = input("Enter the full path to the game directory: ").strip()
                if not os.path.exists(game_dir):
                    print("Invalid path provided. Defragmentation will not be performed.")
                    return

        subprocess.run(f"defrag {game_dir} /D /U /V", shell=True, check=True)
        print("Game files defragmented.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to defragment game files. Error: {e.stderr.decode().strip() if e.stderr else str(e)}")
    except Exception as e:
        print(f"Unexpected error during defragmentation: {e}")
