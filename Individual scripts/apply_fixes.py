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
