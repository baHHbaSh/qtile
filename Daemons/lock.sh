#!/bin/bash
i3lock \
    --bar-indicator \
    --bar-pos y+h \
    --bar-direction 1 \
    --bar-max-height 50 \
    --bar-base-width 50 \
    --bar-color 00000022 \
    --keyhl-color 00ff55cc \
    --bar-periodic-step 50 \
    --bar-step 20 \
    --redraw-thread \
    --clock \
    --time-color ffffffff \
    --date-color ffffffff \
    --time-str="%H:%M:%S" \
    --time-font "Noto Sans" \
    --date-font "Noto Sans" \
    --verif-text "Привет..." \
    --wrong-text "Ха, лох!" \
    --noinput-text "Чё смотришь?" \
    --lock-text "Лочим..." \
    --lockfailed-text "Ошибка!" \
    --show-failed-attempts \
    --ignore-empty-password \
    --pass-media-keys \
    --pass-power-keys \
    --pass-volume-keys \
    --refresh-rate 60             # частота обновления (FPS)


#i3lock \
#    --blur 5 \
#    --clock \
#    --time-color ffffffff \
#    --date-color ffffffff \
#    --time-str="%H:%M:%S" \
#    --date-str="%Y-%m-%d" \
#    --ring-color 00000088 \          # Цвет внешнего кольца
#    --inside-color 00000000 \        # Цвет внутренней части (прозрачный)
#    --line-color 00000000 \          # Цвет линии (прозрачный)
#    --separator-color 00000000 \     # Цвет разделителя (прозрачный)
#    --keyhl-color ffffffcc \         # Цвет подсветки клавиш
#    --ringver-color 00ff00ff \       # Цвет кольца при проверке
#    --ringwrong-color ff0000ff \     # Цвет кольца при ошибке
#    --verif-color ffffffff \         # Цвет текста проверки
#    --wrong-color ffffffff \         # Цвет текста ошибки
#    --modif-color ffffffff \         # Цвет текста модификатора
#    --layout-color ffffffff \        # Цвет текста раскладки
#    --time-font "Noto Sans" \
#    --date-font "Noto Sans" \
#    --time-size 20 \
#    --date-size 15