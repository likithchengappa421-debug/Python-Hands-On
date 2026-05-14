from pathlib import Path

terminal_folder = Path.cwd()
script_location = Path(__file__).parent

print(f"The terminal is currently residing in: {terminal_folder}")
print(f"The script is currently residing in: {script_location}")