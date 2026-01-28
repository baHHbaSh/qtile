# Убить все процессы PulseAudio
pulseaudio -k

# Удалить конфигурацию PulseAudio (создастся заново)
rm -rf ~/.config/pulse

# Перезагрузить демон systemd
systemctl --user daemon-reload

# Попробовать запустить вручную
pulseaudio --start

# Если запустился вручную, остановить и попробовать через systemd
pulseaudio -k
systemctl --user start pulseaudio.service