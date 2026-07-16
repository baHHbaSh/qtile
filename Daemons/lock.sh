#!/bin/bash

LOG="/tmp/lock.log"
exec > "$LOG" 2>&1

SCREENSHOT="/tmp/lockscreen.png"
BLUR="/tmp/lockscreen_blur.png"
BLUR_LEVEL=25
BACKGROUND="#2E3440AA"

# Проверка и создание скриншота
if command -v scrot &>/dev/null; then
    scrot -z "$SCREENSHOT" || { echo "scrot failed"; exit 1; }
elif command -v import &>/dev/null; then
    import -window root "$SCREENSHOT" || { echo "import failed"; exit 1; }
else
    echo "No screenshot tool (scrot or import) found."
    exit 1
fi

# Проверка, что файл создан
if [ ! -f "$SCREENSHOT" ]; then
    echo "Screenshot file not created."
    exit 1
fi

# Размытие
if command -v magick &>/dev/null; then
    magick "$SCREENSHOT" -blur 0x$BLUR_LEVEL -fill "$BACKGROUND" -colorize 30% "$BLUR" || { echo "magick failed"; exit 1; }
elif command -v convert &>/dev/null; then
    convert "$SCREENSHOT" -blur 0x$BLUR_LEVEL -fill "$BACKGROUND" -colorize 30% "$BLUR" || { echo "convert failed"; exit 1; }
else
    echo "No ImageMagick tool (magick or convert) found."
    exit 1
fi

if [ ! -f "$BLUR" ]; then
    echo "Blurred image not created."
    exit 1
fi

# Запуск i3lock
i3lock \
    --image "$BLUR" \
    --clock \
    --time-color 00ee33ff \
    --date-color ffffffff \
    --time-str "%H:%M:%S" \
    --date-str "%A, %d %B" \
    --time-font "Noto Sans" \
    --date-font "Noto Sans" \
    --verif-text "Открываем..." \
    --wrong-text "Неверный пароль" \
    --noinput-text "Вводи пароль" \
    --lock-text "Блокируем..." \
    --lockfailed-text "Ошибка" \
    --show-failed-attempts \
    --ignore-empty-password \
    --pass-media-keys \
    --pass-power-keys \
    --pass-volume-keys \
    --refresh-rate 1 \
    --bar-indicator \
    --bar-pos y+h \
    --bar-direction 1 \
    --bar-max-height 50 \
    --bar-base-width 50 \
    --bar-color 00000022 \
    --bar-periodic-step 50 \
    --bar-step 20 \
    --redraw-thread

# Удаление временных файлов (после завершения i3lock)
rm -f "$SCREENSHOT" "$BLUR"