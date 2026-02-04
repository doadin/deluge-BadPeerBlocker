import os
import shutil
import subprocess
import sys

def main():
    # Remove old build artifacts
    for folder in ("build", "dist", "BadPeerBlocker.egg-info"):
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Removed: {folder}")

    # Build the egg
    print("Building BadPeerBlocker plugin...")
    result = subprocess.call([sys.executable, "setup.py", "bdist_egg"])

    if result != 0:
        print("Build failed.")
        sys.exit(result)

    # Show the output file
    dist_path = os.path.join("dist")
    files = os.listdir(dist_path)
    egg_files = [f for f in files if f.endswith(".egg")]

    if egg_files:
        print(f"Build complete. Egg created:")
        for egg in egg_files:
            print(f"  dist/{egg}")
    else:
        print("Build finished, but no .egg file found.")

if __name__ == "__main__":
    main()