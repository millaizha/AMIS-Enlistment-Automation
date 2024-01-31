import subprocess
import sys

def install_required_modules():
    required_modules = [
        "selenium",
        "webdriver_manager"
    ]

    try:
        for module in required_modules:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        
        print("All required modules installed successfully.")
    except Exception as e:
        print(f"Error installing modules: {e}")

if __name__ == "__main__":
    install_required_modules()