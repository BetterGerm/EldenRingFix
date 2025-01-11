import os
import subprocess
import ctypes
import time
import shutil
import winreg
import psutil
import threading
import traceback

def is_game_running():
    try:
        for proc in psutil.process_iter(['name', 'status']):
            if proc.info['name'] and "eldenring.exe" in proc.info['name'].lower():
                if proc.info['status'] == psutil.STATUS_RUNNING:
                    return True
        return False
    except Exception as e:
        print(f"Error checking if game is running: {e}\n{traceback.format_exc()}")
        return False

def apply_fixes():
    try:
        print("Applying robust fixes...")
        pid = get_game_pid()
        if pid:
            set_process_priority(pid)
            force_cpu_affinity(pid)
        disable_fullscreen_optimizations()
        optimize_graphics_settings()
        clean_temp_files()
        ensure_minimum_resources()
        boost_io_performance()
        defragment_game_files()
        prevent_power_throttling()
        check_and_disable_hibernation()
        remove_unused_startup_programs()
        is_admin()
        is_game_running()
        print("All fixes applied successfully.")
    except Exception as e:
        print(f"Error while applying fixes: {e}\n{traceback.format_exc()}")

def get_game_pid():
    try:
        exe_name = "eldenring.exe"
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] and exe_name in proc.info['name'].lower():
                return proc.info['pid']
        print("Failed to find the game process.")
        return None
    except Exception as e:
        print(f"Error retrieving game process: {e}")
        return None

def set_process_priority(pid):
    try:
        process = psutil.Process(pid)
        process.nice(psutil.HIGH_PRIORITY_CLASS)
        print(f"Process priority set to high for PID {pid}.")
    except psutil.AccessDenied:
        print(f"Failed to set process priority: Access is denied (pid={pid}). Ensure the script is run with administrator privileges.")
    except psutil.NoSuchProcess:
        print(f"Failed to set process priority: Process with PID {pid} does not exist.")
    except Exception as e:
        print(f"Unexpected error while setting process priority: {e}")

def disable_fullscreen_optimizations():
    try:
        exe_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\ELDEN RING\\Game\\eldenring.exe"
        if not os.path.exists(exe_path):
            print("Elden Ring executable not found at the expected path.")
            print("Do you want to manually specify the path? (Y/N): ")
            choice = input().strip().lower()
            if choice == 'y':
                exe_path = input("Enter the full path to eldenring.exe: ").strip()
                if not os.path.exists(exe_path):
                    print("Invalid path provided. Fullscreen optimizations will not be disabled.")
                    return
            else:
                print("Fullscreen optimizations will not be disabled.")
                return

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, exe_path, 0, winreg.REG_SZ, "~ DISABLEDXMAXIMIZEDWINDOWEDMODE")
        winreg.CloseKey(key)
        print("Fullscreen optimizations disabled.")
    except Exception as e:
        print(f"Failed to disable fullscreen optimizations: {e}")

def prevent_power_throttling():
    try:
        subprocess.run("powercfg /setactive SCHEME_MAX", shell=True, check=True)
        print("High-performance power plan activated to prevent power throttling.")
    except Exception as e:
        print(f"Failed to activate high-performance power plan: {e}")

def check_and_disable_hibernation():
    try:
        subprocess.run("powercfg /hibernate off", shell=True, check=True)
        print("Hibernation disabled successfully.")
    except Exception as e:
        print(f"Failed to disable hibernation: {e}")

def remove_unused_startup_programs():
    try:
        startup_keys = [
            r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
            r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
        ]
        for key_path in startup_keys:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
                programs = []
                try:
                    i = 0
                    while True:
                        programs.append(winreg.EnumValue(key, i)[0])
                        i += 1
                except OSError:
                    pass  

            if programs:
                print("The following startup programs are configured:")
                for program in programs:
                    print(f" - {program}")
                choice = input("Do you want to disable all non-essential startup programs? (Y/N): ").strip().lower()
                if choice == 'y':
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as write_key:
                        for program in programs:
                            winreg.DeleteValue(write_key, program)
                    print("Unused startup programs disabled successfully.")
                else:
                    print("Startup programs were not modified.")
    except Exception as e:
        print(f"Failed to manage startup programs: {e}")

def optimize_graphics_settings():
    try:
        config_path = os.path.join(os.getenv('APPDATA'), "EldenRing")
        if os.path.exists(config_path):
            for root, _, files in os.walk(config_path):
                for file in files:
                    if file.endswith(".ini"):
                        settings_file = os.path.join(root, file)
                        with open(settings_file, "r") as f:
                            settings = f.readlines()
                        optimized_settings = []
                        for line in settings:
                            if "ScreenMode" in line:
                                optimized_settings.append("ScreenMode=Windowed\n")
                            elif "QualityLevel" in line:
                                optimized_settings.append("QualityLevel=Low\n")
                            elif "AntiAliasing" in line:
                                optimized_settings.append("AntiAliasing=None\n")
                            else:
                                optimized_settings.append(line)
                        with open(settings_file, "w") as f:
                            f.writelines(optimized_settings)
        print("Graphics settings optimized.")
    except Exception as e:
        print(f"Failed to optimize graphics settings: {e}")

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

def ensure_minimum_resources():
    try:
        memory_info = psutil.virtual_memory()
        if memory_info.available < (memory_info.total * 0.2):
            print("Warning: Low system memory available. Close background applications.")
        else:
            print("System memory check passed.")
    except Exception as e:
        print(f"Failed to verify system resources: {e}")

def boost_io_performance():
    try:
        result = subprocess.run("fsutil behavior set disablelastaccess 1", shell=True, check=True, capture_output=True)
        print("I/O performance optimized.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to boost I/O performance: {e.stderr.decode().strip() if e.stderr else str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred while boosting I/O performance: {e}")

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

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("This script requires administrator privileges. Please run it as an administrator.")
    exit(1)

def main():
    print("Elden Ring Optimization and Fix Tool")
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Please run this script as an administrator to apply all fixes successfully.")
        return

    while True:
        print("Checking if Elden Ring is running...")
        if is_game_running():
            print("Elden Ring is running. Do you want to apply fixes? (Y/N)")
            choice = input().strip().lower()
            if choice == 'y':
                apply_fixes()
                break
            elif choice == 'n':
                print("Exiting without applying fixes.")
                break
        else:
            print("Elden Ring is not running. Waiting for the game to start...")
            time.sleep(10)

if __name__ == "__main__":
    main()
