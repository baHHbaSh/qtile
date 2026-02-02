import subprocess
import re

def get_screen_resolution() -> tuple[int, int]:
    output = subprocess.check_output(['xrandr']).decode('utf-8')
    # Ищем строку с текущим разрешением (помеченную '*')
    match = re.search(r'\b(\d+)x(\d+)\s+\d+\.\d+\*', output)
    if match:
        return int(match.group(1)), int(match.group(2))
    # Если не нашли — берём первое упоминание текущего разрешения экрана
    match = re.search(r'current (\d+) x (\d+)', output)
    if match:
        return int(match.group(1)), int(match.group(2))
    raise RuntimeError("Не удалось определить разрешение")

if __name__ == "__main__":
    width, height = get_screen_resolution()
    print(f"Разрешение: {width}x{height}")