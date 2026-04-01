import subprocess
import sys
import time

print("🚀 Starting FastAPI Backend...")
backend = subprocess.Popen(
    [sys.executable, "-m", "uvicorn", "main:app", "--reload"]
)

# wait for backend to start
time.sleep(3)

print("🎨 Starting UI...")
ui = subprocess.Popen(
    [sys.executable, "app.py"]
)

try:
    backend.wait()
    ui.wait()
except KeyboardInterrupt:
    print("\n🛑 Shutting down...")
    backend.terminate()
    ui.terminate()